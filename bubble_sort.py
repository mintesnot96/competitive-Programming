import sys
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
def countSwaps(a: list[int])->list[int]:
    n=a
    s=0
    unsortedIndex=len(n)-1
    for j in range(0,unsortedIndex):
        for i in range(0, unsortedIndex):
            if n[i] > n[i + 1]:
                s=s+1
                n[i] , n[i + 1]= n[i + 1],n[i]
        unsortedIndex=unsortedIndex-1
    return print('Array is sorted in',s,'swaps.'),print('First Element:',n[0]),print(f'Last Element: {n[len(n)-1]}')
# print(countSwaps([6,4,1]))
