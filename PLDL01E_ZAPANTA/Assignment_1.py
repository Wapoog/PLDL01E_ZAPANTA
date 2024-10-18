class Employee:
    hdmf = 100.00

    def __init__(self):
        self.hdmf_contribution = self.hdmf
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
        self.emp_tardiness = self.emp_num_tardiness * self.emp_rate_per_hour

    # SSS Contribution using a list of tuples
    sss_brackets = [
        (0, 4250, 180.00),
        (4251, 4749.99, 202.50),
        (4750, 5249.99, 225.00),
        (5250, 5749.99, 247.50),
        (5750, 6249.99, 270.00),
        (6250, 6749.99, 292.50),
        (6750, 7249.99, 315.00),
        (7250, 7749.99, 337.50),
        (7750, 8249.99, 360.00),
        (8250, 8749.99, 382.50),
        (8750, 9249.99, 405.00),
        (9250, 9749.99, 427.50),
        (9750, 10249.99, 450.00),
        (10250, 10749.99, 472.50),
        (10750, 11249.99, 495.00),
        (11250, 11749.99, 517.50),
        (11750, 12249.99, 540.00),
        (12250, 12749.99, 562.50),
        (12750, 13249.99, 585.00),
        (13250, 13749.99, 607.50),
        (13750, 14249.99, 630.00),
        (14250, 14749.99, 652.50),
        (14750, 15249.99, 675.00),
        (15250, 15749.99, 697.50),
        (15750, 16249.99, 720.00),
        (16250, 16749.99, 742.50),
        (16750, 17249.99, 765.00),
        (17250, 17749.99, 787.50),
        (17750, 18249.99, 810.00),
        (18250, 18749.99, 832.50),
        (18750, 19249.99, 855.00),
        (19250, 19749.99, 877.50),
        (19750, float('inf'), 900.00)
    ]

    def emp_sss_contribution(self):
        """Calculate SSS contribution based on gross earnings."""
        self.sss_contribution = 0.00
        for low, high, contribution in self.sss_brackets:
            if low <= self.emp_gross_earnings <= high:
                self.sss_contribution = contribution
                break

    # PhilHealth Contribution
    def emp_philhealth_contribution(self):
        """Calculate PhilHealth contribution based on gross earnings."""
        if self.emp_gross_earnings < 10000