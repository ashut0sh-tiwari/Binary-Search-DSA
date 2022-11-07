"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""

l1 = [1,2,3,0,5,6,7]

#function to find the missing value in the list
def listSum(list):
    #initialising the variable
    res = len(list)
    for i in range(len(list)):
        print('-')
        print(list[i])
        print('-')
        #adding the length of the list and minimise list index value with every iteration 
        res += (i-list[i])
        print('-')
        print(res)
        print('-')

solution = listSum(l1)
print(solution)