# https://realpython.com/intro-to-python-threading/
# https://realpython.com/python-gil/#how-to-deal-with-pythons-gil
# https://realpython.com/async-io-python/
# https://docs.python.org/3/library/threading.html


# import time
# from threading import Thread

# COUNT = 50000000

# def countdown(n):
#     while n>0:
#         n -= 1

# start = time.time()
# countdown(COUNT)
# end = time.time()

# print('Time taken in seconds -', end - start)


# multi_threaded.py
import time
from threading import Thread

# COUNT = 50000000

# def countdown(n):
#     while n>0:
#         n -= 1

# t1 = Thread(target=countdown, args=(COUNT//2,))
# t2 = Thread(target=countdown, args=(COUNT//2,))

# start = time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.time()

# print('Time taken in seconds -', end - start)
# from multiprocessing import Pool
# import time

# COUNT = 50000000
# def countdown(n):
#     while n>0:
#         n -= 1

# if __name__ == '__main__':
#     pool = Pool(processes=2)
#     start = time.time()
#     r1 = pool.apply_async(countdown, [COUNT//2])
#     r2 = pool.apply_async(countdown, [COUNT//2])
#     pool.close()
#     pool.join()
#     end = time.time()
#     print('Time taken in seconds -', end - start)

# import logging
# import concurrent.futures
# class FakeDatabase:
#     def __init__(self):
#         self.value = 0

#     def update(self, name):
#         logging.info("Thread %s: starting update", name)
#         local_copy = self.value
#         local_copy += 1
#         time.sleep(0.1)
#         self.value = local_copy
#         logging.info("Thread %s: finishing update", name)


# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     database = FakeDatabase()
#     logging.info("Testing update. Starting value is %d.", database.value)
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         for index in range(2):
#             executor.submit(database.update, index)
#     logging.info("Testing update. Ending value is %d.", database.value)

def inc(x):
   x += 1
import dis
dis.dis(inc)