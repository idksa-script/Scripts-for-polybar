#!/usr/bin/env python3
import sys
from datetime import datetime

state_file = "/tmp/polybar_time_state"

def get_state():
    try:
        with open(state_file, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "time"

def set_state(state):
    with open(state_file, "w") as f:
        f.write(state)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "click":
        current_state = get_state()
        new_state = "date" if current_state == "time" else "time"
        set_state(new_state)
    else:
        current_state = get_state()
        if current_state == "time":
            print(datetime.now().strftime("%H:%M:%S"), flush = True)
        else:
            print(datetime.now().strftime("%Y-%m-%d"), flush = True)

if __name__ == "__main__":
    main()
