def romanToInt(s: str) -> int:
    num_dict = {"I": 1, "V": 5, "X":10, "L": 50, "C":100, "D":500, "M":1000}
    res = 0
    for idx,char in enumerate(s):
        if char in num_dict:
            res += num_dict.get(char)
            if idx != 0 and len(s)-1 < idx and s[idx] < s[idx+1]:
                print(s[idx], s[idx-1])
                res -= num_dict.get(char)
    return res

print(romanToInt("LVIII"))

s = "LVIII"
print([i for i in s])
st = [i for i in s]
ls = []
# for _ in range(len(s)//2+1):
#     char = ""
#     try:
#         for j in range(2):
#             char += st[j]
#         ls.append(char)
#         char = ""
#     except IndexError as err:
#         ls.append(char)
#     st = st[2:]
# print(ls)
s = "MCMXCIV"
# st = [s[i:i+2] for i in range(0, len(s), 2)]
num_dict = {"I": 1, "V": 5, "X":10, "L": 50, "C":100, "D":500, "M":1000}
res = 0
print(s[::-1])
st = [s[i:i+2] for i in range(0, len(s), 2)]
print(st)
st = ["M", "CM", "XC", "IV"]
# st = [""]
for chars in st:
    char = list(chars)
    if len(char) > 2:
        if char[0] > char[1]:
            res += (num_dict.get(char[0]) + num_dict.get(char[1]))
        else:
            res += (num_dict.get(char[1]) - num_dict.get(char[0]))
print(res)