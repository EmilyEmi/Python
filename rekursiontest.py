#Summe von 1,2,3....
#def sum(x):z.B. x=3,dann sum(x) = 1+2+3, wenn x = 10, dann sum(10)= 1+2+3+4+5+6+7+8+9+10

#sum(x) = x + sum(x-1),das heißt sum(10)= 10 +sum(9),sum(1)=1
"""""
def sum(x):
    if x == 1:
        return 1
    elif x> 1 :
        return x + sum(x-1)
    else :
        raise ArithmeticError("Error")


#print(sum(0))

def falc(x):
    x1 = 5
    assert(falc(x1) == 15)
    x2 = 10
    assert(falc(x2) == 55)
    x3 = 0
    assert(ArithmeticError, sum(x3))

print(falc)
"""""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci)

fibonacci(6)


def testfibo():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13

"""""
def sumwithfor(x):
    result = 0
    for x in range(0,x+1):
        result = result + x


      return result

def testsum():
    assert sum(10) == sumwithfor(10)
    assert sum(20) == sumwithfor(20)
"""""