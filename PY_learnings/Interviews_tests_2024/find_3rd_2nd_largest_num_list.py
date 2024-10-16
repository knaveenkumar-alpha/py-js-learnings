nums = [2, 3, 7, 4, 5, 6, 10, 11, 120]
# nums = [120, 2, 3, 7]
large_num = float('-inf')
second_large_num = float('-inf')
third_large_num = float('-inf')

for num in nums:
    if num > large_num:
        third_large_num = second_large_num
        second_large_num = large_num
        large_num = num
    elif num > second_large_num:
        third_large_num = second_large_num
        second_large_num = num
    elif num > third_large_num:
        third_large_num = num

print(f"Largest No: {large_num} Second No: {second_large_num} Third No: {third_large_num}")



