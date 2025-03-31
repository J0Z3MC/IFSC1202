import csv

def load_distance_table(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        table = []
        for row in reader:
            table.append(row)
    return table

def print_distance_table(table):
    for row in table:
        print("\t".join(row))

def find_index(header, city):
    try:
        return header.index(city)
    except ValueError:
        return -1

def main():
    filename = "09.Project Distances.csv"
    table = load_distance_table(filename)
    print_distance_table(table)
    
    from_city = input("Enter From City: ").strip()
    to_city = input("Enter To City: ").strip()
    
    city_names = table[0]
    row_index = find_index([row[0] for row in table], from_city)
    col_index = find_index(city_names, to_city)
    
    if row_index == -1:
        print("Invalid From City")
    elif col_index == -1:
        print("Invalid To City")
    else:
        distance = table[row_index][col_index]
        print(f"{from_city} to {to_city} - {distance} miles")

if __name__ == "__main__":
    main()
