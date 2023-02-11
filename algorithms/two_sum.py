#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSumBrutalForce(nums, target):
    for i in range(len(nums)):
        for j in range (i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return print(f"Sum up two number is equal your target: {nums[i]} + {nums[j]} = {target}")
            else:
                return print(f"There isn't two numbers that sum up to target {target}")

while True:
    nums = list(map(int, input("Enter the elements of the array, separated by spaces: ").strip().split()))
    target = int(input("Enter the target to check if there are two numbers in array sum up to target: "))
    algorithm = int(input("Which algorithm do you want to use:\n1. Brutal force?\n2. One-pass hashmap?\nChoose the number: "))

    if algorithm == 1:
        twoSumBrutalForce(nums, target)
    else:
        print(f"Invalid input")

    tryAgain = input("Do you want to try again ? (yes/no): ")
    if tryAgain == "no":
            break