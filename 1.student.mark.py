# Initialize the data structures
students = []
courses = []
marks = {}

# Define a function to input the number of students in a class
def input_num_students():
    while True:
        num_students = int(input("Enter number of students in the class: "))
        if num_students <= 0:
            print("Error: Number of students must be positive. Please try again.")
        else:
            print("Number of students: ", num_students)
            return num_students

# Define a function to input student information
def input_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DD/MM/YYYY): ")
    students.append((id, name, dob))

# Define a function to input course information
def input_course():
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append((id, name))

# Define a function to select a course and input marks for students in that course
def input_marks():
    # List the available courses
    print("Available courses:")
    for i, course in enumerate(courses):
        print("{}: {}".format(i+1, course[1]))

    # Ask the user to select a course
    choice = int(input("Select a course (1-{}): ".format(len(courses))))
    course_id = courses[choice-1][0]

    # Loop through the students and ask for their marks in the selected course
    for student in students:
        id = student[0]
        name = student[1]
        mark = float(input("Enter mark for student {} ({}) in course {}: ".format(name, id, course_id)))
        marks.setdefault(course_id, []).append((id, mark))

# Define a function to list courses
def list_courses():
    print("List of courses:")
    for course in courses:
        print("ID: {}, Name: {}".format(course[0], course[1]))

# Define a function to list students
def list_students():
    print("List of students:")
    for student in students:
        print("ID: {}, Name: {}, Date of Birth: {}".format(student[0], student[1], student[2]))

# Define a function to show student marks for a given course
def show_marks():
    # List the available courses
    print("Available courses:")
    for i, course in enumerate(courses):
        print("{}: {}".format(i+1, course[1]))

    # Ask the user to select a course
    choice = int(input("Select a course (1-{}): ".format(len(courses))))
    course_id = courses[choice-1][0]

    # Print the marks for the selected course
    print("Marks for course {}:".format(course_id))
    for mark in marks.get(course_id, []):
        print("Student ID: {}, Mark: {}".format(mark[0], mark[1]))

# Define the main function to show the menu
def main():
    # Loop until the user selects the Exit option
    while True:
        # Show the menu options
        print("\nMenu:")
        print("1. Input")
        print("2. Listing")
        print("3. Exit")

        # Ask the user to select an option
        choice = int(input("Select an option (1-3): "))

        # Handle the Input option
        if choice == 1:
            while True:
                # Show the input options
                print("\nInput options:")
                print("1. Input number of students in a class")
                print("2. Input student information: id, name, Dob")
                print("3. Input number of courses")
                print("4. Input marks for a course")
                print("5. Back to main menu")

                # Ask the user to select an option
                sub_choice = int(input("Select an option (1-5): "))

                # Handle the sub-menu options
                if sub_choice == 1:
                    input_num_students()
                elif sub_choice == 2:
                    input_student()
                elif sub_choice == 3:
                    input_course()
                elif sub_choice == 4:
                    input_marks()
                elif sub_choice == 5:
                    break
                else:
                    print("Invalid option. Please try again.")

        # Handle the Listing option
        elif choice == 2:
            while True:
                # Show the listing options
                print("\nListing options:")
                print("1. List courses")
                print("2. List students")
                print("3. Show marks for a course")
                print("4. Back to main menu")

                # Ask the user to select an option
                sub_choice = int(input("Select an option (1-4): "))

                # Handle the sub-menu options
                if sub_choice == 1:
                    list_courses()
                elif sub_choice == 2:
                    list_students()
                elif sub_choice == 3:
                    show_marks()
                elif sub_choice == 4:
                    break
                else:
                    print("Invalid option. Please try again.")

        # Handle the Exit option
        elif choice == 3:
            print("Exiting program...")
            break

        # Handle invalid options
        else:
            print("Invalid option. Please try again.")
            
# Call the main function
main()