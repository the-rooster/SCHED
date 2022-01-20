# SCHED
 a simple command line scheduler.
 
 compile to exe with PyInstaller and add to PATH for optimal experience.
 
 Arguments:
 schedule.py <list|add|remove|done|edit> [-a <task name>] [-d <date info>] [-n <additional notes>] [-f]
 
 list:<br />
 lists all unfinished tasks. use -f flag to show all tasks<br />
 
 add:<br />
 requires -a <task name> and -d <date info><br />
 optional -n <additional notes><br />
 adds the specified task to the local task json file<br />
 
 remove:<br />
 requires -a <task name><br />
 removes an unfinished task with the specified name from the local task json file<br />
 
 done:<br />
 requires -a <task name><br />
 tags a task as done. will not show up in list unless -f flag is used.<br />
 
 edit:<br />
 requires -a <task name><br />
 updates a task to contain new info for -d <date info> and -n <additional notes><br />
 
 TASK JSON FILE:<br />
 specified in path variable of included file config_scheduler.json which should be in the same directory as the executable or python file.<br />
 
 
 
