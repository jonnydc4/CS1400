# Put your code here
def average(x, y):
    ave = x / y
    print(ave)

def convert_to_int(text_file):
    file = open(text_file,'r')

    count = 0
    sum = 0

    for line in file:
        line.rstrip('\n')
        str_numbers = line.split(" ")

        for numberStr in str_numbers:
            count += 1
            sum += float(numberStr)
    average(sum, count)
    file.close()

convert_to_int('numbers.txt')