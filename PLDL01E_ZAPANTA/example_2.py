#Initialization of Final grade, equivalent grade, and Student Name
final_grade = 0
equivalent_grade = 0
student_name = ""

#Input and read the student's name, final quizzes, final research/assignment, final project, and final exam ratings
student_name = str(input("Enter the student's name: "))
final_quizzes = float(input("Enter the student's final quizzes grade: "))
final_research_assignment = float(input("Enter the student's final research/assignment grade: "))
final_project = float(input("Enter the student's final project grade: "))
final_exam_ratings = float(input("Enter the student's final exam ratings: "))

#setting the formula for the final grade of the student
final_grade = (0.30 * final_quizzes) + (0.10 * final_research_assignment) + (0.40 * final_exam_ratings) + (0.20 * final_project)

#Setting the formula for determining the equivalent grade using the final grade
if 98 <= final_grade <= 100:
    equivalent_grade = 4.00
elif 95 <= final_grade < 98:
    equivalent_grade = 3.75
elif 92 <= final_grade < 95:
    equivalent_grade = 3.50
elif 89 <= final_grade < 92:
    equivalent_grade = 3.25
elif 86 <= final_grade < 89:
    equivalent_grade =3.00
elif 83 <= final_grade < 86:
    equivalent_grade = 2.75
elif 80 <= final_grade < 83:
    equivalent_grade = 2.50
elif 77 <= final_grade < 80:
    equivalent_grade = 2.25
elif 74 <= final_grade < 77:
    equivalent_grade = 2.00
elif 71 <= final_grade < 74:
    equivalent_grade = 1.75
elif 68 <= final_grade < 71:
    equivalent_grade = 1.50
elif 64 <= final_grade < 68:
    equivalent_grade = 1.25
elif 60 <= final_grade < 64:
    equivalent_grade = 1.00
else:
    equivalent_grade = 0.00

#Displaying the studen's name, final quizzes, final research/assignment, final project, final exam rating, the final grades and equivalent grade
print("Student name:",student_name)
print("Final quizzes grade:",final_quizzes)
print("Final research/assignment grade:", final_research_assignment)
print("Final project grade:",final_project)
print("Final exam rating:",final_exam_ratings)
print("Final grades:",final_grade)
print("Equivalent grade:",equivalent_grade)