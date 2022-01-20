import json
import os
import sys
import argparse

#change to directory of script
abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('cmd',type=str,help="One of list, add, remove, done or edit")
parser.add_argument('-a',type=str,help="Assignment name. Required for add,done and edit")
parser.add_argument('-d',type=str,help="Date of assignment. Required when adding an assignment. Write whatever you want")
parser.add_argument('-n',type=str,help="Notes to attach to an assignment. Optional")
parser.add_argument('-f',action='store_true',help="Flag for listing all assignments, not just unfinished ones")


def main():

    if not os.path.isfile("config_scheduler.json"):
        with open("config_scheduler.json","w+") as f:
            f.write("{\"path\" : \"\"}")

    with open("config_scheduler.json") as f:
        config = json.loads(f.read())

    if config["path"] == "":
        config["path"] = ".\schedule_info.json"
    
    if not os.path.isfile(config["path"]):
        with open(config["path"],"w+") as f:
            f.write("{\"planner\" : []}")

    with open(config["path"]) as f:
        data = json.loads(f.read())

    args = parser.parse_args()

    cmd = args.cmd
    name = args.a
    date = args.d
    notes = args.n
    list_flag = args.f

    if cmd == "add":
        current = {}
        if name and date:
            current["name"] = name
            current["date"] = date
        else:
            print("Adding an assignment requires --a and --d")
            return
        
        if notes:
            current["notes"] = notes

        current["finished"] = False

        data["planner"].append(current)

    elif cmd == "list":
        for item in data["planner"]:
            if not item["finished"] or list_flag:
                if "notes" in item:
                    print(item["name"] +" | " + item["date"] + " | " + item["notes"] + " | " "FINISHED = " + str(item["finished"]))
                else:
                    print(item["name"] +" | " + item["date"] + " | " + " | " "FINISHED = " + str(item["finished"]))
    elif cmd == "remove":

        if not name:
            print("--a required")
            return
        
        ind = -1
        for i in range(len(data["planner"])):
            if data["planner"][i]["name"].lower() == name.lower() and not data["planner"][i]["finished"]:
                ind = i
        print(name + " succesfully deleted!")
        data["planner"].pop(ind)

    elif cmd == "done":

        if not name:
            print("Requires --a")
            return

        for i in range(len(data["planner"])):
            if data["planner"][i]["name"].lower() == name.lower() and not data["planner"][i]["finished"]:
                data["planner"][i]["finished"] = True
                print(name + " marked as done!")

    elif cmd == "edit":

        for i in range(len(data["planner"])):
            if data["planner"][i]["name"].lower() == name.lower() and not data["planner"][i]["finished"]:
                if date:
                    data["planner"][i]["date"] = date
                if notes:
                    data["planner"][i]["notes"] = notes
                print(name + " was succesfully edited.")
    else:
        print("cmd invalid. Must be one of list, add, remove, done or edit")



    with open(config["path"],"w") as f:
        json.dump(data,f)
        






    


    




if __name__ == "__main__":
    
    main()