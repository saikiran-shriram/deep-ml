def reverse_linked_list(values, method="iterative"):
    # values: list of node values in head-to-tail order
    # method: 'iterative' or 'recursive'
    # return: list of node values after reversal
    if not values:
        return []
    return [values[-1]] + reverse_linked_list(values[:-1])

    