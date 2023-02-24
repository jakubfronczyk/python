def get_input(prompt):
    while True:
            user_input = input(prompt)
            if user_input.isdigit():
                print("Invalid input. Please enter a word")
            else:
                return user_input

def isAnagramHashMaps(s, t):
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    if countS == countT:
        print(f"'{s}' and '{t}' are anagrams")
    else:
        print(f"'{s}' and '{t}' are not anagrams")

while True:
    s = get_input("Please enter first word: ")
    t = get_input("Please enter second word: ")
    if len(s) != len(t):
        print(f"Length of '{s}' is not the same as '{t}', so words cannot be anagrams")
    else:
        algorithm = int(input("Which algorithm do you want to use:\n1. HashMaps?\n2. Sorting?\nChoose the number: "))
        if algorithm == 1:
            isAnagramHashMaps(s, t)
        else:
            print("Valid input. Choose one more time.")
    
    tryAgain = input("Do you want to try again ? (yes/no): ")
    if tryAgain == "no":
        break