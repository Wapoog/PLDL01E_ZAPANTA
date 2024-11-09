# Initialize
Pagibig_Contribution = 100.00
Philhealth_Contribution = 0
Withholding_Tax = 0

# Input employee's name, code , and department
Company_Name = str(input("Enter Company Name: = "))
Department = str(input("Enter Department: = "))
Employee_Code = str(input("Enter Employee Code: = "))
Employee_Name = str(input("Enter Employee Name: = "))
Salary_Date_Cutoff = str(input("Salary Date Cutoff: = "))

# Input rate per hour, working hours per day, days per week, and weeks per month
Rate_per_hour = float(input("Enter Rate per hour: = "))
Hours_per_payday = float(input("Enter Number of Hours per payday: = "))
Hours_overtime = float(input("Enter Number of Hours overtime: = "))
Honorarium = float(input("Enter the Amount of honorarium: = "))

# Input number of hours of absent and tardy
Hours_of_absent = float(input("Enter the Number of Hours Absent: = "))
Hours_tardy = float(input("Enter the number of Hours Tardy: = "))

# Basic Pay and Overtime Pay
Basic_pay = Rate_per_hour * Hours_per_payday
Overtime_pay = Rate_per_hour * Hours_overtime

# Compute Gross Earnings
Gross_Earnings = Basic_pay + Overtime_pay + Honorarium

# Determine SSS Contribution
if Gross_Earnings <= 4249.99:
    sss_contribution = 180.00
elif 4250 <= Gross_Earnings <=4749.99:
    sss_contribution = 202.50
elif 4750 <= Gross_Earnings <= 5249.99:
    sss_contribution = 225.00
elif 5250 <= Gross_Earnings <=5749.99:
    sss_contribution = 247.50
elif 5750 <= Gross_Earnings <= 6249.99:
    sss_contribution = 270.00
elif 6250 <= Gross_Earnings <= 6249.99:
    sss_contribution = 292.50
elif 6750 <= Gross_Earnings <= 7249.99:
    sss_contribution = 315.00
elif 7250 <= Gross_Earnings <= 7749.99:
    sss_contribution = 337.50
elif 7750 <= Gross_Earnings <= 8249.99:
    sss_contribution = 360.00
elif 8250 <= Gross_Earnings <= 8749.99:
    sss_contribution = 382.50
elif 8750 <= Gross_Earnings <= 9249.99:
    sss_contribution = 405.00
elif 9250 <= Gross_Earnings <= 9749.99:
    sss_contribution = 427.50
elif 9750 <= Gross_Earnings <= 10249.99:
    sss_contribution = 450.00
elif 10250 <= Gross_Earnings <= 10749.99:
    sss_contribution = 472.50
elif 10750 <= Gross_Earnings <= 11249.99:
    sss_contribution = 495.00
elif 11250 <= Gross_Earnings <= 11749.99:
    sss_contribution = 517.50
elif 11750 <= Gross_Earnings <= 12249.99:
    sss_contribution = 540.00
elif 12250 <= Gross_Earnings <= 12749.99:
    sss_contribution = 562.50
elif 12750 <= Gross_Earnings <= 13249.99:
    sss_contribution = 585.00
elif 13250 <= Gross_Earnings <= 13749.99:
    sss_contribution = 607.50
elif 13750 <= Gross_Earnings <= 14249.99:
    sss_contribution = 630.00
elif 14250 <= Gross_Earnings <= 14749.99:
    sss_contribution = 652.50
elif 14750 <= Gross_Earnings <= 15249.99:
    sss_contribution = 675.00
elif 15250 <= Gross_Earnings <= 15749.99:
    sss_contribution = 697.50
elif 15750 <= Gross_Earnings <= 16249.99:
    sss_contribution = 720.00
elif 16250 <= Gross_Earnings <= 16749.99:
    sss_contribution = 742.50
elif 16750 <= Gross_Earnings <= 17249.99:
    sss_contribution = 765.00
elif 17250 <= Gross_Earnings <= 17749.99:
    sss_contribution = 787.50
elif 17750 <= Gross_Earnings <= 18249.99:
    sss_contribution = 810.00
