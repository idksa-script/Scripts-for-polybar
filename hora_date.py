#!/usr/bin/env python3
import time
while True:
    hora = time.strftime("%H:%M:%S")
    print(hora, flush=True)
    time.sleep(1)
