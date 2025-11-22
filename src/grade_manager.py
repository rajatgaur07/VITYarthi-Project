from .student import Student

class GradeManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = {}
        self.load_data()

    def add_student(self, roll_no, name, age, course):
        if roll_no in self.students:
            return False
        self.students[roll_no] = Student(roll_no, name, age, course)
        self.save_data()
        return True

    def view_all(self):
        if not self.students:
            print("No students found!")
            return
        for student in self.students.values():
            print(student)

    def update_marks(self, roll_no, subject, marks):
        if roll_no not in self.students:
            return False
        return self.students[roll_no].add_marks(subject, marks)

    def delete_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]
            self.save_data()
            return True
        return False

    def get_topper(self):
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.get_average())

    def save_data(self):
        with open(self.filename, 'w') as f:
            for student in self.students.values():
                marks_str = ';'.join([f"{k}:{v}" for k, v in student.marks.items()])
                f.write(f"{student.roll_no}|{student.name}|{student.age}|{student.course}|{marks_str}\n")

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if not line.strip(): continue
                    parts = line.strip().split('|')
                    roll_no = parts[0]
                    name = parts[1]
                    age = int(parts[2])
                    course = parts[3]
                    student = Student(roll_no, name, age, course)
                    
                    if len(parts) > 4 and parts[4]:
                        marks_data = parts[4].split(';')
                        for item in marks_data:
                            if ':' in item:
                                sub, mark = item.split(':')
                                student.add_marks(sub, int(mark))
                    self.students[roll_no] = student
        except FileNotFoundError:
            pass  # First time running
