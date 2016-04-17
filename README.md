# ChartSpan Python Exercise
Exercise using python for charspan project

WRITTEN WITH PYTHON 3.5.1
by: Kyle Burkett 4.17.16

#### Exercise:

Background

You have a system that processes patients by their patient id (called a pid) and extracts records for them. The script must be able to handle being restarted. It does this by looking for a current pid file. If it finds it then the script should start processing after the current pid. As pids are processed the current pid file should be updated with the pid being processed.

Assignent

Write a python script that looks for 2 files, one containing the list of pids to be processed and one containing the current pid to start at. The list of pids should be sorted and then processing should pick up at the current pid. For processing simply call a function that prints out a message like "Processing pid: XXXX" For example, if the pids look like ['1', '7', '6', '2'] then the sorted list should be ['1', '2', '6', '7']. If the current pid is '2' then the script should process ['2', '6', '7']

See pid list and current pid file (Included in first project commit as current_pid.txt and pids.txt)

#### Output

![Alt text](/output.PNG?raw=true "My Script Output")
