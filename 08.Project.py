def load_constitution(filename):
    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    return [line.strip() for line in lines]

def find_section(lines, index):
    start = index
    while start > 0 and lines[start] != "":
        start = start - 1
    
    end = index
    while end < len(lines) - 1 and lines[end] != "":
        end = end + 1
    
    return start + 1, end - 1

def search_constitution(lines, term):
    i = 0
    while i < len(lines):
        if term.lower() in lines[i].lower():
            start, end = find_section(lines, i)
            print("Line " + str(start) + ":")
            for j in range(start, end + 1):
                print("Line " + str(j + 1) + ": " + lines[j])
            print("\n")
            i = end
        i = i + 1

def main():
    filename = "constitution.txt"
    lines = load_constitution(filename)
    
    while True:
        term = input("Enter search term: ").strip()
        if term == "":
            break
        print("\nSearching for: " + term)
        search_constitution(lines, term)
    
if __name__ == "__main__":
    main()