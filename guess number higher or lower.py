"""We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked."""

def guessNumber(n): 
        low = 1 #initialising the variable
        high = n #initialising the variable
        while low<=high: #looping until low is equal to high
            mid = (low + high)//2  #initialising the variable
            pick = guess(mid) #using guess function to return if number is correct or not
            if pick == -1: # if number is higher than mid num
                high = mid -1
            elif pick == 1: # if number is lesser than mid num
                low = mid + 1
            else:
                return mid #if number is equal to the picked number
    