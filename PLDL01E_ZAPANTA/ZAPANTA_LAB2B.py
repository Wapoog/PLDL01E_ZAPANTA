# Initialize
Net_Income = 0
SSS_Contribution = 0
Philhealth_Contribution = 0
Gross_Income = 0
Total_Deduction = 0
Pagibig_Contribution = 100.00
# Input
Employee_Name = str(input("Enter Employee Name = "))
Department = str(input("Enter Department = "))
Rate_per_hour = float(input("Enter Rate per hour = "))
Number_of_working_hours_per_day = float(input("Enter Number of working hours per day = "))
Number_of_days_per_week = float(input("Enter Number of days per week = "))
Number_of_weeks_per_month = float(input("Enter Number of weeks per month = "))
# Compute
Gross_Income = (Number_of_working_hours_per_day*Number_of_days_per_week*Number_of_weeks_per_month*Rate_per_hour)
# Decision
if 20000 <= Gross_Income >= 0:
    SSS_Contribution = 125.75
    Philhealth_Contribution = 100.00
elif 50000 <= Gross_Income:
    SSS_Contribution = 2200
    Philhealth_Contribution = 1200
elif 75000 <= Gross_Income:
    SSS_Contribution = 4800
    Philhealth_Contribution = 6800
else:
    SSS_Contribution = 5800
    Philhealth_Contribution = 8800
# Compute
Total_Deduction = (SSS_Contribution + Pagibig_Contribution +
Philhealth_Contribution)
Net_Income = Gross_Income - Total_Deduction
# Display
print(f"Employee Name = {Employee_Name}")
print(f"Department = {Department}")
print(f"Total Deduction = {Total_Deduction}")
print(f"Gross Income = {Gross_Income}")
print(f"Net Income = {Net_Income}")

