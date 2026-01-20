# Student Attendance Management System

attendance = {}

def mark_attendance():
    name = input("Enter student name: ")
    status = input("Enter status (P/A): ").upper()
    attendance[name] = status
    print("Attendance marked.")

def view_attendance():
    if not attendance:
        print("No attendance records found.")
    else:
        print("\nAttendance Report")
        for name, status in attendance.items():
            print(name, ":", "Present" if status == "P" else "Absent")

while True:
    print("\nAttendance Menu")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        print("Exiting Attendance System.")
        break
    else:
        print("Invalid choice.")
