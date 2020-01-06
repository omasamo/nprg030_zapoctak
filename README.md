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
