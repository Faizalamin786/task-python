
import statistics
import matplotlib.pyplot as plt
import os

# ==========================================
# STUDENT PERFORMANCE ANALYTICS SYSTEM
# ==========================================

# Initial Dataset (List containing Tuples)
students = [
    ("Amit", 78),
    ("Priya", 92),
    ("Rahul", 65),
    ("Sneha", 88),
    ("Vikas", 55),
    ("Neha", 74),
    ("Arjun", 96),
    ("Kiran", 82),
    ("Riya", 69),
    ("Ankit", 90)
]


# ==========================================
# OOP: ENCAPSULATION
# ==========================================

class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def display_details(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A+"
        elif self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "D"


# ==========================================
# OOP: INHERITANCE
# ==========================================

class PerformanceStudent(Student):

    def calculate_grade(self):
        marks = self.get_marks()

        if marks >= 90:
            return "Excellent"
        elif marks >= 75:
            return "Good"
        elif marks >= 50:
            return "Average"
        else:
            return "Needs Improvement"


# ==========================================
# OOP: POLYMORPHISM
# ==========================================

def show_student_performance(student):
    print(student.get_name(),
          ":", student.calculate_grade())


# ==========================================
# COLLECTIONS: DICTIONARY
# ==========================================

student_data = {}

for name, marks in students:
    student_data[name] = marks


# ==========================================
# ADD STUDENT
# ==========================================

def add_student():

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    if name in student_data:
        print("Student already exists!")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100!")
            return

        student_data[name] = marks
        print("Student added successfully!")

    except ValueError:
        print("Please enter valid marks!")


# ==========================================
# UPDATE STUDENT
# ==========================================

def update_student():

    name = input("Enter student name to update: ").strip()

    if name in student_data:

        try:
            marks = float(input("Enter new marks: "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100!")
                return

            student_data[name] = marks
            print("Student updated successfully!")

        except ValueError:
            print("Invalid marks!")

    else:
        print("Student not found!")


# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student():

    name = input("Enter student name to delete: ").strip()

    if name in student_data:
        del student_data[name]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


# ==========================================
# DISPLAY STUDENTS
# ==========================================

def display_students():

    if not student_data:
        print("No student records found!")
        return

    print("\n===== STUDENT RECORDS =====")

    for name, marks in student_data.items():
        print("Name:", name, "| Marks:", marks)


# ==========================================
# STATISTICAL ANALYSIS
# ==========================================

def statistical_analysis():

    marks = list(student_data.values())

    if not marks:
        print("No data available!")
        return

    print("\n===== STATISTICAL ANALYSIS =====")

    print("Mean:", statistics.mean(marks))
    print("Median:", statistics.median(marks))

    try:
        print("Mode:", statistics.mode(marks))
    except statistics.StatisticsError:
        print("Mode: No mode")

    print("Range:", max(marks) - min(marks))

    print("Variance:", statistics.variance(marks)
          if len(marks) > 1 else 0)

    print("Standard Deviation:",
          statistics.stdev(marks) if len(marks) > 1 else 0)

    # Quartiles
    q1, q2, q3 = statistics.quantiles(
        marks, n=4, method="inclusive"
    ) if len(marks) >= 2 else (marks[0], marks[0], marks[0])

    print("Q1:", q1)
    print("Q2:", q2)
    print("Q3:", q3)

    # Interquartile Range
    iqr = q3 - q1

    print("IQR:", iqr)


# ==========================================
# PROBABILITY ANALYSIS
# ==========================================

def probability_analysis():

    marks = list(student_data.values())

    total_students = len(marks)

    if total_students == 0:
        print("No data available!")
        return

    # Simple Probability
    passed_students = [
        m for m in marks if m >= 40
    ]

    probability_pass = len(passed_students) / total_students

    print("\n===== PROBABILITY ANALYSIS =====")

    print("Total Students:", total_students)

    print("Students scoring 40 or above:",
          len(passed_students))

    print("Probability of passing:",
          probability_pass)

    # Conditional Probability
    # A = Students scoring 90 or above
    # B = Students scoring 80 or above

    event_b = [m for m in marks if m >= 80]

    event_a_and_b = [
        m for m in marks if m >= 90
    ]

    if len(event_b) > 0:

        conditional_probability = (
            len(event_a_and_b) / len(event_b)
        )

        print("Students scoring 80 or above:",
              len(event_b))

        print("Students scoring 90 or above:",
              len(event_a_and_b))

        print("P(90+ | 80+):",
              conditional_probability)


# ==========================================
# OOP DEMONSTRATION
# ==========================================

def oop_demonstration():

    print("\n===== OOP DEMONSTRATION =====")

    student1 = Student("Amit", 78)

    student2 = PerformanceStudent("Priya", 92)

    print("\nEncapsulation:")
    student1.display_details()

    print("\nInheritance:")
    print("Student name:", student2.get_name())

    print("\nPolymorphism:")

    show_student_performance(student1)
    show_student_performance(student2)


    
# ==========================================
# DATA VISUALIZATION
# ==========================================

def data_visualization():

    names = list(student_data.keys())
    marks = list(student_data.values())

    if not marks:
        print("No student data available!")
        return

    # Create screenshots folder automatically
    os.makedirs("screenshots", exist_ok=True)

    print("\n===== GENERATING GRAPHS =====")

    # 1. HISTOGRAM
    plt.figure(figsize=(8, 5))
    plt.hist(marks, bins=5, color="skyblue", edgecolor="black")
    plt.title("Student Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", alpha=0.3)
    plt.savefig("screenshots/histogram.png")
    plt.show()
    plt.close()

    print("Histogram saved!")

    # 2. BAR CHART
    plt.figure(figsize=(9, 5))
    plt.bar(names, marks, color="orange", edgecolor="black")
    plt.title("Student Marks Comparison")
    plt.xlabel("Student Names")
    plt.ylabel("Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("screenshots/bar_chart.png")
    plt.show()
    plt.close()

    print("Bar Chart saved!")

    # 3. BOX PLOT
    plt.figure(figsize=(7, 5))
    plt.boxplot(marks, patch_artist=True,
                boxprops=dict(facecolor="lightgreen"))
    plt.title("Student Marks Box Plot")
    plt.ylabel("Marks")
    plt.grid(axis="y", alpha=0.3)
    plt.savefig("screenshots/box_plot.png")
    plt.show()
    plt.close()

    print("Box Plot saved!")

    # 4. SCATTER PLOT
    plt.figure(figsize=(8, 5))
    student_numbers = list(range(1, len(marks) + 1))

    plt.scatter(student_numbers, marks,
                color="red", s=100)

    plt.title("Student Performance Scatter Plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")
    plt.grid(True, alpha=0.3)
    plt.savefig("screenshots/scatter_plot.png")
    plt.show()
    plt.close()

    print("Scatter Plot saved!")

    # 5. LINE CHART
    plt.figure(figsize=(8, 5))
    plt.plot(names, marks, marker="o",
             color="blue", linewidth=2)

    plt.title("Student Marks Line Chart")
    plt.xlabel("Student Names")
    plt.ylabel("Marks")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("screenshots/line_chart.png")
    plt.show()
    plt.close()

    print("Line Chart saved!")

    print("\nAll 5 graphs generated successfully!")
    print("Check the screenshots folder.")



# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n================================")
        print(" STUDENT PERFORMANCE ANALYTICS ")
        print("================================")

        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Statistical Analysis")
        print("6. Probability Analysis")
        print("7. OOP Demonstration")
        print("8. Data Visualization")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            update_student()

        elif choice == "3":
            delete_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            statistical_analysis()

        elif choice == "6":
            probability_analysis()

        elif choice == "7":
            oop_demonstration()

        elif choice == "8":
            data_visualization()
        elif choice == "9":
            print("Thank you for using Student Performance Analytics!")
            break


# ==========================================
# PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    main()
