students = [
    {'stdid': 'std101', 'stdname': 'Ashish kumar', 'standard': '10th', 'age': 15, 'hindi': 67, 'english': 89, 'maths': 87, 'science': 89, 'computer': 90, 'total': 422},
    {'stdid': 'std102', 'stdname': 'abhishek kumar', 'standard': '10th', 'age': 14, 'hindi': 85, 'english': 45, 'maths': 48, 'science': 90, 'computer': 45, 'total': 313},
    {'stdid': 'std103', 'stdname': 'aman', 'standard': '10th', 'age': 15, 'hindi': 23, 'english': 56, 'maths': 78, 'science': 78, 'computer': 67, 'total': 302},
    {'stdid': 'std104', 'stdname': 'rahul', 'standard': '10th', 'age': 14, 'hindi': 45, 'english': 67, 'maths': 45, 'science': 45, 'computer': 56, 'total': 258},
    {'stdid': 'std105', 'stdname': 'ruby', 'standard': '10th', 'age': 13, 'hindi': 89, 'english': 67, 'maths': 89, 'science': 93, 'computer': 65, 'total': 403},
    {'stdid': 'std106', 'stdname': 'suman', 'standard': '10th', 'age': 13, 'hindi': 90, 'english': 46, 'maths': 67, 'science': 67, 'computer': 67, 'total': 337},
    {'stdid': 'std107', 'stdname': 'saurabh', 'standard': '10th', 'age': 15, 'hindi': 45, 'english': 23, 'maths': 34, 'science': 45, 'computer': 34, 'total': 181},
    {'stdid': 'std108', 'stdname': 'sumit', 'standard': '10th', 'age': 14, 'hindi': 23, 'english': 45, 'maths': 67, 'science': 78, 'computer': 90, 'total': 303},
    {'stdid': 'std109', 'stdname': 'kamlesh', 'standard': '10th', 'age': 15, 'hindi': 45, 'english': 56, 'maths': 78, 'science': 99, 'computer': 67, 'total': 345},
    {'stdid': 'std110', 'stdname': 'rohan', 'standard': '10th', 'age': 15, 'hindi': 34, 'english': 12, 'maths': 24, 'science': 45, 'computer': 56, 'total': 171}
]

# Define the header
header = ["Student ID", "Name", "Standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]

# Calculate the width for each column based on the longest item in each column
col_widths = [max(len(str(student[col])) for student in students) for col in students[0].keys()]
# Adjust column widths for header
col_widths = [max(col_width, len(header[i])) for i, col_width in enumerate(col_widths)]

# Print the header
header_str = " | ".join(f"{header[i]:<{col_widths[i]}}" for i in range(len(header)))
print(header_str)
print("-" * len(header_str))

# Print each row
for student in students:
    row_str = " | ".join(f"{str(student[key]):<{col_widths[j]}}" for j, key in enumerate(student.keys()))
    print(row_str)
print("\n")
# Action insights

# a) Display name of student whose marks in English is greater than 50
print("a) Students with English marks greater than 50:")
for student in students:
    if student['english'] > 50:
        print(student['stdname'])

# b) Display student name and age of top 4 scorers in Maths
print("\nb) Top 4 scorers in Maths:")
top_4_maths_students = sorted(students, key=lambda x: x['maths'], reverse=True)[:4]
for student in top_4_maths_students:
    print(f"{student['stdname']} (Age: {student['age']})")

# c) Display name, ID, and age of students who are bottom three scorers in Computer
print("\nc) Bottom 3 scorers in Computer:")
bottom_3_computer_students = sorted(students, key=lambda x: x['computer'])[:3]
for student in bottom_3_computer_students:
    print(f"{student['stdname']} (ID: {student['stdid']}, Age: {student['age']})")
