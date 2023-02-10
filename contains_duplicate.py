# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def containsDuplicate(nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


nums = list(map(int, input("Enter the elements of the array, separated by spaces: ").strip().split()))
result = containsDuplicate(nums)
if result:
    print("The array contains duplicates.")
else:
    print("The array does not contain duplicates.")


