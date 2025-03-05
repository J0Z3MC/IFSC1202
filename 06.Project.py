def merge_files(input_file, merge_file, output_file):
    input_records = 0
    merge_records = 0
    output_records = 0
    insert_marker = '**Insert Merge File Here**'

    with open(output_file, 'w') as output:
        with open(input_file, 'r') as input:
            input_lines = input.readlines()
            for line in input_lines:
                input_records += 1
                output.write(line)
                if insert_marker in line:
                    with open(merge_file, 'r') as merge:
                        merge_lines = merge.readlines()
                        for merge_line in merge_lines:
                            merge_records += 1
                            output.write(merge_line)

        for line in input_lines:
            output_records += 1
            output.write(line)

    print(f'{input_records} input file records')
    print(f'{merge_records} merge file records')
    print(f'{output_records} output file records')

input_file = '06.Project Input File.txt'
merge_file = '06.Project Merge File.txt'
output_file = '06.Project Output File.txt'

merge_files(input_file, merge_file, output_file)