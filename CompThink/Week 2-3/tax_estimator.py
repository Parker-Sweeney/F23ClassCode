# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:52:35 2023

@author: pswny
"""

# Asks user their annual income and if they are filing jointly
income = float(input("What is your annual income? "))
mfj = bool(input("If you are married filing jointly type True. Otherwise, hit enter "))

# If user is filing jointly, it asks the user what their partner's income is and adds it to theirs
if mfj == True :
    partner_income = float(input("What is your partner's annual income? "))
    income = float((partner_income) + (income))
    print("Combined Income is: ", income)

# If the user is not filing jointly, income stays the same
else: 
    partner_income = 0
    income = float(income + partner_income)

# max tax for mfj
max_tax_mfj_1 = 528.00
max_tax_mfj_2 = 2841.60
max_tax_mfj_3 = 7971.60

# max tax for singles
max_tax_single_1 = 264.00
max_tax_single_2 = 1420.80
max_tax_single_3 = 3985.80

if mfj == True:
    
    if income <= 12000: 
        state_tax = 0
        
    elif (income > 12000) and (income <= 60000):
        state_tax = max_tax_mfj_1 + (income - 12000)*0.0482
    
    elif (income > 60000) and (income <= 150000):
        state_tax = max_tax_mfj_2 + (income - 60000)*0.0570
        
    else:
        state_tax = max_tax_mfj_3 + (income - 150000)*0.0600

else: 
    
    if income <= 6000: 
        state_tax = 0
        
    elif (income > 6000) and (income <= 30000):
        state_tax = max_tax_single_1 + (income - 6000)*0.0482
    
    elif (income > 30000) and (income <= 75000):
        state_tax = max_tax_single_2 + (income - 30000)*0.0570
        
    else:
        state_tax = max_tax_single_3 + (income - 75000)*0.0600
    
# outputs state_tax value

print("Your state tax is", "$",round(state_tax,2))

