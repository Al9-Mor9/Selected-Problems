import math
import sys
sys.setrecursionlimit(10000)

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(isbintree(num))
    return answer

def isbintree(n):
    nb = format(n, 'b')
    nl = len(nb)
    tree_width = 2 ** (int(math.log2(nl)) + 1) - 1
    
    if nl!= tree_width: 
        nb = "0" * (tree_width - nl) + nb
    ans = 1 if check(0, tree_width-1, nb) else 0
    return ans

def check(s, e, str1):
    if s == e: return str1[s]
    mid = (s + e) // 2

    left = check(s, mid - 1, str1)
    right = check(mid + 1, e, str1)
    
    if not left or not right: return False
    if str1[mid] == "0" and (left == "1" or right == "1"): return False 
    return str1[mid]
