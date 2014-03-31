# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 17:08:10 2014

@author: Daniel S. Hono II
"""
import math

def russianPeasant(x, y, z):
    s = 1;
    while(x > 0):
        if (x%2 == 1):
            s = (s*y) % z;        
        x = x//2;
        y = (y**2) % z;
            
    return s;
                        
def egcd(a, b):

    #Initial values 
    u1 =  1;
    v1 =  0;
    u2 =  0; 
    v2 =  1;

    while(b > 0):        
       #Find the remainder and the quotient
        r = a % b
        q = a // b       
        
        # set the values 
        a = b; 
        b = r;
        
        u1prime = u1
        v1prime = v1
        u2prime = u2
        v2prime = v2
        
        u1 = u2;
        v1 = v2;
        
        u2 =  (u1prime - (u2prime * q));
        v2 =  (v1prime - (v2prime * q));

    return u1, v1;

def computeM (p):
    m = math.ceil(math.sqrt(p-1));
    return m;

def babyList (g, p):
    X = dict(); #O(1) avg lookups according to python's website
    m = int(computeM(p));
    for i in range(0, m):
        X[g**i % p] = i; #fix this. Mult prev. elem by g. 
    return X;

def compareGiant (b, g, p):
    Y = babyList(g, p);
    m = int(computeM(p));
    (Inv, _) = egcd(g, p);
    Inv = Inv % p;
    a = russianPeasant(m, Inv, p);
    for i in range(0, m):       
        Z = b*(russianPeasant(i, a, p)) % p; #This can be made better as well. 
        if Z in Y:
            return i*m + Y[Z] 
    
def main():
    print "Enter g: ";
    g = int(raw_input());
    print "Enter b: ";
    b = int(raw_input());    
    print "Enter p: ";
    p = int(raw_input());
    K = compareGiant(b, g, p);
    print "A Solution to g^x = b mod p is x = " + str(K);

if __name__ == '__main__':
    main()