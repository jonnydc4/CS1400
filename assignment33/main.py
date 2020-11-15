# from tabulate import tabulate

def payroll(file_name):
    file = open(file_name, 'r')
    file_contents = file.read()
    lines = file_contents.split("\n")

    # print header
    header = ["Name", "Hours", "Total Pay"]
    print("\t\t".join(header))

    for lineNumber in range(len(lines)):
        line_variables = lines[lineNumber].split(" ")
        totalPay = float(line_variables[1]) * float(line_variables[2])
        printArray = [
            line_variables[0],
            line_variables[1],
            str(totalPay)
            ]
        print("\t".join(printArray))



    # print(tabulate([[file_array[0], file_array[1], file_array[2]],
    #                 [file_array[3], file_array[4], file_array[5]],
    #                 [file_array[6], file_array[7], file_array[8]]],
    #                 headers = ["Name", "Hours", "Total Pay"]))

payroll('data.txt')