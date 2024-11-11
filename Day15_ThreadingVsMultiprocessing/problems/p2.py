'''
Problem 2: Multi-process Summation
Task: Write a function that calculates the sum of numbers from 1 to a large number (e.g., 1,000,000)
using multiple processes. Divide the range of numbers equally among processes, compute the 
sum for each subset, and then aggregate the results from all processes.

Expected Output:
The output should be the sum of all numbers from 1 to 1,000,000.
'''
from multiprocessing import Process, Manager
import os

def summation(start, end, result_list):
    partial_sum = sum(range(start, end))
    result_list.append(partial_sum)

if __name__ == '__main__':
    total_sum_range = 1_000_000
    cpu_count = os.cpu_count()
    chunk_size = total_sum_range // cpu_count  # Divide the range equally

    with Manager() as manager:
        result_list = manager.list()
        processes = []

        for i in range(cpu_count):
            start = i * chunk_size + 1
            end = start + chunk_size if i < cpu_count - 1 else total_sum_range + 1
            p = Process(target=summation, args=(start, end, result_list))
            processes.append(p)
            p.start()

        # Join all processes
        for p in processes:
            p.join()

        # Aggregate results from all processes
        total_sum = sum(result_list)
        print("Total sum:", total_sum)
