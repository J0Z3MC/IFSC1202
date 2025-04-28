class Sketch:
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'
        self.pen = 'U'
        self.canvas = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(' ')
            self.canvas.append(row)

    def printsketch(self):
        print('+' + '-' * self.size + '+')
        for y in range(self.size - 1, -1, -1):
            print('|', end='')
            for x in range(self.size):
                print(self.canvas[y][x], end='')
            print('|')
        print('+' + '-' * self.size + '+')
        print('X =', self.xpos, ' Y =', self.ypos, ' Direction =', self.direction)

    def penup(self):
        self.pen = 'U'

    def pendown(self):
        self.pen = 'D'

    def turnleft(self):
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'U'

    def turnright(self):
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'U'

    def move(self, distance):
        for i in range(distance):
            if self.pen == 'D':
                self.canvas[self.ypos][self.xpos] = '*'

            if self.direction == 'U':
                if self.ypos + 1 < self.size:
                    self.ypos = self.ypos + 1
                else:
                    break
            elif self.direction == 'D':
                if self.ypos - 1 >= 0:
                    self.ypos = self.ypos - 1
                else:
                    break
            elif self.direction == 'R':
                if self.xpos + 1 < self.size:
                    self.xpos = self.xpos + 1
                else:
                    break
            elif self.direction == 'L':
                if self.xpos - 1 >= 0:
                    self.xpos = self.xpos - 1
                else:
                    break
        if self.pen == 'D':
            self.canvas[self.ypos][self.xpos] = '*'

def main():
    f = open('Cshape.txt', 'r')
    lines = f.readlines()
    f.close()

    commands = []
    for line in lines:
        line = line.strip()
        if line != '':
            commands.append(line)

    size = int(commands[0])
    sketch = Sketch(size)

    for cmd in commands[1:]:
        if ',' in cmd:
            parts = cmd.split(',')
            command = int(parts[0])
            value = int(parts[1])
        else:
            command = int(cmd)
            value = None

        if command == 1:
            sketch.penup()
        elif command == 2:
            sketch.pendown()
        elif command == 3:
            sketch.turnright()
        elif command == 4:
            sketch.turnleft()
        elif command == 5:
            if value is not None:
                sketch.move(value)
        elif command == 6:
            sketch.printsketch()

if __name__ == "__main__":
    main()