stdid = ['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110']
stdname = ['Ashish kumar','abhishek kumar','aman','rahul','ruby','suman','saurabh','sumit','kamlesh','rohan']
standard = ['10th','10th','10th','10th','10th','10th','10th','10th','10th','10th']
age = [15,14,15,14,13,13,15,14,15,15]
hindi = [67,85,23,45,89,90,45,23,45,34]
english = [89,45,56,67,67,46,23,45,56,12]
maths = [87,48,78,45,89,67,34,67,78,24]
science = [89,90,78,45,93,67,45,78,99,45]
computer = [90,45,67,56,65,67,34,90,67,56]
total = [422,313,302,258,403,337,181,303,345,171]
main_list = (stdid, stdname, standard, age, hindi, english, maths, science, computer, total)
# Define the header
header = ["Student ID", "Name", "Standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]
# Calculate the width for each column based on the longest item in each list
col_widths = [max(len(str(item)) for item in col) for col in main_list]
# Adjust column widths for header
col_widths = [max(col_width, len(header[i])) for i, col_width in enumerate(col_widths)]
# Print the header
header_str = " | ".join(f"{header[i]:<{col_widths[i]}}" for i in range(len(header)))
print(header_str)
print("-" * len(header_str))
# Print each row
for i in range(len(stdid)):
    row = [stdid[i], stdname[i], standard[i], age[i], hindi[i], english[i], maths[i], science[i], computer[i], total[i]]
    row_str = " | ".join(f"{str(row[j]):<{col_widths[j]}}" for j in range(len(row)))
    print(row_str)
print("\n")
print("TASK - 1 : Display name of students whose marks in English is greater than 50")
for i in range(len(english)):
    if english[i]>50:
        print(stdname[i],"-",english[i])
print("\n")
print("TASK - 2 : Display student name and age of top 4 scorer in maths")
toppers_4 = sorted(range(len(maths)), key=lambda x: maths[x], reverse=True)[:4]
for i in toppers_4:
    print(f"{stdname[i]} (Age: {age[i]})")
print("\n")
print("TASK - 3 :  Display name , id , age of students who are bottom three scorer in computer")
bottom_3 = sorted(range(len(computer)), key=lambda x: computer[x])[:3]
for i in bottom_3:
    print(f"{stdname[i]} (ID: {stdid[i]}, Age: {age[i]})")