# concurrent and parallelism;

# what is concurrent - multiple task at once in a single core

# parallelism -- multiple task at exect same time in  a multiple core

import threading
import time

def one():
    print('Hello')
    time.sleep(2)

def two():
    print('Hello 2')
    time.sleep(2)


one_thread = threading.Thread(target=one)
two_thread = threading.Thread(target=two)

one_thread.start()
two_thread.start()
# invoke or join to 
one_thread.join()
two_thread.join()


# cuncurrency 
# first task sleep take 2s and second task takes 2 second
#  python execute the first and not wait for there to second it excute and switch beteern second and one core and multiple task switching 



# Parallelism:
# multiple core 
# from multiprocessing import Process, Queue
# import time

# def partial_sum(start, end, q):
#     total = 0
#     for i in range(start, end):
#         total += i
#     q.put(total)   # put result in queue

# if __name__ == "__main__":
#     N = 10**7
#     num_processes = 4
#     step = N // num_processes
#     q = Queue()

#     start_time = time.time()
#     processes = []

#     for i in range(num_processes):
#         start = i * step
#         end = (i + 1) * step if i != num_processes - 1 else N
#         p = Process(target=partial_sum, args=(start, end, q))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()

#     total_sum = sum(q.get() for _ in processes)
#     end_time = time.time()

#     print(f"Total sum = {total_sum}")
#     print(f"Finished in {end_time - start_time:.2f} seconds")

# one task  split into multiple process and combine at the end for sequence orders

#Race condtions - memory need loock for one thread , if 2 thread access and modify the thread at same time it a problem memory need to access sync , uses mutex , GLI .
# Lock the memory for concurrent memory:

# import threading

# counter = 0
# lock = threading.Lock()  # create a lock

# def increment():
#     global counter
#     for _ in range(100000):
#         with lock:          # acquire lock before modifying
#             counter += 1    # critical section

# threads = [threading.Thread(target=increment) for _ in range(2)]
# for t in threads: t.start()
# for t in threads: t.join()

# print("Counter:", counter)  # now reliably 200000


# IF  a function inside a varibale is created it good to go for all threading and process beacuse each fun has its own memory no problem 
# but with Global variable race condition happens so we need to lock the statemennts;

# from multiprocessing import Process, Value, Lock

# counter = Value('i', 0)  # shared integer across processes
# lock = Lock()

# def increment():
#     for _ in range(1000):
#         with lock:
#             counter.value += 1

# processes = [Process(target=increment) for _ in range(2)]
# for p in processes: p.start()
# for p in processes: p.join()

# print("Counter:", counter.value)