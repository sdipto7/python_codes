# Suppose you have two arrays: Arr1 and Arr2. [7 Marks]
# Arr1 will be sorted values. For each element v in Arr2, you need to write a pseudo code that will
# print the number of elements in Arr1 that is less than or equal to v.
# For example: suppose you are given two arrays of size 5 and 3 respectively.
# 5 3 [size of the arrays]
# Arr1 = 1 3 5 7 9
# Arr2 = 6 4 8
# The output should be 3 2 4
# Explanation: Firstly, you should search how many numbers are there in Arr1 which are
# less than 6. There are 1, 3, 5 which are less than 6 (total 3 numbers). Therefore, the answer
# for 6 will be 3.
# After that, you will do the same thing for 4 and 8 and output the corresponding answers
# which are 2 and 4. Your searching method should not take more than O (log n) time

arr1 = [1,3,5,7,9]
arr2 = [6,4,8]
print([sum(1 for Arr1Num in arr1 if Arr1Num <= Arr2Num) for Arr2Num in arr2])