#       The Overly Verbose GPA Calculator

# Function to get a valid numeric grade from user input
def get_valid_grade(prompt: str) -> float:
    """
    Prompt the user for a grade and validate it.

    Parameters:
        prompt (str): The message shown to the user when requesting input.

    Returns:
        float: A valid numeric grade between 0.0 and 4.0 inclusive.

    Functionality:
        - Continuously prompts the user until a valid float is entered.
        - Ensures the grade is within the 0.0 - 4.0 range.
        - Handles non-numeric inputs gracefully.
    """
    while True:
        try:
            # Attempt to convert user input to float
            grade = float(input(prompt))
            if 0.0 <= grade <= 4.0:
                return grade  # Valid grade entered
            else:
                print("That is not a valid grade. It must be between 0.0 and 4.0.")
        except ValueError:
            # Handles cases where input cannot be converted to float
            print("Please enter a numeric value.")

#   Program Introduction
print("Welcome to The Overly Verbose GPA Calculator")
print("Let's get started!")

#   Collecting Grades
grades = []
num_grades = 5  # Number of grades to collect

for i in range(num_grades):
    # Prompt user for each grade and append to grades list
    grade = get_valid_grade(f"Enter grade #{i+1} (0.0-4.0): ")
    grades.append(grade)

print("\nAll grades recorded:", grades)

#   Calculate Current GPA
total = sum(grades)
count = len(grades)
current_gpa = total / count  # Average of all grades

print("\nCalculating... crunch")
print(f"Your current GPA is: {current_gpa:.2f}")

#   Analyze Semester GPA
choice = input("\nWould you like to analyze your 'first' or 'second' half of classes? ").strip().lower()
midpoint = len(grades) // 2  # Split grades into two halves

# Slice the grades list based on user choice
if choice == "first":
    semester_grades = grades[:midpoint]
elif choice == "second":
    semester_grades = grades[midpoint:]
else:
    # Default to first half if input is invalid
    print("Invalid choice — defaulting to first half!")
    semester_grades = grades[:midpoint]

# Compute the GPA for the chosen half
semester_gpa = sum(semester_grades) / len(semester_grades)

print(f"\nYour {choice if choice in ['first','second'] else 'first'} semester GPA is: {semester_gpa:.2f}")

# Provide feedback comparing semester GPA to overall GPA
if semester_gpa > current_gpa:
    print("Good Job! You improved in this part of the semester.")
elif semester_gpa < current_gpa:
    print("Looks like your grade dropped. Time to lock in!")
else:
    print("You're staying consistent. Way to go!")

#   Goal GPA Analysis
goal_gpa = get_valid_grade("\nWhat's your goal GPA? ")

# Check if current GPA already meets or exceeds the goal
if goal_gpa <= current_gpa:
    print(f"Wow! Your current GPA of {current_gpa:.2f} already meets or exceeds your goal!")
else:
    possible = []  # List to track which grade(s) can be improved to reach goal

    # Algorithm: Check if raising a single grade to 4.0 allows reaching goal GPA
    for i in range(len(grades)):
        temp_grades = grades.copy()  # Copy current grades to avoid modifying original
        temp_grades[i] = 4.0  # Hypothetically raise this grade
        new_gpa = sum(temp_grades) / len(temp_grades)
        if new_gpa >= goal_gpa:
            possible.append(i + 1)  # Store class index (1-based)

    # Display result based on analysis
    if possible:
        print(f"\nYou can reach your goal of {goal_gpa:.2f} by raising one grade to 4.0!")
        print("Try improving grade(s):", ', '.join(map(str, possible)))
    else:
        print(f"\nEven if you raised one grade to 4.0, you wouldn’t reach your goal of {goal_gpa:.2f}.")
        print("You’ll need to boost multiple grades!")

#   Program End
print("\nThanks for using The Overly Verbose GPA Calculator")
