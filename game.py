import random
def computer(high,low,count,randnum):
    if high >= low:
        guess = low + (high-low) // 2
        if guess == randnum:
            return count
        elif guess < randnum:
            count = count + 1
            return(computer(high,guess+1,count,randnum))
        else:
            count = count + 1
            return(computer(guess-1,low,count,randnum))
    else:
        return -1
 
randnum = random.randint(0,101)
count = 0
guess = -99

while(guess!=randnum):
    guess = int(input("Enter the number between 1 to 100:"))
    if guess < randnum:
        print("higher")
        count = count + 1
    elif guess > randnum:
        print("lower")
        count = count + 1
    else:
        print("you guessed it!")
        break

print("you took " + str(count) + " number of steps")
print("computer took " + str(computer(100,0,0,randnum)) + " number of steps")