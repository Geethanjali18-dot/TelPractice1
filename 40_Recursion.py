import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print("Hello",i)
    greet()

greet()