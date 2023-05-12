
# Minimax Algorithm

```js
function minimax(position, depth, maximizingPlayer)
    if depth == O or game over in position
        return static evaluation of position
    
    if maximizingPlayer
        maxEval = -infinity
        for each child of position
            eval = minimax(child, depth - 1, false)
            maxEval = max (maxEval, eval)
        return maxEval
    else
        minEval = infinity
        for each child of position
            eval = minimax(child, depth- 1, true)
            minEval = min (minEval, eval)
        return minEval
```

--- 

# Implement in Code

--- 

# Capture time

```python
import time

start = time.time()

# code

end = time.time()
print(end - start)

```
---

```py
@cache
@time
```
