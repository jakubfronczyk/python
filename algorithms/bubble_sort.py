def bubbleSort(numbers):
    for i in range(len(numbers)):
        for j in range (0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

test1 = [12,32,0,4,15,-2,1]
test2 = [125,-54,25,436,-640,1099,543.2]

bubbleSort(test1)
bubbleSort(test2)

print(f'Sorted Array using Bubble Sort algorithm\n {test1}')
print(f'Sorted Array using Bubble Sort algorithm\n {test2}')