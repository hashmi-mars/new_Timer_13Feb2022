# lets make a count down timer in python
# first, we need to import time

import time

# next lets ask the user how many seconds we want to count down from

seconds = int(input("How many seconds to wait?"))

# next, lets use a ranged loop to count downards

for i in range(seconds):
    print(str(seconds - i) + "seconds remain")
    time.sleep(1) #Make python sleep for 1 second between each iteration

print("Time is uP!!")
