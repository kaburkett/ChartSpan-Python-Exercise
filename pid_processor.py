#using time to sleep to fake processing
import time

#get starting point
with open('current_pid.txt', 'r') as f:
    startnum = f.read()
    startnum = int(startnum)
#read and sort pids in int array
with open('pids.txt', 'r') as f:
    pid_raw = f.read().splitlines()
pid_ints = [int(i) for i in pid_raw]
pid_ints.sort()
#cycle through ints to find starting point
for num in pid_ints:
    if num == startnum:
        for num in pid_ints:
            print ("Processing patient with id: " + str(num) + "... ", end="")
            time.sleep(1)
            print ("complete.")

#print (pid_ints)