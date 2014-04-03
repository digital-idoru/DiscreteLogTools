Discrete Logarithm Problem. 
=================

Python implementation of the some tools for solving instances of the discrete
log problem. The Pohlig-Hellman algorithm is best optimized for solving 
g^x = b mod p when p-1 has small prime factors. 

Babystep-Gianstep algorithm is better for p-1 with larger prime factors. 

Also included is a simply trial division + number sieve alorithm set for finding
factors as used in the functions. These functions are rather basic but are 
effect for small cases. 

The infeasability of computing hard discrete log problems is what gives certain
cryptosystems their security, for example, the ElGamal crypto system. These 
algorithms are designed as attacks again these systems, thus demonstrating
that great care must be used when setting up such cryptopsystems, i.e, "strong"
prime numbers must be used that resist these attacks.

The Pohlig-Hellman algorithm implemented here is very fast against primes that
are vunuralbe to such an attack, i.e. primes P such that P-1 has smooth factors.