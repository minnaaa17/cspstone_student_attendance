# Attendance Shortage Alert — Capstone Project
# Complete this file by following docs/STUDENT_GUIDE.md

DATA_FILE = "data/students.txt"
SHORTAGE_LIMIT = 75


# Calculate average attendance from a list like ["English:60", "Maths:72"]
def calculate_average(subject_list):
    # Your code will go here
    total = 0
    for entry in subject_list:
        parts = entry.split(":")
        total = total + float(parts[1])
    average = total / len(subject_list)
    return average

   

# Print each subject with OK or SHORTAGE WARNING if below 75%
def check_shortage(subject_list):
    # Your code will go here
    for entry in subject_list:
        parts    = entry.split(":")
        sub_name = parts[0]
        pct      = float(parts[1])


        if pct < SHORTAGE_LIMIT:
            print(sub_name, ":", pct, "% --> SHORTAGE WARNING")
        else:
            print(sub_name, ":", pct, "% -- OK")

    


# Ask for student details and save one line to the file (type 'done' to go back)
def add_student():
    # Your code will go here
     while True:
        roll = input("\nRoll no (or 'done' to go back): ")
        if roll == "done":
            break


        name   = input("Name   : ")
        stream = input("Stream : ")
        n      = int(input("Number of subjects: "))


        subjects = []
        for i in range(n):
            sub = input("  Subject name : ")
            pct = input("  Attendance % : ")
            subjects.append(sub + ":" + pct)


        subjects_str = " ".join(subjects)
        line = roll+" "+name+" "+stream+" "+subjects_str


        with open(DATA_FILE, "a") as f:
            f.write(line + "\n")
        print("Record saved for", name)




# Search student by roll number and show attendance report
def search_student():
    # Your code will go here
    search_roll = input("\nEnter roll number to search: ")
    found = False


    try:
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(" ")
                if parts[0] == search_roll:
                    found        = True
                    student_name = parts[1]
                    stream       = parts[2]
                    subject_list = parts[3:]


                    print("\n--- Student Report ---")
                    print("Roll   :", search_roll)
                    print("Name   :", student_name)
                    print("Stream :", stream)
                    print("\nSubject-wise Attendance:")


                    check_shortage(subject_list)


                    avg = calculate_average(subject_list)
                    print("\nAverage Attendance :", round(avg, 2), "%")


                    if avg < SHORTAGE_LIMIT:
                        print("OVERALL STATUS: SHORTAGE — Below 75%")
                    else:
                        print("OVERALL STATUS: Attendance is Good")


    except FileNotFoundError:
        print("No records file found. Add a student first.")


    if found == False:
        print("No record found for roll number:", search_roll)

   


# Show main menu and handle user choice in a loop
def main():
    # Your code will go here
     while True:
        print("\n=== Attendance Alert System ===")
        print("1. Add Student Record")
        print("2. Search Student")
        print("3. Exit")


        choice = input("Enter choice: ")


        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
   
    


if __name__ == "__main__":
    main()
