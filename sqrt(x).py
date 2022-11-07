"""Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned."""





#function to get the square root of a number by using binary search method which takes a number as an arguement
def mysqrt(x):
    #initialising the variables
    low = 0
    high = x
    ans = 0
    #using while loop until low is equal to high
    while low<=high:
        #initialising mid variable
        mid = (low+high)//2
        print(low)
        print(high)
        print(mid)
        #if mid square is equal to target value
        if mid*mid == x:
            return mid
        #if mid square is less than target value then updating the ans value with that mid value
        elif mid*mid<x:
            ans = mid
            low = mid+1
            print(low)
            print(high)
            print(mid)
            print(ans)
        #if mid square is greater than target value
        else:
            high = mid-1
            print(low)
            print(high)
            print(mid)
    return ans

solution = mysqrt(36)
print(solution)

