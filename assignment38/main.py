def alphabetizer(filename):
    file = open(filename, 'r')
    contents = file.read()
    words = contents.split(" ")
    print(sorted(words))

alphabetizer('example.txt')