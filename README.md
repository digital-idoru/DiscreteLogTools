Discrete Logarithm Problem. 
=================

Python implementation of the some tools for solving instances of the discrete
log problem. The Pohlig-Hellman algorithm is best optimized for solving 
g^x = b mod p when p-1 has small prime factors. 

Babystep-Gianstep algorithm is better for p-1 with larger prime factors. 

Also included is a simply trial division + number sieve alorithm set for finding
factors as used in the functions. These functions are rather basic but are 
effect for small cases. 