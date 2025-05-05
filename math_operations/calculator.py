def add(*args):
    num = sum(args)
    return num

def subtract(*args):
    num = args[0]
    for i in range(1,len(args)):
        num = num - args[i]
    return num


def multiply(*args):
    num = 1
    for i in args:
        num = num * i
    return num

def divide(*args):
    num = args[0]
    for i in range(1,len(args)):
        num = num / args[i]
    return num



if __name__ == '__main__':
    a = multiply(2,3,4)
    print(a)
    
