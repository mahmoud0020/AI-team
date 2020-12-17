# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:12:48 2020

@author: mahmoud0020
"""
import random 


#HARD constraint:
    #nerse work at most one shift in day 
    #A nurse does not do a late-night shift followed by a day shift the next day.

#Soft constraint:
    #each nerse has qualification 
    #each nerse work minimum and maximum numbers of shifts assigned to a given nurse in a given week, of hours worked per week, of days worked
    #consecutively
#-----------------------------------------------------------------------------#
#FUNCTION-1 intialization function
#-----------------------------------------------------------------------------#

def intialization():
    
        
        #this loop generate chromosome random and handle hard constraint
        rand=random.randrange(0,4,1);
        chromosome=[rand];
        i=1;
        while i<98:
            rand=random.randrange(1,4,1);
            if rand==1 and chromosome[i-1]==3:
                continue;
            else:
                chromosome.append(rand);
                i+=1; 
        #here i make every nerse have one holiday at most
        j=0;
        while j<14:
            rand=random.randrange(0,7,1);
            chromosome[j*7+rand]=0;
            j+=1
        
        temp=""
        temp1=""
        i=0
        while(i<98):
            temp=str(chromosome[i])
            temp1+=temp
            i+=1;
        return temp1;



#-----------------------------------------------------------------------------#
#this function is calculate fitness of chromosome
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
#this function is select based on fitness function 
#-----------------------------------------------------------------------------#



#-----------------------------------------------------------------------------#
#this function is make cross over based on uniform cross over
#-----------------------------------------------------------------------------#



#-----------------------------------------------------------------------------#
#this function is make mutation 
#-----------------------------------------------------------------------------#



#-----------------------------------------------------------------------------#
# main program run here
#-----------------------------------------------------------------------------#
if __name__ == "__main__":
    intial=intialization();
    

    
