# capturing user inputs
worker_name= input("\nEnter your name: ")
task_name = input("\nEnter your task: ")
hours_worked = int(input("\nPlease Enter the hours worked: "))
RATE = 30000

# computation
wage = hours_worked * RATE
meal_allowance = 0.05 * wage
gross_wage = meal_allowance + wage
tax= 0.05 * gross_wage
net_wage = gross_wage - tax

# output statement to output all the computed values
print(f"\nName\n: {worker_name} \nWage\n: {wage} \nMeal allowance\n: {meal_allowance} \nGross wage\n: {gross_wage} \nTax\n: {tax} \nNet wage\n: {net_wage}\n")




