# Bad Code
salesAmt = 1100
if salesAmt >= 1000 :
    commissionRate = .08
    
if salesAmt >= 500 :
    commissionRate = .06
    
if salesAmt < 499 :
    commissionRate = .05
print(commissionRate)
# The result of this is commissionRate = .06 due to running the first if first,
# setting the commissionRate = .08, but then it runs the second if function
# and changes the commissionRate to .06
# Bottom Line: Pay attention to the order that if statements are in if 
# structured like this example
# should use elif as well to fix this

#Fixed Code
salesAmt = 1100
if salesAmt >= 1000 :
    commissionRate = .08
elif salesAmt >= 500 :
    commissionRate = .06
else :
    commissionRate = .05
