n, k = map(int, input().split())
arr = list(map(int, list(input())))
stack = [arr[0]]
for idx, num in enumerate(arr[1:]):
    if num <= stack[-1]:
        stack.append(num)
    else:
        while stack and k > 0:
            right = stack.pop()
            if right < num:
                k -= 1
            else:
                stack.append(right)
                break
        stack.append(num)
if k > 0:
    stack = stack[:- k]

print(''.join(map(str, stack)))
