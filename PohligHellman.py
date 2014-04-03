# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 17:08:10 2014

@author: Daniel S. Hono II
"""

import math
import TrialDivisionFactor
import time

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

def parseFactors(F): 
    X = [];    
    while(F != []):
        X.append( (F[0], F.count(F[0])) ); #(p_i, n_i)
        F = F[F.count(F[0]):len(F)];
    return X;

def pohligHellman(P, g, b, n):
    A = []; #[Z_1, ..,Z_k]
    u = 0;
    (gInv, _) = egcd(g, n);
    gInv = gInv % n;
    c = n-1;
    r = b; 
    for i in range(0, len(P)): #for each prime
        x = russianPeasant((c/(P[i][0])), g, n);
        for j in range(0, (P[i][1])): #for each degree                                  
            y = russianPeasant((c/((P[i][0])**(j+1))), b, n);
            for k in range(0, (P[i][0])): #find the base P[i] digit
                if pow(x, k, n) == y:
                    u += k*(P[i][0]**j);
                    break;           
            b = (b * russianPeasant((P[i][0]**j)*k, gInv, n)) % n;
        A.append(u);
        u = 0;
        b = r;                 
    return A; 

def Combine(X, P):
   x = 0;
   N = 1;
   Y = [];
   for k in range(0, len(P)):
       Y.append(P[k][0]**P[k][1]);
   for j in range(0, len(Y)):
       N *= Y[j];
   for i in range(0, len(Y)):
       (s, _) = egcd(int(N/Y[i]), Y[i]);    
       e = s*(int(N/Y[i])); 
       x += X[i]*e; 
   return x; 
    
def main():
    start_time = time.time();
    F = [];
    print "Enter g: ";
    g = int(raw_input());
    print "Enter b: ";
    b = int(raw_input());    
    print "Enter p: ";
    p = int(raw_input()); 
    TrialDivisionFactor.factor(p-1, F, 0); 
    F = parseFactors(F);
    Z = pohligHellman(F, g, b, p);
    x = Combine(Z, F);
    print "A Solution to g^x = b mod p is x = " + str(x);
    print "Verifying solution.....";
    if pow(g, x, p) == b:
        print "Verified!";
    else:
        print "Something went wrong!";        
    print time.time() - start_time, "seconds" 

if __name__ == '__main__':
    main()