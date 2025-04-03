from datetime import datetime
from dateutil.relativedelta import relativedelta

def age_calculator(dob_str) :
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        today = datetime.today().date()

        if dob > today:
            return "Error: Date of birth cannot be in the future!"

        age_difference = relativedelta(today, dob)
        return (f"Age: {age_difference.years} years\n"
                f"{age_difference.months} months\n"
                f"{age_difference.days} days\n")

    except ValueError:
        return "Error: Invalid date format. Please enter the date as YYYY-MM-DD."

dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
print(age_calculator(dob_input))