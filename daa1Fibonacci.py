def fib(n):
    prev = 0
    next = 1
    stepc = 0
    for i in range(n):
        stepc += 1
        print(prev)
        temp = next
        next = prev + next
        prev = temp 
    print(f"step c = {stepc}")
fib(6)