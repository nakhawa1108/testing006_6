factorial = 1
a=int(input('enter the no-'))
if a<0:
    print('factorial is not possible.')
elif a==0:
    print('factorial is 1.')
else:

    for i in range(1,a+1):
        factorial=factorial*i
print('fact=',factorial)