def reverse_arr(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right],  arr[left]
        left += 1
        right -= 1
    return arr


nums = [1,3,5,7,9]
print(reverse_arr(nums))
nums = []
print(reverse_arr(nums))


def isValid(s: str) -> bool:
    dt = {")":"(", "]":"[", "}":"{"}
    s = "(){}}{"
    stack = [char for char in s if char not in dt.keys()]
    print(stack)
    flag = False
    if len(s) < 2:
        return flag
    for i in s:
        if i in dt.keys():
            char = stack.pop()
            if char == dt.get(i):
                flag = True
                continue
    return flag

print(isValid("st"))
