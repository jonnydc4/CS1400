
def diffTwoFiles(filename1, filename2):

    # compare file contents
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')

    file1_contents = file1.read()
    file2_contents = file2.read()

    if file1_contents == file2_contents:
        print("Yes")
    else:
        print("No")
        file1_array = file1_contents.split("\n")
        file2_array = file2_contents.split("\n")
        for line_number in range(max(len(file1_array), len(file2_array))):
            # print(line_number)
            if line_number > len(file1_array) - 1:
                x = 1
                # print('no line in file 1')
            elif line_number > len(file2_array) - 1:
                x = 2
                # print('no line in file 2')
            elif file1_array[line_number] == file2_array[line_number]:
                x = 3
                # print('lines are the same')
            else:
                print(file1_array[line_number])
                print(file2_array[line_number])
                exit()


    # for line1 in open_file1
    #     f.read(line)
    #
    # for line2 in open_file2
    #     f.readline(line)
    # if
    #


    # print yes if the same
# else print no and the differences

# prompt user for 1st file
#file1 = input("Enter first file name: ")
# prompt user for 2nd file
#file2 = input("Enter second file name: ")

diffTwoFiles('file1.txt', 'file2.txt')