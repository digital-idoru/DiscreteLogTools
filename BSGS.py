# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:36:45 2014

@author: performanceof100
"""
import math

def russianPeasant(x, y, z):
    s = 1;
    while(x > 0):
        if (x%2 == 1):
            s = (s*y) % z;        
        x = x//2;
        y = (y*y) % z;            
    return int(s);

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
        #unpleasant...
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
    #S = [];
    m = int(computeM(p)); 
    b = list(xrange(m));
    print "Building the babystep list with m = " + str(m);     
    #S = (map((lambda x: russianPeasant(x, g, p)), b)); pow() is better   
    S = map((lambda x: pow(g, x, p)), b); #create list of powers
    X = dict(zip(S, b)); #zip list of powers and positions into a dictionary
    return X;

def compareGiant (b, g, p):
    if b == 1:
        return 0;
    Y = babyList(g, p);
    m = int(computeM(p));
    (Inv, _) = egcd(g, p);
    Inv = Inv % p;
    a = russianPeasant(m, Inv, p);
    Z = b; # i = 0 " 
    for i in xrange(1, m):       
        #Z = b*(russianPeasant(i, a, p)) % p; #This can be made better as well.
        Z = (Z * a) % p; #Is this a better way? 
        if Z in Y:
            return i*m + Y[Z]; 
