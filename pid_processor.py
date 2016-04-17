#WRITTEN WITH PYTHON 3.5.1
#by: Kyle Burkett 4.17.16

#using time to sleep to fake processing
import time
# Function to process pid
def process( str ):
    print ("Processing patient with id: " + pid + "... ", end="")
    time.sleep(1)
    with open('current_pid.txt', 'w') as f:
        f.write(pid)
        f.close()
    print ("complete.")
    return
#get starting point
with open('current_pid.txt', 'r') as f:
    startnum = f.read()
    print ("Start processing patient with id: " + startnum)
    startnum = int(startnum)
    f.close()
#read and sort pids in int array
with open('pids.txt', 'r') as f:
    pid_raw = f.read().splitlines()
pid_ints = [int(i) for i in pid_raw]
pid_ints.sort()
#cycle through ints to find starting point
for num in (y for y in pid_ints if y > startnum):
    pid = str(num)
    process(pid)

print ("All Patients In pids.txt Now Processed")