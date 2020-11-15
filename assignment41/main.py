import math

def root_estimator(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break

    # Output the result
    print("The program's estimate is", estimate)
    print("Python's estimate is", math.sqrt(x))


while True:
    y = input("Enter a positive number or enter/return to quit: ")
    try:
        root_estimator(float(y))
    except:
        exit(0)
