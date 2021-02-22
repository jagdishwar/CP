A=2
stack = [A]
result = [[A]]
while stack:
    queue = []
    while stack:
        node = stack.pop()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(queue)
    stack = queue

return result


