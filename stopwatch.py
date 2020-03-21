#! python3
# stopwatch.py - A simpl estopwatch program

import time

# Disply the program's instructions
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Prest CRTL-C to quit.')
input()
print('Started...')
startTime = time.time()
lastTime = startTime
lapNum = 1

# TODO: start tracking the lap times.
try:
  while True:
    input()
    lapTime = round(time.time() - lastTime, 2)
    totalTime = round(time.time() - startTime, 2)
    print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
    lapNum += 1
    lastTime= time.time()
except KeyboardInterrupt:
  # Handle the CTRL-C exception to keep its error message from displaying.
  print('\nDone.')
