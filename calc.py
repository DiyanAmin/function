def calc(n1,n2):
    if wish=='add':
        return n1+n2
    elif wish=='subtract':
        return n1-n2
    elif wish=='division':
        return n1/n2
    elif wish=='multiplication':
        return n1*n2
    else:
        print('Choice not avaible')
wish=str(input('Enter program: '))
n1=int(input('Enter number 1: '))
n2=int(input('Enter number 2: '))
print('Answer is:\n',calc(n1,n2))
