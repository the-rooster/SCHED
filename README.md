# SCHED
 a simple command line scheduler that doesn't get in your way
 
 compile to exe with PyInstaller and add to PATH for optimal experience.
 
 Arguments:
 schedule.py <list|add|remove|done|edit> [-a <task name>] [-d <date info>] [-n <additional notes>] [-f]
 
 list:
 lists all unfinished tasks. use -f flag to show all tasks
 
 add:
 requires -a <task name> and -d <date info>
 optional -n <additional notes>
 adds the specified task to the local task json file
 
 remove:
 requires -a <task name>
 removes an unfinished task with the specified name from the local task json file
 
 done:
 requires -a <task name>
 tags a task as done. will not show up in list unless -f flag is used.
 
 edit:
 requires -a <task name>
 updates a task to contain new info for -d <date info> and -n <additional notes>
 
 TASK JSON FILE:
 specified in path variable of included file config_scheduler.json which should be in the same directory as the executable or python file.
 
 
 
