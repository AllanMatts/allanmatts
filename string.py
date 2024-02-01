from datetime import date

# Get current date
current_date = date.today()

# Ask user for date of birth
birth_date = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert birth date string to date object
birth_date_obj = date.fromisoformat(birth_date)

# Calculate age in years
age = current_date.year - birth_date_obj.year

# Adjust for months and days if user's birthday hasn't passed yet
if current_date.month < birth_date_obj.month or (current_date.month == birth_date_obj.month and current_date.day < birth_date_obj.day):
    age -= 1

# Print age
print(f"Your age is {age} years old.")