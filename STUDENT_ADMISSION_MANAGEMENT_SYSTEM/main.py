import matplotlib.pyplot as plt

class StudentAdmissionSystem:
    def __init__(self):
        self.admin_id = "abc"
        self.admin_password = "123"
        self.students_file = "students.txt"
        self.formatted_students_file = "students_formatted.txt"
        self.students = {}
        self.degree_branches = ["Computer Science", "Information Technology", "AIML", "Data Science", "Cyber Security", "Biotechnology", "Chemical Engineering", "Aerospace Engineering", "Automobile Engineering"]
        self.diploma_branches = ["Mechanical Engineering", "Electrical Engineering", "Civil Engineering", "Electronics"]

        self.min_marks = {
            "Computer Science": 80,
            "Mechanical Engineering": 70,
            "Electrical Engineering": 60,
            "Civil Engineering": 55,
            "Electronics": 50,
            "Information Technology": 75,
            "AIML": 85,
            "Data Science": 82,
            "Cyber Security": 78,
            "Biotechnology": 65,
            "Chemical Engineering": 60,
            "Aerospace Engineering": 88,
            "Automobile Engineering": 68
        }

        self.admission_fees = {
            "Computer Science": 50000,
            "Mechanical Engineering": 45000,
            "Electrical Engineering": 40000,
            "Civil Engineering": 35000,
            "Electronics": 30000,
            "Information Technology": 48000,
            "AIML": 55000,
            "Data Science": 53000,
            "Cyber Security": 52000,
            "Biotechnology": 40000,
            "Chemical Engineering": 38000,
            "Aerospace Engineering": 60000,
            "Automobile Engineering": 42000
        }

        self.load_students_from_file()

    def authenticate(self):
            attempts = 2
            while attempts > 0:
                user_id = input("Enter Admin ID: ")
                password = input("Enter Password: ")
                if user_id == self.admin_id and password == self.admin_password:
                    print("\nAuthentication Successful!\n")
                    return True
                else:
                    attempts -= 1
                    print(f"Incorrect credentials. {attempts} attempt(s) remaining.\n")
            print("Authentication failed. Exiting system.")
            return False
    

    def validate_marks(self, branch, marks):
        if float(marks) < self.min_marks[branch]:
            print(f"Minimum marks required for {branch} is {self.min_marks[branch]}.")
            return False
        return True

    def save_students_to_file(self):
        with open(self.students_file, "w+") as file:
            for student_id, details in self.students.items():
                file.write(f"{student_id},{details['Name']},{details['Gender']},{details['Caste']},{details['Freeship']},{details['ProgramType']},{details['Branch']},{details['PreviousPercentage']}\n")
        
        # Save formatted data
        headers = ["ID", "Name", "Gender", "Caste", "Freeship", "ProgramType", "Branch", "Fee", "Percentage"]
        column_widths = [10, 20, 10, 10, 15, 15, 30, 10, 15]
        
        with open(self.formatted_students_file, "w+") as file:
            header_line = " ".join(f"{headers[i]:<{column_widths[i]}}" for i in range(len(headers)))
            file.write(header_line + "\n")
            file.write("=" * sum(column_widths) + "\n")
            
            for student_id, details in self.students.items():
                freeship_status = details['Freeship'] if details['Caste'].lower() in ["sc", "st"] else "Not Eligible"
                fee = self.calculate_fees(details)
                row = [student_id, details['Name'], details['Gender'], details['Caste'], freeship_status, details['ProgramType'], details['Branch'], str(fee), details['PreviousPercentage']]
                file.write(" ".join(f"{row[i]:<{column_widths[i]}}" for i in range(len(row))) + "\n")

    def load_students_from_file(self):
        try:
            with open(self.students_file, "r+") as file:  # Use "r+" to read without clearing the file
                for line in file:
                    try:
                        student_id, name, gender, caste, freeship, program_type, branch, previous_percentage = line.strip().split(",")
                        self.students[student_id] = {
                            "Name": name,
                            "Gender": gender,
                            "Caste": caste,
                            "Freeship": freeship,
                            "ProgramType": program_type,
                            "Branch": branch,
                            "PreviousPercentage": previous_percentage
                        }
                    except ValueError:
                        print(f"Error parsing line: {line.strip()}")  # Debugging message
        except FileNotFoundError:
            self.students = {}  # If the file doesn't exist, initialize an empty dictionary


    def add_student(self):
        print("\n")
        student_id = int(input("Enter Student ID: "))
        if student_id in self.students:
            print("Student ID already exists. Please try again.")
            return
        name = input("Enter Student Name: ")
        gender = input("Enter Student Gender (M/F): ")
        caste = input("Enter Student Caste: ")
        freeship = "Not Eligible" if caste.lower() not in ["sc", "st"] else input("Does the student have a freeship card? (yes/no): ").lower()
        
        program_type = input("Are you applying for a Degree or Diploma? (Enter 'Degree' or 'Diploma'): ").capitalize()
        if program_type == "Degree":
            branches = self.degree_branches
            previous_percentage = input("Enter your 12th percentage: ")
        elif program_type == "Diploma":
            branches = self.diploma_branches
            previous_percentage = input("Enter your 10th percentage: ")
        else:
            print("Invalid program type. Please try again.")
            return
        print(f"Available {program_type} Branches:")
        for i, branch in enumerate(branches, 1):
            print(f"{i}. {branch}")
        branch_choice = input("Enter the number corresponding to the branch: ")
        if branch_choice.isdigit() and int(branch_choice) in range(1, len(branches) + 1):
            branch = branches[int(branch_choice) - 1]
        else:
            print("Invalid branch choice.")
            return
        if not self.validate_marks(branch, previous_percentage):
           return
        self.students[student_id] = {"Name": name, "Gender": gender, "Caste": caste, "Freeship": freeship, "ProgramType": program_type, "Branch": branch, "PreviousPercentage": previous_percentage}
        self.save_students_to_file()
        print("Student added successfully!")

    def calculate_fees(self, student):
        if student['Caste'].lower() in ["sc", "st"] and student['Freeship'] == "yes":
            return 6000
        return self.admission_fees.get(student['Branch'], "N/A")

    def search_by_caste(self):
        caste = input("Enter caste to search: ")
        found = False
        print("\n")
        print(f"{'ID':<10}{'Name':<20}{'Gender':<10}{'Caste':<15}{'ProgramType':<10}{'Branch':<30}{'Percentage':<15}")
        print("=" * 120)
        for student_id, details in self.students.items():
            if details['Caste'].lower() == caste.lower():
                print(f"{student_id:<10}{details['Name']:<20}{details['Gender']:<10}{details['Caste']:<15}{details['ProgramType']:<10}{details['Branch']:<30}{details['PreviousPercentage']:<15}")
                found = True
        if not found:
            print(f"No students found under caste {caste}.")

    def view_students(self):
        if not self.students_file:
            print("\nNo student records found.")
            return
        print("\n")
        headers = ["ID", "Name", "Gender", "Caste", "Freeship", "ProgramType", "Branch", "Fee", "Percentage"]
        column_widths = [10, 20, 10, 10, 15, 15, 30, 10, 12]
        
        header_line = " ".join(f"{headers[i]:<{column_widths[i]}}" for i in range(len(headers)))
        print(header_line)
        print("=" * sum(column_widths))
        
        for student_id, details in self.students.items():
            freeship_status = details['Freeship'] if details['Caste'].lower() in ["sc", "st"] else "Not Eligible"
            fee = self.calculate_fees(details)
            row = [student_id, details['Name'], details['Gender'], details['Caste'], freeship_status, details['ProgramType'], details['Branch'], str(fee), details['PreviousPercentage']]
            print(" ".join(f"{row[i]:<{column_widths[i]}}" for i in range(len(row))))

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        if student_id not in self.students:
            print("\nStudent ID not found. Please try again.")
            return
        del self.students[student_id]
        self.save_students_to_file()
        print("\nStudent deleted successfully!")

    def view_students_by_branch(self):
        branch = input("Enter the branch name: ")
        found = False
        print("\n")
        print(f"{'ID':<10}{'Name':<20}{'Gender':<10}{'Program Type':<10}{'Branch':<30}{'Fee':<15}{'Percentage':<15}")
        print("_"*120)
        for student_id, details in self.students.items():
            if details["Branch"] == branch:
                fee = self.admission_fees.get(branch, "N/A")
                print(f"{student_id:<10}{details['Name']:<20}{details['Gender']:<10}{details['ProgramType']:<10}{branch:<30}{fee:<15}{details['PreviousPercentage']:<15}")
                found = True
        if not found:
            print(f"No students found in the {branch} branch.")

    def view_students_by_program_type(self):
        program_type = input("Enter the program type (Degree/Diploma): ").capitalize()
        found = False
        print("\n")
        print(f"{'ID':<10}{'Name':<20}{'Gender':<10}{'ProgramType':<10}{'Branch':<30}{'Fee':<15}{'Percentage':<15}")
        print("="*120)
        for student_id, details in self.students.items():
            if details["ProgramType"] == program_type:
                branch = details['Branch']
                fee = self.admission_fees.get(branch, "N/A")
                print(f"{student_id:<10}{details['Name']:<20}{details['Gender']:<10}{details['ProgramType']:<10}{branch:<30}{fee:<15}{details['PreviousPercentage']:<15}")
                found = True
        if not found:
            print(f"No students found in the {program_type} program type.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        if student_id not in self.students:
            print("Student ID not found. Please try again.")
            return
        
        student = self.students[student_id]
        
        name = input(f"Enter new name (or press Enter to keep {student['Name']}): ").strip() or student['Name']
        gender = input(f"Enter new gender (or press Enter to keep {student['Gender']}): ").strip() or student['Gender']
        caste = input(f"Enter new caste (or press Enter to keep {student['Caste']}): ").strip() or student['Caste']
        freeship = input(f"Enter new freeship status (yes/no) (or press Enter to keep {student['Freeship']}): ").strip() or student['Freeship']
        program_type = input(f"Enter new program type (Degree/Diploma) (or press Enter to keep {student['ProgramType']}): ").strip() or student['ProgramType']
        previous_percentage = input(f"Enter new previous percentage (or press Enter to keep {student['PreviousPercentage']}): ").strip() or student['PreviousPercentage']
        
        print("Available Branches:")
        branches = self.degree_branches if program_type == "Degree" else self.diploma_branches
        for i, branch in enumerate(branches, 1):
            print(f"{i}. {branch}")
        
        branch_choice = input(f"Enter the number corresponding to the branch (or press Enter to keep {student['Branch']}): ")
        if branch_choice:
            if branch_choice.isdigit() and int(branch_choice) in range(1, len(branches) + 1):
                branch = branches[int(branch_choice) - 1]
            else:
                print("Invalid branch choice.")
                return
        else:
            branch = student['Branch']
        
        student.update({
            "Name": name,
            "Gender": gender,
            "Caste": caste,
            "Freeship": freeship,
            "ProgramType": program_type,
            "Branch": branch,
            "PreviousPercentage": previous_percentage
        })
        
        self.save_students_to_file()
        print("\nStudent updated successfully!")

    def search_student(self):
        self.load_students_from_file()

        student_id = input("Enter Student ID to search: ")
        if student_id in self.students:
            details = self.students[student_id]
            fee = self.admission_fees.get(details['Branch'], "N/A")
            print(f"\nID: {student_id}, Name: {details['Name']}, Gender: {details['Gender']}, Caste: {details['Caste']}, "
                f"ProgramType: {details['ProgramType']}, Branch: {details['Branch']}, Fee: {fee}, "
                f"PreviousPercentage: {details['PreviousPercentage']}")
        else:
            print("Student ID not found.")

    def count_total_students(self):
        total_students = len(self.students)
        print(f"Total number of students: {total_students}")

    def list_branches(self):
        print("\nDegree Branches:")
        for branch in self.degree_branches:
            print(f" - {branch}")
        
        print("\nDiploma Branches:")
        for branch in self.diploma_branches:
            print(f" - {branch}")

    def sort_students(self):
        print("Sort by:")
        print("1. Name")
        print("2. Branch")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            sorted_students = sorted(self.students.items(), key=lambda x: x[1]['Name'])
        elif choice == "2":
            sorted_students = sorted(self.students.items(), key=lambda x: x[1]['Branch'])
        else:
            print("Invalid choice")
            return

        print("\n")
        print(f"{'ID':<10}{'Name':<20}{'Gender':<10}{'Caste':<10}{'ProgramType':<12}{'Branch':<30}{'Fee':<15}{'Percentage':<15}")
        print("=" * 130)

        for student_id, details in sorted_students:
            branch = details['Branch']
            caste = details['Caste'].lower()
            freeship_status = details['Freeship'].lower()

            # Check if student belongs to SC/ST caste and has a freeship card
            if caste in ["sc", "st"] and freeship_status == "yes":
                fee = 6000
            else:
                fee = self.admission_fees.get(branch, "N/A")

            print(f"{student_id:<10}{details['Name']:<20}{details['Gender']:<10}{caste:<10}{details['ProgramType']:<12}"
                f"{branch:<30}{fee:<15}{details['PreviousPercentage']:<15}")

    def view_branch_fees(self):
        print("\n")
        print(f"{'Branch':<40}{'Admission Fee':<15}")
        print("=" * 55)
        for branch, fee in self.admission_fees.items():
            print(f"{branch:<40}{fee:<15}")


    def show_student_graph(self):
        branch_counts = {branch: 0 for branch in self.degree_branches + self.diploma_branches}
        for student in self.students.values():
            branch_counts[student["Branch"]] += 1

        branches = list(branch_counts.keys())
        counts = list(branch_counts.values())

        plt.figure(figsize=(10, 6))
        plt.bar(branches, counts, color='skyblue')
        plt.xlabel('Branches')
        plt.ylabel('Number of Students')
        plt.title('Number of Students in Each Branch')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def main(self):
        if not self.authenticate():
            return
        
        while True:
            print("\nStudent Admission Management System")
            print("1.  Add Student")
            print("2.  View Students")
            print("3.  View Students by Branch")
            print("4.  View Students by Program Type")
            print("5.  Delete Student")
            print("6.  Update Student Information")
            print("7.  Search for a Student")
            print("8.  Count Total Students")
            print("9.  List All Branches")
            print("10. Sort Students")
            print("11. View Branch Fees")
            print("12. Search Student by Caste")
            print("13. Graph")
            print("14. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.view_students_by_branch()
            elif choice == "4":
                self.view_students_by_program_type()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                self.update_student()
            elif choice == "7":
                self.search_student()
            elif choice == "8":
                self.count_total_students()
            elif choice == "9":
                self.list_branches()
            elif choice == "10":
                self.sort_students()
            elif choice == "11":
                self.view_branch_fees()
            elif choice == "12":
                self.search_by_caste()
            elif choice == "13":
                self.show_student_graph()
            elif choice == "14":
                print("Exiting the system. Have a Good Day!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = StudentAdmissionSystem()
    system.main()