def MyMathShower(*args):
    Sum = 0.0
    Sub = 1.0
    for i in args:
        Sum = Sum + float(i)
        Sub = Sub * float(i)
    print(Sum,Sub,-Sum+2*args[0])
MyMathShower(10,4,1,1)

