# Author: Adam Jeffries
# Date: 2/24/2021
# Description: A decorator function named sort_timer that times how many seconds it takes the decorated function to run.

import random
import time
import matplotlib.pyplot as plt
from functools import wraps


def sort_timer(func):
    @wraps(func)
    def sort_dec(numbers):
        begin = time.perf_counter()
        func(numbers)
        end = time.perf_counter()
        return end - begin
    return sort_dec


@sort_timer
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(dec1_bubble, dec2_ins):
    list1 = []
    list2 = []
    list3 = []
    size = 1000
    while size < 10001:
        numbers = [random.randint(1, 10000) for x in range(size)]
        copy = list(numbers)
        time_dec1 = dec1_bubble(numbers)
        time_dec2 = dec2_ins(copy)
        list1.append(size)
        list2.append(time_dec1)
        list3.append(time_dec2)
        size += 1000
    plt.plot(list1, list2, 'ro--', linewidth=2, label='Bubble Sort')
    plt.plot(list1, list3, 'go--', linewidth=2, label='Insertion Sort')
    plt.legend(loc="upper left")
    plt.show()


compare_sorts(bubble_sort, insertion_sort)
