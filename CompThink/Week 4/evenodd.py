count = 0
even_numbers = 0
odd_numbers = 0

while count < 5:
    value = int(input("Enter a whole number: "))
    if value % 2 == 0:
        even_numbers = even_numbers + 1
    else:
        odd_numbers = odd_numbers + 1
    count = count + 1
    
print("You entered", even_numbers, "even numbers and", 
      odd_numbers, "odd numbers.")
