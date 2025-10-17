def get_valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0.0 <= grade <= 4.0:
                return grade
            else: 
                print ("That is not a valid grade it must be between 0.0 and 4.0")
        except ValueError:
            ("please enter a numeric value")

print ("welcome to The Overly Verbose GPA Calculator")
print ("Lets get started")

grades = []
num_grades = 5

for i in range(num_grades):
    grade = get_valid_grade(f"Enter grade #{i+1} (0.0-4.0): ")
    grades.append(grade)

print("\nAll grades recorded:", grades)

total = sum(grades)
count = len(grades)
current_gpa = total / count

print("\nCalculating.. crunch")
print(f"Your current GPA is: {current_gpa:.2f}")

choice = input("\nWould you like to analyze your 'first' or 'second' half of classes ").strip().lower()

midpoint = len(grades) // 2

if choice == "first":
    semester_grades = grades[:midpoint]
elif choice == "second":
    semester_grades = grades[midpoint:]
else:
    print("Invalid choice — defaulting to first half!")
    semester_grades = grades[:midpoint]

semester_gpa = sum(semester_grades) / len(semester_grades)

print(f"\nYour {choice if choice in ['first','second'] else 'first'} semester GPA is: {semester_gpa:.2f}")

if semester_gpa > current_gpa:
    print(" Good Job! You improved in this part of the semester.")
elif semester_gpa < current_gpa:
    print(" Looks like your grade dropped time to lock in!")
else:
    print(" Your staying consistent way to go!")

goal_gpa = get_valid_grade("\nWhat’s your goal GPA? ")

if goal_gpa <= current_gpa:
    print(f"Wow! Your current GPA of {current_gpa:.2f} already meets or exceeds your goal!")
else:
    possible = []
    for i in range(len(grades)):
        temp_grades = grades.copy()
        temp_grades[i] = 4.0
        new_gpa = sum(temp_grades) / len(temp_grades)
        if new_gpa >= goal_gpa:
            possible.append(i + 1)

    if possible:
        print(f"\nYou can reach your goal of {goal_gpa:.2f} by raising one grade to 4.0!")
        print("Try improving grade(s):", ', '.join(map(str, possible)))
    else:
        print(f"\nEven if you raised one grade to 4.0, you wouldn’t reach your goal of {goal_gpa:.2f}.")
        print("You’ll need to boost multiple grades!")

print("\nThanks for using The Overly Verbose GPA Calculator")