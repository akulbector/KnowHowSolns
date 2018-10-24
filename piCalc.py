import math

pi_1=4

for i in range(2,1000):
    
    int_denom = (i*2)-1
    
    if(i%2==0):
        pi_1-= (4/int_denom)
    else:
        pi_1 += (4/int_denom)
        
pi_2 = 4
j = 2

while(round(pi_2,2)!=3.14):
    
    int_denom = (j*2)-1

    if(j%2==0):
        pi_2 -= (4/int_denom)
    else:
        pi_2 += (4/int_denom)
    
    j = j+1
#This loop runs until pi becomes the rounded value even once
#The number fluctuates around pi, one above, one below
#What if we want to know when both the above and below
    #calculation are accurate to 2 decimal places
    
pi_3 = 4
pi_b4 = 0
k = 2
accurate = False

while(not accurate):
    
    int_denom = (k*2)-1
    pi_b4 = pi_3
    
    if(k%2==0):
        pi_3 -= (4/int_denom)
    else:
        pi_3 += (4/int_denom)
        
    k+=1
    if(round(pi_b4-3.14,2)==0.01 or round(pi_b4-3.14,2)==0.00):
       if(round(pi_3-3.14,2)==0.01 or round(pi_3-3.14,2)==0.00):
            accurate=True
    

print(k)
list = [1,2,3]
list.append(4)
for x in list:
    print(x**2)

    