def add_two_numbers(l1, l2):
    carry = 0
    result = [0] * len(l1)
    max_len = max(len(l1), len(l2))
    for i in range(max_len) :
        if i < len(l1):
            a = l1[i]
        else:
            a = 0
        if i < len(l2):
            b = l2[i]
        else:
            b = 0
        total = a + b + carry
        digit = total % 10
        carry = total // 10
        result[i] = digit
    if carry != 0 :
        result.append(carry)
    return result