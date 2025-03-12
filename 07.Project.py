def ParseDegreeString(ddmmss):
    deg_pos = ddmmss.find("°")
    min_pos = ddmmss.find("'")
    sec_pos = ddmmss.find('"')
    deg = ddmmss[0:deg_pos]
    mins = ddmmss[deg_pos+1:min_pos]
    secs = ddmmss[min_pos+1:sec_pos]
    deg = float(deg)
    mins = float(mins)
    secs = float(secs)
    return deg, mins, secs

def DDMMSStoDecimal(deg, mins, secs):
    decimal_deg = deg + (mins / 60) + (secs / 3600)
    return decimal_deg

def process_file(input_file, output_file):
    infile = open(input_file, "r")
    outfile = open(output_file, "w")
    count = 0
    for line in infile:
        line = line.strip()
        if line:
            deg, mins, secs = ParseDegreeString(line)
            decimal_deg = DDMMSStoDecimal(deg, mins, secs)
            outfile.write(str(decimal_deg) + "\n")
            count += 1
    infile.close()
    outfile.close()
    print(f"{count} records processed")

input_file = "07.Project Angles Input.txt"
output_file = "07.Project Angles Output.txt"
process_file(input_file, output_file)