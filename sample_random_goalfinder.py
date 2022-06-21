import random
import sys
sys.setrecursionlimit(10000)
randomizer = [1,2]
ls=[10,10,20,40,50,10]
n=len(ls)
answer = 20

def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c


def goal_state(res,answer):
    if res == answer:
        return True
    else:
        return False

def choose_something():
    choice = random.choice(randomizer)
    print(choice)
    return choice


def do_operations(ls):
    res=0
    operations=[]
    for i in range(0,n):
        choice = choose_something()
        if choice == 1:
            res=add(res,ls[i])
            operations.append("+")
        if choice == 2:
            res=sub(res,ls[i])
            operations.append("-")
    print("REsult: ",res)
    return res, operations



def find_solutions(list,answer):
    res,operations=do_operations(list)
    if goal_state(res,answer):
        print("solution found doing following operations:",operations)
    else:
        find_solutions(list,answer)

find_solutions(ls,answer)
