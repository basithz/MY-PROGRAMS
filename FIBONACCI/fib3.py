fibdict={1:0,2:1}
def fib(num):
    if num in fibdict:
        return fibdict[num]
    else:
        fibdict[num]=fib(num-1)+fib(num-2)
        return fibdict[num]

n=int(input('Enter a number : '))
print(fib(n))