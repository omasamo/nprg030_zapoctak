# PRIME FACTORIZATION FOR LARGE NUMBERS
This program will factorize large numbers into prime numbers using known algorithms to perform such work.

By the fundamental theorem of arithmetic, every positive integer has a unique prime factorization.

Given a general algorithm for integer factorization, any integer can be factored into its constituent prime
factors by repeated application of this algorithm. 

Donald Knuth. The Art of Computer Programming, Volume 2: Seminumerical Algorithms, Third Edition. Addison-Wesley, 1997. ISBN 0-201-89684-2. Section 4.5.4: Factoring into Primes, pp. 379–417.

# USAGE
Program will ask user the number for which he would like to see his prime roots.
User will give the number.
If the given number is prime, the program will notify user. Otherwise it will give the user all the prime roots

# IMPLEMENTATION
It will use J.M. Pollards's Rho Method, which is more efficient than the usual trivial solutions to this problem.
It works with the fact the using random numbers with some conditions is rather effective method of factorization.
Having method to test if the number is prime we would be able to quickly detect prime numbers.

# USER MANUAL
User can run this code in his command line/command prompt. Code should run independently of the OS of the computer.
User will be guided through whole program with explanation of each step. There will be multiple options possible for some steps. The options will be
explained directly to the user while running the program.
Program instruction will be displayed in the command line/command prompt environment.

Firstly, user will be asked to submit the number he would like to factorize.

Afterwards, user will be asked if he wants to set the variables in Floyd cycle detection function or he would like the program to initialize them randomly.

If he chose to set variables by himself, he will be then asked to submit his preferred values.

Also, sometimes the factorization can last for too long, therefore user will have the opportunity to set the timeout limit for the factorization.

After all these possibilities, the program will proceed to factorization with the settings given by user.

It will print, Factorized number, variables of the function used, Time limit and possible factors.

If the factors are not prime it will automatically detect it and will notify the user about that.

#WHY CAN THE ALGORTHM FAIL?

Sometimes with certaines values of variables, seeds and numbers to factorize we can observe that the code will fail. It can be quickly resolved by just factoring the not prime factors,
however we would like to show this to the user so that he can better understand that this algorithm is not 100% correct.

We invite the user to try it for himself:

Observe the difference in factorization of the nubmber 25852

with x = 2 and c = 1 the factorization will work however with x = 2 and c = -1 the factorization will fail, therefore as we can see, that it is also important to find proper variables of
cycle detection algorithm so that the whole Pollard Rho algorithm will work.

I hope you will have some fun!
