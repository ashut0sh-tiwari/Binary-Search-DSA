"""You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build."""

n = 8
s = 10
#binary search solution with O(logn)
def arrangeCoins1(n):
        l = 1 #initialising the variable
        r = n #initialising the variable
        res = 0 #initialising the variable
        while l<=r: #iterating until l != r
            mid = (l+r)//2 #initialising mid variable
            coins = (mid/2)*(mid+1) #gauss formula to find sum of all value till mid
            if coins == n: #if sum is equal to the given n then return mid
                return mid
            elif coins > n: #if sum is greater than the given n then return update the r variable
                r = mid-1
            else: #if sum is less than the given n then return update the l variable
                l = mid+1
                res = max(mid,res) #storing the max value of coins in res
        return res #return res

#linear solution with O(n)
def arrangeCoins2(n):
        stairs = 0 #initialising the variable
        coins = 1 #initialising the variable
        i = 1 #initialising the variable
        while coins<=n: #iterating until coins != n
            stairs += 1 #updating the variable
            i += 1 #updating the variable
            coins += i #updating the variable
        return stairs #return res

solution1 = arrangeCoins1(n)
solution2 = arrangeCoins2(s)
print(solution1)
print(solution2)
