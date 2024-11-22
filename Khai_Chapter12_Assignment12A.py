# In this assignment, I am using exam grades from a previous assignment, and performing calculations to gather the mean, min, max, etc of all exam grades.



import numpy as np

# Data for student's exam grades
grades_data = np.array([
    [85, 78, 92],
    [67, 55, 79],
    [90, 84, 86],
    [58, 62, 49],
    [75, 80, 85],
    [60, 61, 58],
    [82, 76, 79],
    [47, 52, 45],
    [88, 90, 91],
    [79, 81, 84]
])


# Display data from each exam
def calculate_exam_statistics(data):
    num_exams = data.shape[1]
    for exam in range(num_exams):
        print(f"\nStatistics for Exam {exam + 1}:")
        exam_scores = data[:, exam]
        print(f"Mean: {np.mean(exam_scores):.2f}")
        print(f"Median: {np.median(exam_scores):.2f}")
        print(f"Standard Deviation: {np.std(exam_scores):.2f}")
        print(f"Minimum: {np.min(exam_scores):.2f}")
        print(f"Maximum: {np.max(exam_scores):.2f}")


# Calculate overall results for the set
def calculate_overall_statistics(data):
    flat_data = data.flatten()
    print("\nOverall Statistics for All Exams Combined:")
    print(f"Mean: {np.mean(flat_data):.2f}")
    print(f"Median: {np.median(flat_data):.2f}")
    print(f"Standard Deviation: {np.std(flat_data):.2f}")
    print(f"Minimum: {np.min(flat_data):.2f}")
    print(f"Maximum: {np.max(flat_data):.2f}")


# Determine pass and fail grades
def pass_fail_counts(data, passing_grade=60):
    num_exams = data.shape[1]
    for exam in range(num_exams):
        exam_scores = data[:, exam]
        passed = np.sum(exam_scores >= passing_grade)
        failed = np.sum(exam_scores < passing_grade)
        print(f"\nExam {exam + 1}:")
        print(f"Number of Students Passed: {passed}")
        print(f"Number of Students Failed: {failed}")


# Calculate pass percentages
def calculate_overall_pass_percentage(data, passing_grade=60):
    total_scores = data.size
    total_passed = np.sum(data >= passing_grade)
    pass_percentage = (total_passed / total_scores) * 100
    print(f"\nFinal Passing Percentages: {pass_percentage:.2f}%")



def main():

    print("First Few Rows of the Dataset:")
    print(grades_data[:5])


    calculate_exam_statistics(grades_data)


    calculate_overall_statistics(grades_data)


    pass_fail_counts(grades_data)


    calculate_overall_pass_percentage(grades_data)


if __name__ == "__main__":
    main()
