from concurrent.futures import ThreadPoolExecutor, wait
import time

COUNT = 25000000
def countdown(n):
    while n > 0:
        n = n - 1
    return "Result"    

start = time.time()

with ThreadPoolExecutor(2) as executor:
    future1 = executor.submit(countdown, COUNT)
    future2 = executor.submit(countdown, COUNT)
    wait([future1, future2])

end = time.time()
print(end - start)