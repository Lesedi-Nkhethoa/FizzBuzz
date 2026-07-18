print("Welcome to the FizzBuzz!")

max_number = int(input("Enter a maximum number: ")) # Asks user to input a max number for the test. 

x = int(max_number + 1) # Includes the maximum number given by the user and converts the input into an integer.

for y in range(1, x): # Iterates the from 1 until the maximum number given by the user.
   
    if y%3 == 0 and y%5 == 0: # The 'and' operator makes sure both conditions must be met for the output to be FizzBuzz.
        print(f"{y} - FizzBuzz") 
    
    elif y%3 == 0: # Checks for Fizz only.
        print(f"{y} - Fizz") 
    
    elif y%5 == 0: # Checks for Buzz only.
        print(f"{y} - Buzz")
    
    else: # Numbers that do not meet any requirement are seen as false.
        print(f"{y}   ")

print(f"Done! Checked all {y} numbers")
    



 