def minimax(state, is_max):
    if len(state.children()) == 0:
        return state.value()

    if is_max:
        max_value = float('-inf')
        for child in state.children():
            value = minimax(child, not is_max)
            max_value = max(max_value, value)
        return max_value
    else:
        min_value = float('inf')
        for child in state.children():
            value = minimax(child, not is_max)
            min_value = min(min_value, value)
        return min_value