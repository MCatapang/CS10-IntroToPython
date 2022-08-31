# Unpacking
def func_unpacking():
    fruits = ("apple", "banana", "mango", "cherry")
    x, *y, z= fruits
    print(fruits, x, y, z)
# func_unpacking()




# Lambda
def func_lambda(): 
    l = [2,4,7,3,14,19]
    for i in l:
        checkOdd = lambda x : "True" if x%2 == 1 else "False"
        print(checkOdd(i))
# func_lambda()




# Global Variables
def func_global():
    x = "awesome"

    # def inner1():
    #     x = "fantastic" # value isn't reassigned
    #     print(x)
    # inner1()
    # print(x)

    def inner2():
        global x
        x = "fantastic"
        print(x)
    inner2()
    print(x)
# func_global()




# Loops
def func_forloop():
    primes = [2,3,5,7]
    # for i in primes:
    #     print(i)
    #     print("----")
    for j in range(8):
        print(j)
        print("----")
    # for k in range(1,8):
    #     print(k)
    #     print("----")
    # for m in range(1,8,2):
    #     print(m)
    #     print("----")
func_forloop()

def func_whileloop():
    count = 1
    while count <= 5:
        print(count)
        count += 1 ## `++` is not available in Python
func_whileloop()