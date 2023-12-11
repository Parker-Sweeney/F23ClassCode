# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:05:15 2023

@author: sween
"""

# Parker J Sweeney (01389288) Quiz Version D

contribPer = .05

unicontrib = contribPer * 2

salinc = .03

retplnrtn = .08

emp_curcontrib = 0
iowa_contrib = 0
invest_bal = 0
totalcontrib = 0
past_empcontrib = 0
emp = 0

years = int(input("Years at Iowa: "))
starting_sal = float(input("Starting Salary: "))

print(years, "years planned starting at", starting_sal)

cur_years = 0
cur_sal = starting_sal

while cur_years != years: 
    if cur_years >= 5:
        cur_sal = cur_sal + 5000
        salinc = 0
    cur_years += 1
    invest_bal = invest_bal * (1 + retplnrtn)
    emp = (cur_sal * contribPer) + emp
    iowa_contrib = (cur_sal * (1+unicontrib)) + iowa_contrib
    invest_bal = invest_bal + (emp_curcontrib + iowa_contrib)
    cur_sal = cur_sal * (1+salinc)
    print(cur_years, cur_sal, iowa_contrib, invest_bal, emp)
print("Current salary: $%0.2f" %float(cur_sal), " Your Contribution: $%0.2f", %float(emp), "Iowa's contrib: $%0.2f", %float(iowa_contrib), )
