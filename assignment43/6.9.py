# Put your code here
def average(x, y):
    ave = x / y
    print(ave)

def convert_to_int(text_file):
    file = open(text_file,'r')

    for line in file:
        x = 0
        count = 0
        sum = 0
        line.rstrip('\n')
        str_numbers = line.split(" ")

        for number in str_numbers:
            number = float(str_numbers[x])
            x += 1
            count += 1
            sum += number
            print(number)
    file.close()

convert_to_int('numbers.txt')



