# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:30:43 2023

@author: sween
"""

'''fh = open('first_half_tackles.txt')
tackles = dict()
for line in fh: 
   names = line.split()
   for name in names:
       if name not in tackles:
           tackles[name] = 1
       else:
           tackles[name] += 1
           
print(tackles)
'''

def main():
    fh = open('Retail_Sales-3.csv')
    for line in fh:
        months = line.split(',')
        # Get month and year as key for better differentiation
        month = [months[0]+months[1]]
        health_rev = months[3]
    build_month_dict(fh)
    print('The month with the worst average revenue was', worst_month, 'with an average revenue of $%0.2f' %float(worst_avg))
    worst_revenue(fh)
    print(worst_month)
    print(worst_avg)
    
def build_month_dict():
    months = dict()
    for month in months:
        if month not in months:
            months[month, int(health_rev)]
    return months

def worst_revenue():
    worst_avg = 32000
    worst_month = ''
    for month in months:
        
    
    print(worst_month)
    print(worst_avg)
    return worst_avg, worst_month
if __name__ == "__main__":
    main()
