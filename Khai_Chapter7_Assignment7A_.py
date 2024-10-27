import csv


def input_student_grades():
    # Ask for the number of students
    num_students = int(input("Enter the number of students: "))

    # Open the CSV file for writing
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Input student data
        for _ in range(num_students):
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write the student record to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])


if __name__ == "__main__":
    input_student_grades()
