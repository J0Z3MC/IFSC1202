def load_names(filename):
    boys = []
    girls = []
    try:
        file = open(filename, 'r')
        rank = 1
        for line in file:
            line = line.strip()
            parts = line.split(',')
            boy_name = parts[0].strip()
            girl_name = parts[1].strip()
            boys.append(boy_name)
            girls.append(girl_name)
            rank += 1
        file.close()
    except:
        print("Error: Could not open file.")
        return [], []
    return boys, girls

def search_name(name, boys, girls):
    for i in range(len(boys)):
        if boys[i] == name:
            return "Boy’s Name - Rank: " + str(i + 1)
        if girls[i] == name:
            return "Girls’s Name - Rank: " + str(i + 1)
    return "Name Not Found"

def main():
    filename = "Exam Two Names.txt"
    boys, girls = load_names(filename)
    if boys == [] and girls == []:
        return
    
    while True:
        user_input = input("Enter a Name: ")
        user_input = user_input.strip()
        if user_input == 'Q' or user_input == 'q':
            break
        
        formatted_name = user_input[0].upper() + user_input[1:].lower()
        result = search_name(formatted_name, boys, girls)
        print(result)

main()