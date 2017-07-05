import time

def time_execution(code):
    start = time.clock() #time.clock -> proccesor time (in seconds)
    result = eval(code) # eval(string)
    run_time = time.clock() - start# execution time
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1

#console:
#time_execution('1+15')
#time_execution('spin_loop(2000)')
