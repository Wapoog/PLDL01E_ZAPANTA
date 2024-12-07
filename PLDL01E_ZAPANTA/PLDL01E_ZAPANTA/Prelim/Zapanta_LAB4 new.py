# this program is design to compute the payroll salary of an employee
class Employee:
    hdmf = 100.00

    # initialization or constructor method of
    def __init__(self):
        # class Employee
        self.hdmf_contribution = 100.00
        self.company_name = input("Enter Company Name: ")
        self.employee_department = input("Enter Employee Department: ")
        self.employee_name = input("Enter Employee Name: ")
        self.employee_code = input("Enter Employee Code: ")
        self.salary_cutoff_date = input("Enter Cut-off Date: ")

        # Input Computation
        self.emp_rate_per_hour = float(input("Employee rate per hour: "))
        self.emp_num_of_hours_per_payday = int(input("Employee's number of hours worked per payday: "))
        self.emp_hour_overtime = float(input("Employee overtime hours: "))
        self.honorarium_pay = float(input("Employee Honorarium Pay: "))
        self.emp_num_of_absences = int(input("Employee absences: "))
        self.emp_num_tardiness = int(input("Employee tardiness: "))

    def emp_salary_computation(self):
        self.basic_pay = self.emp_rate_per_hour * self.emp_num_of_hours_per_payday
        self.overtime_pay = self.emp_hour_overtime * self.emp_rate_per_hour
        self.emp_gross_earnings = self.basic_pay + self.overtime_pay + self.honorarium_pay
        self.emp_absences = self.emp_num_of_absences * self.emp_rate_per_hour
        self.emp_tardiness =  self.emp_num_tardiness * self.emp_rate_per_hour

    def emp_sss_contribution(self):
        # Setting condition for Employee's Gross Earnings to get the SSS, Tax, and Philhealth Contribution
        if self.emp_gross_earnings < 0:
            self.sss_contribution = 0.00
        elif self.emp_gross_earnings >= 0 and self.emp_gross_earnings < 4250.00:
            self.sss_contribution = 180.00
        elif self.emp_gross_earnings >= 4251 and self.emp_gross_earnings < 4759.99:
            self.sss_contribution = 202.50
        elif self.emp_gross_earnings >= 4750 and self.emp_gross_earnings < 5249.99:
            self.sss_contribution = 225.00
        elif self.emp_gross_earnings >= 5250 and self.emp_gross_earnings < 5749.99:
            self.sss_contribution = 247.50
        elif self.emp_gross_earnings >= 4750 and self.emp_gross_earnings < 6249.99:
            self.sss_contribution = 270.00
        elif self.emp_gross_earnings >= 6250 and self.emp_gross_earnings < 6749.99:
            self.sss_contribution = 292.50
        elif self.emp_gross_earnings >= 6750 and self.emp_gross_earnings < 7249.99:
            self.sss_contribution = 315.00
        elif self.emp_gross_earnings >= 7250 and self.emp_gross_earnings < 7749.99:
            self.sss_contribution = 337.50
        elif self.emp_gross_earnings >= 7750 and self.emp_gross_earnings < 8249.99:
            self.sss_contribution = 360.00
        elif self.emp_gross_earnings >= 8250 and self.emp_gross_earnings < 8749.99:
            self.sss_contribution = 382.50
        elif self.emp_gross_earnings >= 8750 and self.emp_gross_earnings < 9249.99:
            self.sss_contribution = 405.00
        elif self.emp_gross_earnings >= 9250 and self.emp_gross_earnings < 9749.99:
            self.sss_contribution = 427.50
        elif self.emp_gross_earnings >= 9750 and self.emp_gross_earnings < 10249.99:
            self.sss_contribution = 450.00
        elif self.emp_gross_earnings >= 10250 and self.emp_gross_earnings < 10749.99:
            self.sss_contribution = 472.50
        elif self.emp_gross_earnings >= 10750 and self.emp_gross_earnings < 11249.99:
            self.sss_contribution = 495.00
        elif self.emp_gross_earnings >= 11250 and self.emp_gross_earnings < 11749.99:
            self.sss_contribution = 517.50
        elif self.emp_gross_earnings >= 11750 and self.emp_gross_earnings < 12249.99:
            self.sss_contribution = 540.00
        elif self.emp_gross_earnings >= 12250 and self.emp_gross_earnings < 12749.99:
            self.sss_contribution = 562.50
        elif self.emp_gross_earnings >= 12750 and self.emp_gross_earnings < 13249.99:
            self.sss_contribution = 585.00
        elif self.emp_gross_earnings >= 13250 and self.emp_gross_earnings < 13749.99:
            self.sss_contribution = 607.50
        elif self.emp_gross_earnings >= 13750 and self.emp_gross_earnings < 14249.99:
            self.sss_contribution = 630.00
        elif self.emp_gross_earnings >= 14250 and self.emp_gross_earnings < 14749.99:
            self.sss_contribution = 652.50
        elif self.emp_gross_earnings >= 14750 and self.emp_gross_earnings < 15249.99:
            self.sss_contribution = 675.00
        elif self.emp_gross_earnings >= 15250 and self.emp_gross_earnings < 15749.99:
            self.sss_contribution = 697.50
        elif self.emp_gross_earnings >= 15750 and self.emp_gross_earnings < 16249.99:
            self.sss_contribution = 720.00
        elif self.emp_gross_earnings >= 16250 and self.emp_gross_earnings < 16749.99:
            self.sss_contribution = 742.50
        elif self.emp_gross_earnings >= 16750 and self.emp_gross_earnings < 17249.99:
            self.sss_contribution = 765.00
        elif self.emp_gross_earnings >= 17250 and self.emp_gross_earnings < 17749.99:
            self.sss_contribution = 787.50
        elif self.emp_gross_earnings >= 17750 and self.emp_gross_earnings < 18249.99:
            self.sss_contribution = 810.00
        elif self.emp_gross_earnings >= 18250 and self.emp_gross_earnings < 18749.99:
            self.sss_contribution = 832.50
        elif self.emp_gross_earnings >= 18750 and self.emp_gross_earnings < 19249.99:
            self.sss_contribution = 855.00
        elif self.emp_gross_earnings >= 19250 and self.emp_gross_earnings < 19749.99:
            self.sss_contribution = 877.50
        elif self.emp_gross_earnings >= 19758 and self.emp_gross_earnings < 20249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 20250 and self.emp_gross_earnings < 20749.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 20750 and self.emp_gross_earnings < 21249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 21250 and self.emp_gross_earnings < 21749.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 21750 and self.emp_gross_earnings < 22249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 22250 and self.emp_gross_earnings < 22749.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 22750 and self.emp_gross_earnings < 23249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 23250 and self.emp_gross_earnings < 23749.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 23750 and self.emp_gross_earnings < 24249.99:
            self.sss_contribution = 900.00
        elif self.emp_gross_earnings >= 24250 and self.emp_gross_earnings < 24749.99:
            self.sss_contribution = 900
        else:
            self.sss_contribution = 900.00

    def emp_philhealth_contribution(self):
    # Setting conditions in getting PhilHealth Contribution
        if self.emp_gross_earnings < 10000:
            self.philhealth_contribution = 0.00
        else:
            self.philhealth_contribution = self.emp_gross_earnings * 0.0450

