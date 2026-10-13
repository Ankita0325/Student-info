class Student:
    def __init__(self):
        self.name =""
        self.rollno = ""
        self.subjects = {}
        self.total_marks =0
        self.percentage = 0.0
        self.attendance = 0
    
    def menu(self):
        while True :
            choice = int(input("""
            Enter your choice btw 1-6 :
            1. Add Student 
            2. View Students 
            3. Search Student 
            4. Class Summary 
            5. Ineligible Students
            6. Exit
            """))

            if choice == 1 :
                # add student
                self.add_student()
            elif choice ==2:
                #view student
                self.view_student()
            elif choice ==3:
                #search student
                self.search_student()
            elif choice ==4:
                #class summary
                self.class_summary()
                
            elif choice == 5:
                self.ineligible()
                
            elif choice == 6:
                exit()
            else:
                print("Invalid choice Please enter a valid choice !")
                

    def add_student(self):
        self.name = input("Enter student Name :")
        self.rollno = input("Enter Roll Number :")

        
        self.subjects = {}
        total_sub = int(input("Total no. of subject :"))
        
        for i in range(total_sub):
            subject_name = input(f"enter subject {i+1}name :")
            student_marks = float(input(f"enter marks of {subject_name} :"))
            
            self.subjects[subject_name] = student_marks
        
        
        self.total_marks = sum(self.subjects.values())
        
        self.percentage =(self.total_marks/(total_sub*100))*100 if total_sub > 0 else 0
        
        self.attendance = int(input("Enter student attendance :"))
        print(f"Student {self.name}, roll number {self.rollno}, "
            "has been added successfully!")   
            
        
    def view_student(self):
        print("\n--- Student Details ---")
        print(f"Student Name : {self.name}")
        print(f"Roll Number : {self.rollno}")
        print(f"Subjects and Marks : {self.subjects}")
        print(f"Total Marks : {self.total_marks}")
        print(f"Percentage : {self.percentage:.2f}%")
        print(f"Attendance: {self.attendance}%")
        
   
        
    def search_student(self):
        search_rollno =(input(" enter roll number to search student :"))
        if search_rollno == self.rollno:
            print("Student found")
            self.view_student()
        else:
            print("Student not found") 
            
            
    def class_summary(self):
        print("\n--- Class Summary ---")
        print(f"Student Name : {self.name}")
        print(f"Roll Number : {self.rollno}")
        
        if 90 < self.percentage <= 100:
            print("Grade: A+ ")
        elif 80 < self.percentage < 90:
            print("Grade: A")
        elif 70 < self.percentage < 80:
            print("Grade: B")
        elif 60 < self.percentage <= 70:
            print("Grade: C")
        elif 50 < self.percentage <= 60:
            print("Grade: D")
        else:
            print("Grade: F")
            
        if self.attendance >= 75:
            print("Eligible")
        else:
            print("Not Eligible")
            
        
    def ineligible(self):
        count =0
        if self.attendance < 75:
            count +=1
        print(count)
            

student = Student()
student.menu()
    