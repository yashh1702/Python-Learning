x = 99
def f1():
    x = 88
    def f2():
        print(x) 
    return f2
myResult = f1()
myResult()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

# isme actual functionh return hoga jisme num=2 remember hoga mtlb (return x ** 2) hoga
square = chaicoder(2) 

# isme hume square ko call karege jisse actual function execute hoga mtlb isme hum x ki value dege aur vo square print kr degi

actualSquare = square(2)
print(actualSquare)