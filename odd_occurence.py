def odd_occurence(array):
    res=0
    for ele in array:
        res ^=ele
    return res
if __name__ == '__main__':
    array=list(map(int,input().split()))
    print(odd_occurence(array))
"""
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
NOTE: Your algorithm should have a linear runtime complexity.
"""