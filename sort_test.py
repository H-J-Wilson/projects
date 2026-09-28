"""Testing sorting algorithams"""

import random
import time

list_nums = []
times_one = []


def main():
    """Create random numbers, run tets"""
    for i in range(1000):
        random_num = random.uniform(0, 10000)
        list_nums.append(random_num)

    #print(list_nums, "\n")

    start = time.time()
    results = sort_one(list_nums)
    end = time.time()

    total = end - start
    #print(results, "\n")
    print(f"{total * 1000:.3f}ms")
    times_one.append(total)

def sort_one(nums):

    leng = len(nums)

    for i in range(leng):
        for j in range (leng):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

def sort_two(nums):

    leng = len(nums)

    for i in range(leng):
        swaped = False

        for j in range():



if __name__ == "__main__":
    main()
