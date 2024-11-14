grades = []
passed_students = []
valid_input = True
total_students = 0

print("________Enter student grades between 40 to 100!")
print("________Type 'done' if finished")
print("________!NOTE! 'please use lowercase only!' !NOTE!")
while True:
    user_input = input("            Enter Student Grade: ")

    if user_input == 'done':
        print("......cAlcUlAtInGg......")
        break
    
    else: 
        grade = int(user_input)
        if grade < 40 or grade > 100:
            print("Error. Please enter a valid number.")
            valid_input = False
            break
        else:
            grades.append(grade)
            total_students += 1
            if grade >= 75:
                passed_students.append(grade)
                
if valid_input:
    if grades:
        average_grade = sum(grades) / len(grades)
        passing = (len(passed_students) / total_students) * 100 if total_students > 0 else 0

        print(f"Grades Entered: {grades}")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Number of Students who passed the Subject: {len(passed_students)}")
        print(f"Passing Percentage: {passing:.2f}%")