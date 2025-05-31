import time
import threading
import multiprocessing

def sum_normal():
    return sum(range(1, 10000001))


def sum_thread(result, index):
    result[index] = sum(range(1, 10000001))


def sum_process(index, return_dict):
    return_dict[index] = sum(range(1, 10000001))

if __name__ == "__main__":
   
    start_time = time.time()
    sum_normal()
    normal_time = time.time() - start_time
    print(f"Normal function time: {normal_time:.6f} seconds")

   
    start_time = time.time()
    result = [0]
    thread = threading.Thread(target=sum_thread, args=(result, 0))
    thread.start()
    thread.join()
    threading_time = time.time() - start_time
    print(f"Threading time: {threading_time:.6f} seconds")

   
    start_time = time.time()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    process = multiprocessing.Process(target=sum_process, args=(0, return_dict))
    process.start()
    process.join()
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing time: {multiprocessing_time:.6f} seconds")
