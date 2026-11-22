class Student:
    def __init__(self, student_id, name, email, major):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.major = major
        self.enrollments = []

    def enroll(self, course):
        enrollment = Enrollment(self, course)
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Major: {self.major}")

    def display_courses(self):
        print(f"\nCourses for {self.name}:")

        if not self.enrollments:
            print("No courses enrolled.")
            return

        for enrollment in self.enrollments:
            print(
                f"{enrollment.course.course_code} - "
                f"{enrollment.course.course_name} - "
                f"Grade: {enrollment.grade}"
            )


class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.enrollments = []

    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Credits: {self.credits}")


class Enrollment:
    def __init__(self, student, course, grade=None):
        self.student = student
        self.course = course
        self.grade = grade

    def assign_grade(self, grade):
        self.grade = grade


student1 = Student(
    "S001",
    "Mahgol",
    "mahgol@example.com",
    "Computer Engineering"
)

course1 = Course(
    "CS101",
    "Introduction to Programming",
    3
)

course2 = Course(
    "CS102",
    "Object-Oriented Programming",
    3
)

student1.enroll(course1)
student1.enroll(course2)

student1.enrollments[0].assign_grade("A")
student1.enrollments[1].assign_grade("B+")

student1.display_info()

student1.display_courses()