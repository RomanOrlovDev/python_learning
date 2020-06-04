# process properties:
# PID
# RAM allocation
# stack
# opened files
# input / output

# python program for test:
# let's name our command py1.py
import time
import os

pid = os.getpid()

while True:
    print(pid, time.time())
    time.sleep(2)

# top - display list of processes
# ps axu - also display list of processes
# ps aux | head -1; ps aux | grep "name_of_python_file.py" - display running python program among processes
# sudo strace -p "PID"s - display how OS interacts with process
# lsof -p "PID" - display opened files for process,
# if we run our python program as:
# python3 py1.py
# then we can see that our program has following files for errors, input and output
# python3 105 rorlov    0u   CHR    4,2          1688849860746014 /dev/tty2
# python3 105 rorlov    1u   CHR    4,2          1688849860746014 /dev/tty2
# python3 105 rorlov    2u   CHR    4,2          1688849860746014 /dev/tty2
# if we run our python program as:
# python3 py1.py > log.txt
# we will see that our output file has been changed:
# python3 139 rorlov    0u   CHR    4,2          1688849860746014 /dev/tty2
# python3 139 rorlov    2u   CHR    4,2          1688849860746014 /dev/tty2
# python3 139 rorlov    1w   REG    0,2       0 15481123719263339 /home/rorlov/playground/log.txt

