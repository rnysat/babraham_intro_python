"""
Molarity Calculator 
• Write a script to calculate how much of a compound is needed to make a solution of a given molarity.  

You will need to create variables to store: 
o The molecular mass of the compound (in g/mol) 
o The volume of solution you want to create (in ml) 
o The desired concentration (molar M) 

• The formula will be: 
o Mass (g) = Concentration (mol/L) * Volume (L) * Formula Weight (g/mol) 

• Make the script print a summary of the input variables and the calculated value by passing all of these as separate arguments to your print function. 

Interactive Molarity Calculator 

• Make a modified version of your initial script in which the different values you need for the calculation are requested interactively using input statements. 
• Remember that the return value from input will be a string (str), which you can’t use in mathematical calculations.  
You will need to use float() to convert it to a numerical value. 
• So that the calculated value doesn’t get too specific use the round function to limit the precision to 2 decimal places when printing the result. 
"""

user_mol_mass = float(input("Enter the molecular mass of the compound that you wish to make a solution of in g/mol: "))
user_sol_vol = float(input("Enter the volume of the solution that you wish to make in ml: "))
user_sol_conc = float(input("Enter the concentration of the solution that you wish to make in M (mol/L): "))

def cal_comp_mass(molecular_mass:float, solution_volume:float, solution_concentration:float)->str:
    compound_mass = round(solution_concentration * (solution_volume/1000) * solution_concentration, 2)
    return f"""
    In order to create {solution_volume} ml of a solution with concentration {solution_concentration} M
    using a compound with molecular mass {molecular_mass} g/mol, it is necessary to use {compound_mass} g
    of the compound.
    """
calculator_response = cal_comp_mass(user_mol_mass, user_sol_vol, user_sol_conc)
print(calculator_response)