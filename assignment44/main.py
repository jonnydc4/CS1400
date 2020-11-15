# Put your code here
def isSorted(list):
    #if list is sorted print true
    list_length = len(list)
    if list_length == 0 or list_length == 1:
        return True
    else:
        list_place = 1
        while list_place < list_length:
            if list[list_place] > list[list_place - 1]:
                return True
            else:
                return False
        list_place += 1

# A main for testing your code
def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst), lyst)
    lyst[9] = 3
    print(isSorted(lyst), lyst[8], lyst[9])

main()