#student record management system using singly linked list 




class StudentNode:
    def __init__(self, roll_no, name, marks ):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name, marks):
        new_node = StudentNode(roll_no, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("Student record added.")

    def delete_student(self, roll_no):
        current = self.head
        prev = None
        while current:
            if current.roll_no ==roll_no:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print("Student record deleted")
                return
            prev = current
            current = current.next
        print("Student not found.")

    def update_student(self,roll_no,new_name, new_marks):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                current.name = new_name 
                current.marks = new_marks
                print("Student record updated.")
                return
            current = current.next
        print("Student not found.")

    def search_student(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                print(f"Student found: Roll No: {current.roll_no}, Name: {current.name}, Marks: {current.marks}")
                return
            current = current.next
        print("Student not found.")

    def display_students(self, sort_by="roll_no", ascendng=True):
        students = []
        current = self.head
        while current:
            students.append((current.roll_no, current.name, current.marks))
            current = current.next

        if sort_by == "roll_no":
            students.sort(key=lambda x: x[0], reverse=not ascending)
        elif sort_by == "marks":
            students.sort(key=lambda x: x[2], reverse=not ascending)

        if not students:
            print("No student records found.")
            return
        print("Student Records:")
        for s in students:
            print(f"Roll No: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

    # Menu to interact with the system
def menu():
        system = StudentLinkedList()
        while True:
            print("\n---STUDENT RECORD MANAGEMENT MENU---")
            print("1. Add Student Record")
            print("2. Delete Student Record")
            print("3. Update Student Record")
            print("4. Search Student Record")
            print("5. Display All Student Records")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                roll = int(input("Enter Roll No: "))
                name = input("Enter Name: ")
                marks = int(input("Enter Marks: "))
                system.add_student(roll, name, marks)

            elif choice == '2':
                roll_no = int(input("Enter Roll No to delete: "))
                system.delete_student(roll_no)

            elif choice == '3':
                roll_no = int(input("Enter Roll No to update: "))
                new_name = input("Enter New Name: ")
                new_marks = float(input("Enter New Marks: "))
                system.update_student(roll_no, new_name, new_marks)

            elif choice == '4':
                roll_no = int(input("Enter Roll No to search: "))
                system.search_student(roll_no)

            elif choice == '5':
                sort_by = input("Sort by (roll_no/marks): ").strip().lower()
                ascending_input = input("Sort order (asc/desc): ").strip().lower()
                ascending = True if ascending_input == "asc" else False
                system.display_students(sort_by=sort_by, ascending=ascending)


            elif choice == '6':
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")

#start the system
menu()