"""Given a positive integer num, write a function which returns True if num is a perfect square else False."""

num = 16

def isPerfectSquare(num): #function to find the number is perfect square or not
        low = 0 #initialising the variable
        high = num #initialising the variable

        while low<=high: #looping until low and high are equal
            mid = (low + high)//2 #initialising mid variable
            if mid*mid == num: #checking if mid square is equal to the num
                return True #return true if yes
            elif mid*mid > num: #if mid square is greater than the num
                high = mid -1 #updating the high value
            else: #if mid square is less than the num
                low = mid+1 #updating the low value
        return False #returning false if all cases failed to find the number

solutions = isPerfectSquare(num)
print(solutions)