#Exercise 3: Iteration and Conditions: Iteration and Looping: Variant Counting

"""You are running an experiment looking for a series of protein variants, 
specifically E23A, P12S, W88Y and R32N Write a script which repeatedly 
prompts you to enter a variant name and keep count of the number of times 
the ones in the list come up.  

If you get a variant which isn’t in the list then print out a warning and 
move on. If they enter a blank variant then stop asking for more input and 
print out the counts of the variants you saw. 

To do this: 
• Create a dictionary with the variant names as keys and an integer 
(initially 0) as values 
• Start an infinite loop with while True:
• Ask for the name of the variant in an input statement. 
• If nothing was entered then break to exit the loop 
• Look up the variant in the dictionary and increase the value 
by using += 1 
• Print out the dictionary after you exit the loop. 
 """

prot_var = "E23A P12S W88Y R32N".split()

prot_dict = {k:0 for k in prot_var}

while True:
    user_var = input("Enter the variant name of a protein: ").upper()
    if user_var == "":
        break
    try:
        prot_dict[user_var] += 1
    except KeyError:
        print("The protein variant that you entered is not one that this experiment if focussed on so will be disregarded.")


print(prot_dict)