# Setting conditions in getting Tax Contribution
    def emp_tax_contribution(self):
        if self.emp_gross_earnings < 10417:
            self.tax_contribution = 0.00
        elif self.emp_gross_earnings >= 10417 and self.emp_gross_earnings <= 16666:
            self.tax_contribution = ((self.emp_gross_earnings - 10417) * 0.15 + 0.00)
        elif self.emp_gross_earnings >= 16667 and self.emp_gross_earnings <= 33332:
            self.tax_contribution = ((self.emp_gross_earnings - 16667) * 0.20 + 937.50)
        elif self.emp_gross_earnings >= 33333 and self.emp_gross_earnings <= 83332:
            self.tax_contribution = ((self.emp_gross_earnings - 33333) * 0.25 + 4270.70)
        elif self.emp_gross_earnings >= 83333 and self.emp_gross_earnings <= 333332:
            self.tax_contribution = ((self.emp_gross_earnings - 83333) * 0.30 + 16770.70)
        else:
            self.tax_contribution = ((self.emp_gross_earnings - 333333) * 0.35 + 91770.70)

    def emp_total_deduction(self):
        self.deduction = (self.emp_absences + self.emp_tardiness + self.tax_contribution + self.sss_contribution
                          + self.philhealth_contribution + self.hdmf_contribution)

    def emp_employee_netpay(self):
            self.net_pay = self.emp_gross_earnings - self.deduction
        #display Student method of class Employee
    def emp_displayEmployee(self):
        print("Company Name: ", self.company_name)
        print("Employee Department:", self.employee_department)
        print("Employee Name:", self.employee_name)
        print("Employee Code:", self.employee_code)
        print("Cut-Off Date:", self.salary_cutoff_date)
        print("Basic Pay: %.2f" % self.basic_pay)
        print("Overtime Pay: %.2f" % self.overtime_pay)
        print("Gross Income: %.2f" % self.emp_gross_earnings)
        print("Absences: %.2f" % self.emp_absences)
        print("Tardiness: %.2f" % self.emp_tardiness)
        print("SSS Contribution: %.2f" % self.sss_contribution)
        print("TAX Contribution: %2f" % self.tax_contribution)
        print("Philhealth Contribution: %.2f" % self.philhealth_contribution)
        print("Total Deduction: %.2f" % self.deduction)
        print("Net Income: %.2f" % self.net_pay)

emp1 = Employee()
emp1.emp_salary_computation()
emp1.emp_sss_contribution()
emp1.emp_philhealth_contribution()
emp1.emp_tax_contribution()
emp1.emp_total_deduction()
emp1.emp_employee_netpay()
emp1.emp_displayEmployee()