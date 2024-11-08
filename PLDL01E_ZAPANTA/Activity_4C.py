from Activity_4 import StudentData, AssessmentFees

def main():
    # Collect student details
    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    student_number = input("Enter Student Number: ")
    acad_year = input("Enter Academic Year: ")
    current_date = input("Enter Current Date (YYYY-MM-DD): ")

    # Create an object of the StudentData class
    student = StudentData(student_name, course, student_number, acad_year, current_date)

    # Collect total units for assessment
    total_units = int(input("Enter Total Units Enrolled: "))

    # Input downpayment
    downpayment = float(input("Enter Downpayment Amount (P): "))

    # Create an object of the AssessmentFees class, passing total units and downpayment
    fees = AssessmentFees(total_units, downpayment)

    # Input assessment fees
    fees.input_fees()

    # Compute assessment and display
    fees.compute_fees()

    # Display the student data
    print("\n=== ENROLLMENT DETAILS ===\n")
    student.display()

    # Display the fees information
    fees.display()

if __name__ == "__main__":
    main()
