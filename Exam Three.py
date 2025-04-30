import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)

    def type(self):
        if self.s1 == self.s2 and self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

    def angles(self):
        a = self.s1
        b = self.s2
        c = self.s3
        angle1 = math.degrees(math.acos((b*b + c*c - a*a) / (2 * b * c)))
        angle2 = math.degrees(math.acos((a*a + c*c - b*b) / (2 * a * c)))
        angle3 = 180 - angle1 - angle2
        return [angle1, angle2, angle3]

triangles = []

file = open("Exam Three Triangles.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    sides = line.strip().split(",")
    t = Triangle(sides[0], sides[1], sides[2])
    triangles.append(t)

print("      Type     Side 1     Side 2     Side 3  Perimeter       Area    Angle 1    Angle 2    Angle 3")

for t in triangles:
    angles = t.angles()
    print(f"{t.type():>12} {t.s1:10.3f} {t.s2:10.3f} {t.s3:10.3f} {t.perimeter():10.3f} {t.area():10.3f} {angles[0]:10.3f} {angles[1]:10.3f} {angles[2]:10.3f}")