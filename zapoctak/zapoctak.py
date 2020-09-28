#here will be the code for zapoctak.py
from itertools import count
from math import gcd
import random
import time
#number = 10403
#number = 43142398922
seed = 1
listfactorsfinal = []


#Miller Rabin primality test
def Miller_Rabin(d, n):
    a = 2 + random.randint(1, n - 4)
    res = 1

    a = a % n
    while (d > 0):

        if (d & 1):
            res = (res * a) % n
        d = d >> 1
        a = (a * a) % n

    if (res == 1 or res == n - 1):
        return True

    while (d != n - 1):
        res = (res * res) % n
        d *= 2

        if (res == 1):
            return False
        if (res == n - 1):
            return True
    return False
#Function to test the primality of number using Miller-Rabin test for complex numbers and few basic conditions to speed the test for small numbers.
def is_prime(n):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    # because M-R is probabilistic method, we are controlling accuracy by increasing or decreasing number of repetitions.
    for i in range(10):
        if (Miller_Rabin(d, n) == False):
            return False
    return True


#function used in Floyd cycle detection
def func(c, number):
    return (c * c + seed) % number

#Pollard rho function with Floyd cycle detection
def PollarRho(number,x):
    #x = 2
    notend = 1
    listfactors = []
    while notend == 1:
        #hladame divisor numberu
        for cycle in count(1):
            y = x
            for i in range(2 ** cycle):
                x = func(x,number)
                factor = gcd(x - y, number)
                if factor > 1:
                    listfactors.append(factor)
                    if (number/factor > 1):
                        number = int(number/factor)
                    else:
                        #print(listfactors)
                        return listfactors

#function to check if the numbers subnmitted by user are integer
def integerCheck(nmbr):
    try:
        val = int(nmbr)
        return val
    except:
        nmbr2 = input("You did not write integer, please submit integer value")
        try:
            val = int(nmbr2)
            return val
        except:
            print("You did not write integer again, the program is shutting down, please re-run program if you want to use it ")
            quit()



#welcome message to the user, explanation of possible use
print("Hi,\nwelcome to the Large Numbers Prime Factorization program using Pollard Rho algorithm.\nIn this program you can see the "
      "behaviour of the algorithm under different circumstances.\nYou can change paramaters  used in of Floyd cycle detection algorithm "
      "to observe \nhow it can change the results which may not be correct everytime\n" )
start = True

#start of the main loop, it helps us to give the user possibility of using program multiple times, without rerunning whole code
while start == True:
    #entering the number to factorize
    numberi = (input("Please, enter number you want to factorize"))
    #checking if the input is integer
    numberi = integerCheck(numberi)
    rand = input("Would you like to set variables of function used in Floyd cycle detection algorithm? If Yes please answer with Y.\n"
          "For random variables, please push any alphanumerical key."
          " To end program press E ")
    #checking the answer, if asnwer is "Y" then we proceed to ask for variables input
    if rand == "Y":
        seed = (input("Please select the c (smaller than number we are going to factorize) in function f(x) = x^2 + c used in cycle detection algorithm."))
        # checking if the input is integer
        seed = integerCheck(seed)
        xinit = (input("Please select the x (smaller than number we are going to factorize) in function f(x) = x^2 + c used in cycle detection algorithm"))
        # checking if the input is integer
        xinit = integerCheck(xinit)
    #if answer is E we randomize the variables
    elif rand != "E":
        seed = random.randint(1, numberi-1)
        xinit = random.randint(1, numberi - 1)
        print ("Here are the results for randomized variables used in cycle detection algorithm\n\n")
    # if answer is differetn from E and Y we quit the program
    else:
        print("Thank you for using our program!")
        quit ()
    timelimit = 10
    timelimit = input("Please set the time limit in seconds(integer value) for the execution of the factorization after which the program will shut down.\n"
                      "If you do not want to have timelimit, please submit 0 ")
    timelimit = integerCheck(timelimit)
    print("\n\n")
    #Basic printing of variables and factorized number
    print ("Factorized number: ", numberi)
    print ("Seed: ", seed)
    print ("Function variable: ", xinit )
    print ("Time limit: ", timelimit)
    #checking the timelimit condition
    if abs(timelimit) > 0:
        starttime = time.time()
        #call of pollard factorization
        lst = PollarRho(numberi,xinit)
        if time.time() >= starttime + abs(timelimit):
            print("It takes more than your timelimit to factorize this number. The programs is closing now")
            quit()
    else:
        #call of pollard factorization
        lst = PollarRho(numberi, xinit)
    print("Possible prime factorization: " +  " ".join(str(z) for z in lst) )

    check = 1
    fail = 0
    for l in lst:
        if is_prime(l) == False:
            print("Algorithm probably failed")
            fail += 1
        check = check*l
    print ("We multiply all the factors to see if the algorithm factorized our number fully\n"
           "The result is: " + "*".join(str(z) for z in lst) + " =",check)
    #check if multiplication of factors are giving us original number
    if check == numberi :
        if fail != 0:
            print("Multiplication of factors equals original number however the algorithm failed because not all the found factors are primes")
        else:
            print("Multiplication of all prime factors equals original numberm the algorithm worked")
    #possibility to rerun the program
    restart = input("Would you like to try again? For YES type Y, to end tap on any other alphanumerical key.")
    if restart == 'Y':
        start = True
    else:
        print("Thank you! Hope you had fun!")
        start = False




