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
   parent=[];
   j=0;
   while j<14:
            #this loop generate chromosome random and handle hard constraint
        rand=random.randrange(0,4,1);
        chromosome=[rand];
        i=1;
        while i<98:
            rand=random.randrange(0,4,1);
            if rand==1 and chromosome[i-1]==3:
                continue;
            else:
                chromosome.append(rand);
                i+=1; 
        parent.append(chromosome);
        j+=1
   return parent;    
#-----------------------------------------------------------------------------#
#this function print parent generate form intialization function
#-----------------------------------------------------------------------------#

def printParent(parent=0):
    if parent==0:
        print("the value null in parent plaese bass the parent to this function ")
        return 0
    j=0
    while j<len(parent):
        i=1
        n=0
        print("p",j)
        while i<=14:
            print(parent[j][n:i*7])
            i+=1
            n+=7
        j+=1

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
    printParent(intial);

    