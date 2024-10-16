def run_length_input_string(inp_str):
    if not inp_str:
        return ""
    inp_str = "".join([aph for aph in inp_str if aph.isalpha()])
    count = 1
    res = ""
    for idx in range(1, len(inp_str)):
        if inp_str[idx] == inp_str[idx - 1]:
            count += 1
        else:
            res += inp_str[idx-1] + str(count)
            count = 1
    res += inp_str[-1] + str(count)
    return res


# s = '  AB  AB a a b @4bbk'
s = ' AB ABB a a b @456 bk '
# st = s.replace(' ', '')
res = run_length_input_string(s)
print(res)