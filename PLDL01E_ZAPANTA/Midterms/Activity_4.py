class StudentData:
    def __init__(self, name, course, student_number, acad_year, date_printed):
        self.name = name
        self.course = course
        self.student_number = student_number
        self.acad_year = acad_year
        self.date_printed = date_printed

    def display(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Student No.: {self.student_number}")
        print(f"Acad. Year: {self.acad_year}")
        print(f"Date Printed: {self.date_printed}")


class CourseInfo:
    def __init__(self):
        self.sections = []
        self.subjects = []
        self.units = []

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            section = input(f"Enter Section for Course {i + 1}: ")
            subject = input(f"Enter Subject for Course {i + 1}: ")
            unit = int(input(f"Enter Units for Course {i + 1}: "))
            self.sections.append(section)
            self.subjects.append(subject)
            self.units.append(unit)

    def display(self):
        print("\n=== COURSE INFORMATION ===\n")
        print(f"{'Section':<10} {'Subject':<40} {'Units':<5}")
        for i in range(len(self.sections)):
            print(f"{self.sections[i]:<10} {self.subjects[i]:<40} {self.units[i]:<5}")
        print(f"Total Units: {sum(self.units)}")


class AssessmentFees:
    def __init__(self, total_units, downpayment):
        self.fees = {}
        self.total_units = total_units
        self.downpayment = downpayment
        self.tuition_fee_per_unit = 1551.00
        self.assessment_amt = 0
        self.total_due = 0
        self.prelims = 0
        self.midterms = 0
        self.finals = 0

    def input_fees(self):
        self.fees['AdU Chronicle'] = float(input("Enter AdU Chronicle Fee: "))
        self.fees['Athletic'] = float(input("Enter Athletic Fee: "))
        self.fees['Audio-Visual Library'] = float(input("Enter Audio-Visual Library Fee: "))
        self.fees['AUSG'] = float(input("Enter AUSG Fee: "))
        self.fees['Cultural'] = float(input("Enter Cultural Fee: "))
        self.fees['Energy Cost/Aircon Classroom'] = float(input("Enter Energy Cost/Aircon Fee: "))
        self.fees['Guidance'] = float(input("Enter Guidance Fee: "))
        self.fees['Insurance'] = float(input("Enter Insurance Fee: "))
        self.fees['LMS'] = float(input("Enter LMS Fee: "))
        self.fees['Library'] = float(input("Enter Library Fee: "))
        self.fees['Medical and Dental'] = float(input("Enter Medical and Dental Fee: "))
        self.fees['Registration'] = float(input("Enter Registration Fee: "))
        self.fees['RSO'] = float(input("Enter RSO Fee: "))
        self.fees['Student Activities'] = float(input("Enter Student Activities Fee: "))
        self.fees['Student Nurturance'] = float(input("Enter Student Nurturance Fee: "))
        self.fees['Technology'] = float(input("Enter Technology Fee: "))
        self.fees['Test Papers'] = float(input("Enter Test Papers Fee: "))

    def compute_fees(self):
        self.fees['Tuition Fee Lecture'] = self.total_units * self.tuition_fee_per_unit
        self.assessment_amt = sum(self.fees.values())
        self.total_due = self.assessment_amt + self.downpayment
        self.prelims = self.total_due / 3
        self.midterms = self.total_due / 3
        self.finals = self.total_due / 3

    def display(self):
        print("\n=== ASSESSMENT OF FEES ===\n")
        for fee_name, amount in self.fees.items():
            print(f"{fee_name}: {amount:.2f} P")
        print(f"\nAssessment Amount: {self.assessment_amt:.2f} P")
        print(f"Downpayment: {self.downpayment:.2f} P")
        print(f"Total Due: {self.total_due:.2f} P")
        print(f"Prelims: {self.prelims:.2f} P")
        print(f"Midterms: {self.midterms:.2f} P")
        print(f"Finals: {self.finals:.2f} P")
