from Activity_4 import StudentData, CourseInfo, AssessmentFees


def main():
    # Collect student details
    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    student_number = input("Enter Student Number: ")
    acad_year = input("Enter Academic Year: ")
    current_date = input("Enter Current Date (YYYY-MM-DD): ")

    # Create an object of the StudentData class
    student = StudentData(student_name, course, student_number, acad_year, current_date)

    # Create an object of the CourseInfo class and input course details
    course_info = CourseInfo()
    course_info.input_courses()

    # Input downpayment
    downpayment = float(input("Enter Downpayment Amount (P): "))

    # Create an object of the AssessmentFees class, passing total units and downpayment
    fees = AssessmentFees(sum(course_info.units), downpayment)

    # Input assessment fees
    fees.input_fees()

    # Compute assessment and display
    fees.compute_fees()

    # Display the student data
    print("\n=== ENROLLMENT DETAILS ===\n")
    student.display()

    # Display course information
    course_info.display()

    # Display the fees information
    fees.display()


if __name__ == "__main__":
    main()