from Activity_4 import StudentData, CourseInfo


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

    # Display the student data
    print("\n=== ENROLLMENT DETAILS ===\n")
    student.display()

    # Display course information
    course_info.display()




if __name__ == "__main__":
    main()