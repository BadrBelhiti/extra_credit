import os
import sys
import copy

def gcd(a, b):
    if (a == 0): 
        return b 
    return gcd(b % a, a)

def gcd_list(n):
    n = copy.deepcopy(n)
    while len(n) > 1:
        n.append(gcd(n.pop(), n.pop()))
    
    return n.pop()

def generate_lists(original, acc, curr):
    if len(curr) == len(original):
        acc.append(curr)
    else:
        dim = len(curr)
        for i in range(original[dim]):
            new_list = copy.deepcopy(curr)
            new_list.append(i + 1)
            generate_lists(original, acc, new_list)
    
def solve(n):
    gcds = []
    lists = list()
    generate_lists(n, lists, list())
    
    for i in range(len(lists)):
        gcds.append(gcd_list(lists[i]))
        
    return sum(gcds) % 1000000007
