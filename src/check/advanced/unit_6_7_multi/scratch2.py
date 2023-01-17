import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
from reactivex import from_future
COUNT = 25000000

def countdown(n):
    while n>0:
        n -= 1
    return "Dome"

start = time.time()

with ProcessPoolExecutor(5) as executor:
    future1 = executor.submit(countdown, COUNT)
    future2 = executor.submit(countdown, COUNT)
    future3 = executor.submit(countdown, COUNT)
    future4 = executor.submit(countdown, COUNT)
    from_future(future1).subscribe(lambda s: print(f"finished {s}"))
    from_future(future2).subscribe(lambda s: print(f"finished {s}"))
    from_future(future3).subscribe(lambda s: print(f"finished {s}"))
    from_future(future4).subscribe(lambda s: print(f"finished {s}"))
    wait([future1, future2, future3, future4])

# t1.start()
# t2.start()
# t1.join()
# t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

