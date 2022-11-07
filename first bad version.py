"""You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API."""



def firstBadVersion(self, n: int) -> int:

    #initialising the variables
    low=1
    high = n
    #looping the list
    while low<high:
        mid = (low+high)//2 #initialising mid value
        if isBadVersion(mid):#running the given API function to check whether mid value product is bad or not and if it is bad then updating the high variable and running the loop again because we dont know whether its the first bad version or not 
            high = mid
        else: # else updating the low variable
            low = mid+1
    return low #returning high or low as both represent the same value in final outcome