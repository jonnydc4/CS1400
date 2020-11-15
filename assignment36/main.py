def main(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for loop in range(100):
            print("The file has", len(lines),"lines.")
            x = int(input("Enter a line number[0 to quit]: "))
            if x > len(lines):
                print("Error: Line must be less than", len(lines))
                continue
            elif x == 0:
                quit()
            else:
                print(lines[(x-1)])
main("test_file.txt")
