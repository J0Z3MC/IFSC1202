class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = [score.strip() for score in scores]

    def RunningAverage(self):
        valid_scores = []
        for score in self.Grades:
            if score != '':
                valid_scores.append(float(score))
        if len(valid_scores) > 0:
            return sum(valid_scores) / len(valid_scores)
        else:
            return 0.0

    def TotalAverage(self):
        total = 0.0
        for score in self.Grades:
            if score != '':
                total += float(score)
            else:
                total += 0.0
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

def main():
    try:
        with open("10.Project Student Scores.txt", "r") as file:
            print(f"{'First':<12}{'Last':<12}{'ID Number':<12}{'Running Avg':<15}{'Semester Avg':<15}{'Grade':<6}")
            print("=" * 72)

            for line in file:
                parts = line.strip().split(",")
                firstname = parts[0]
                lastname = parts[1]
                tnumber = parts[2]
                scores = parts[3:]
                student = Student(firstname, lastname, tnumber, scores)
                print(f"{student.FirstName:<12}{student.LastName:<12}{student.TNumber:<12}"
                      f"{student.RunningAverage():<15.2f}{student.TotalAverage():<15.2f}"
                      f"{student.LetterGrade():<6}")
    except FileNotFoundError:
        print("The file '10.Project Student Scores.txt' was not found.")

if __name__ == "__main__":
    main()
