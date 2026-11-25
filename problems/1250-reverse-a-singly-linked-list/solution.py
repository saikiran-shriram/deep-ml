def reverse_linked_list(values, method="iterative"):
    # values: list of node values in head-to-tail order
    # method: 'iterative' or 'recursive'
    # return: list of node values after reversal
    result = []
    stack = []
    for value in values :
        stack.append(value)
    while stack : 
        result.append(stack.pop())
    return result
    