class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = []

    def RunningAverage(self):
        total = 0
        count = 0
        for score in self.Grades:
            if score != '':
                total += float(score)
                count += 1
        if count > 0:
            return total / count
        else:
            return 0.0

    def TotalAverage(self):
        total = 0
        for score in self.Grades:
            if score != '':
                total += float(score)
            else:
                total += 0
        if len(self.Grades) > 0:
            return total / len(self.Grades)
        else:
            return 0.0

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        newstudent = Student(firstname, lastname, tnumber)
        self.Studentlist.append(newstudent)

    def find_student(self, tnumber):
        for i in range(len(self.Studentlist)):
            if self.Studentlist[i].TNumber == tnumber:
                return i
        return -1

    def print_student_list(self):
        print("{:<12}{:<12}{:<12}{:<15}{:<15}{:<6}".format("First", "Last", "ID Number", "Running Avg", "Semester Avg", "Grade"))
        print("=" * 72)
        for stu in self.Studentlist:
            print("{:<12}{:<12}{:<12}{:<15.2f}{:<15.2f}{:<6}".format(
                stu.FirstName, stu.LastName, stu.TNumber,
                stu.RunningAverage(), stu.TotalAverage(), stu.LetterGrade()))

    def add_student_from_file(self, filename):
        f = open(filename, "r")
        for line in f:
            info = line.strip().split(",")
            if len(info) == 3:
                self.add_student(info[0], info[1], info[2])
        f.close()

    def add_scores_from_file(self, filename):
        f = open(filename, "r")
        for line in f:
            stuff = line.strip().split(",")
            if len(stuff) == 2:
                idnum = stuff[0].strip()
                score = stuff[1].strip()
                idx = self.find_student(idnum)
                if idx != -1:
                    self.Studentlist[idx].Grades.append(score)
        f.close()

def main():
    sl = StudentList()
    sl.add_student_from_file("11.Project Students.txt")
    sl.add_scores_from_file("11.Project Scores.txt")
    sl.print_student_list()

if __name__ == "__main__":
    main()