elif 18250 <= Gross_Earnings <= 18749.99:
    sss_contribution = 832.50
elif 18750 <= Gross_Earnings <= 19249.99:
    sss_contribution = 855.00
elif 19250 <= Gross_Earnings <= 19749.99:
    sss_contribution = 877.50
elif 19750 <= Gross_Earnings <= 20249.99:
    sss_contribution = 900.00
elif 20250 <= Gross_Earnings <= 20749.99:
    sss_contribution = 900.00
elif 20750 <= Gross_Earnings <= 21249.99:
    sss_contribution = 900.00
elif 21250 <= Gross_Earnings <= 21749.99:
    sss_contribution = 900.00
elif 21750 <= Gross_Earnings <= 22249.99:
    sss_contribution = 900.00
elif 22250 <= Gross_Earnings <= 22749.99:
    sss_contribution = 900.00
elif 22750 <= Gross_Earnings <= 23249.99:
    sss_contribution = 900.00
elif 23250 <= Gross_Earnings <= 23749.99:
    sss_contribution = 900.00
elif 23750 <= Gross_Earnings <= 24249.99:
    sss_contribution = 900.00
elif 24250 <= Gross_Earnings <= 24749.99:
    sss_contribution = 900.00
elif 24750 <= Gross_Earnings <= 25249.99:
    sss_contribution = 900.00
elif 25250 <= Gross_Earnings <= 26749.99:
    sss_contribution = 900.00
elif 26750 <= Gross_Earnings <= 27249.99:
    sss_contribution = 900.00
elif 27250 <= Gross_Earnings <= 28749.99:
    sss_contribution = 900.00
elif 28750 <= Gross_Earnings <= 29249.99:
    sss_contribution = 900.00
elif 29250 <= Gross_Earnings <= 29749.99:
    sss_contribution = 900.00
else:
    sss_contribution = 900.00

# Determine withholding Philhealth Contribution
if Gross_Earnings <=9999.99:
    Philhealth_Contribution= 0
elif Gross_Earnings == 10000.00:
    Philhealth_Contribution = 500
elif 10000.01<= Gross_Earnings <= 99999.99:
    Philhealth_Contribution = Gross_Earnings*0.05
else:
    Philhealth_Contribution = 5000

# Statement for witholding tax
if 0 <= Gross_Earnings <= 20832.99:
    witholding_tax = 0.00
elif 20833 <= Gross_Earnings<= 33332:
    witholding_tax = 0.15 / 20833
elif 33333 <= Gross_Earnings <= 66666:
    witholding_tax = 1875 + 0.2 / 33333
elif 66667 <= Gross_Earnings <= 166666:
    witholding_tax = 8541.80 + 0.25 / 66667
elif 166666 <= Gross_Earnings <= 666666:
    witholding_tax = 33541.80 + 0.3 / 166667
else:
    witholding_tax = 183541.80 + 0.35 / 666667

# Total Deductions
deductions = Hours_of_absent+ Hours_tardy + Withholding_Tax + sss_contribution + Philhealth_Contribution + Pagibig_Contribution

# Net Pay
net_pay = Gross_Earnings - deductions

# Output Section
print("\n--- Payroll Summary ---")
print(f"Company Name: {Company_Name}")
print(f"Employee Code: {Employee_Code}")
print(f"Employee Name: {Employee_Name}")
print(f"Department: {Department}")
print(f"Pay Period: {Salary_Date_Cutoff}")
print(f"Basic Pay: {Basic_pay:.2f}")
print(f"Overtime Pay: {Overtime_pay:.2f}")
print(f"Absences: {Hours_of_absent:.2f}")
print(f"Honorarium: {Honorarium:.2f}")
print(f"Tardy: {Hours_tardy:.2f}")
print(f"Withholding Tax: {Withholding_Tax:.2f}")
print(f"SSS Contribution: {sss_contribution:.2f}")
print(f"HDMF Contribution: {Pagibig_Contribution:.2f}")
print(f"PhilHealth Contribution: {Philhealth_Contribution:.2f}")
print(f"Total Deductions: {deductions:.2f}")
print(f"Gross Earnings: {Gross_Earnings:.2f}")
print(f"Net Pay: {net_pay:.2f}")



