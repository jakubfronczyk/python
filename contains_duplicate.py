# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicateBrutalForce(nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return print(f"The array contains duplicates: {nums[i]} == {nums[j]}")
        print("The array does not contain duplicates.")

def containsDuplicateSorting(nums):
        nums.sort()
        for i in range (len(nums) - 1):
            if nums[i] == nums[i+1]:
                return print(f"The array contains duplicates: {nums[i]} == {nums[i+1]}")
        print("The array does not contain duplicates.")

def containsDuplicateHashSet(nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return print(f"The array contains duplicates: {n} == {n}")
            hashset.add(n)
        print("The array does not contain duplicates.")

while True:
    nums = list(map(int, input("Enter the elements of the array, separated by spaces: ").strip().split()))
    algorithm = int(input("Which algorithm do you want to use:\n1. Brutal force?\n2. Sorting?\n3. Hashset?\nChoose the number: "))

    if algorithm == 1:
        containsDuplicateBrutalForce(nums)
    elif  algorithm == 2:
        containsDuplicateSorting(nums)
    elif  algorithm == 3:
        containsDuplicateHashSet(nums)
    else:
        print("Valid input. Choose one more time.")


