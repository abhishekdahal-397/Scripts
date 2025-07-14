#!/usr/bin/env python3

import subprocess
import time
import os

LOCK_CHECK_COMMAND = ["cinnamon-screensaver-command", "-q"]
LOCKED_STRING = "The screensaver is active"
WAIT_TIME = 20*60# 20 minutes in seconds
CHECK_INTERVAL = 10  # check every 10 seconds

def is_locked():
    try:
        output = subprocess.check_output(LOCK_CHECK_COMMAND).decode()
        return LOCKED_STRING in output
    except Exception as e:
        print(f"Error checking lock state: {e}")
        return False

def shutdown():
    print("Shutting down...")
    os.system("sudo /sbin/shutdown -h now")

while True:
    if is_locked():
        print("Screen is locked. Waiting 20 minutes...")
        time.sleep(WAIT_TIME)
        if is_locked():
            shutdown()
        else:
            print("Screen unlocked during the wait. Cancel shutdown.")
    time.sleep(CHECK_INTERVAL)

