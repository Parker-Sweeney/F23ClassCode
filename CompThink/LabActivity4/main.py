# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:26:01 2023

@author: Parker
"""

import utilities as ut

def main(): 
    
    print("\nHeart Attack Analysis:")
    
    print("\nThese are the factors related to heart attacks that are considered in this data: \n")
    ut.getEKG()
    
    print("\n\t1. Heart Attack Percentage is calculated based on all data to see if the data is skewed. \n")
    ut.getHeart()
    
    print("\n\t2. Gender Percent is used to distinguish between the heart attack rates in men and women. \n")
    ut.getGender()
    
    print("\n\t3. EKG is considered, as it detects heart problems that can forecast chance of future heart attacks. \n")
    ut.getEKG()
    
    print("\n\t4. Exercise is considered to see if likelihood of heart attack increases when physically acticve. \n")
    ut.getExercise()


if __name__ == "__main__":
    main()
