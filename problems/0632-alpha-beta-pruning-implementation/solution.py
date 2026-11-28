def alpha_beta_pruning(tree, is_maximizing=True):
    """
    Perform alpha-beta pruning on a game tree.

    Args:
        tree: A nested list representing the game tree. Leaf nodes are numbers,
              internal nodes are lists of children.
        is_maximizing: Whether the root node is a maximizing player.

    Returns:
        A tuple (value, nodes_evaluated) where value is the optimal minimax
        value and nodes_evaluated is the number of leaf nodes examined.
    """
    alpha = -float('inf')
    beta = float('inf')
    def fun(node, alpha , beta , maximizing) :
        if isinstance(node, (int, float)):
            return node, 1

        if maximizing:
            best = float('-inf')
            count = 0
            for child in node:
                value, child_count = fun(child, alpha, beta, False)
                best = max(best, value)
                count += child_count
                alpha = max(alpha, best)
                if alpha >= beta:
                    break
            return best, count
        else :
            best = float('inf')
            count = 0
            for child in node :
                value , child_count = fun(child,alpha,beta,True)
                best = min(best,value)
                count += child_count
                beta = min(beta,best) 
                if alpha >= beta :
                    break
            return best,count

    return fun(tree, alpha, beta, is_maximizing)