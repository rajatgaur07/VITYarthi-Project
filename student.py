class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = {}  # Subject: Marks

    def add_marks(self, subject, marks):
        if 0 <= marks <= 100:
            self.marks[subject] = marks
            return True
        return False

    def get_average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90: return 'A+'
        elif avg >= 80: return 'A'
        elif avg >= 70: return 'B+'
        elif avg >= 60: return 'B'
        elif avg >= 50: return 'C'
        else: return 'F'

    def __str__(self):
        return f"{self.roll_no} | {self.name} | {self.course} | Avg: {self.get_average():.2f} | Grade: {self.get_grade()}"



                                student.add_marks(sub, int(mark))
                    self.students[roll_no] = student
        except FileNotFoundError:
            pass  # First time running
