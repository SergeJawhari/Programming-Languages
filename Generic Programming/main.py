# This main function will take advantage of the generic sorted() function to sort lists and tuples dynamically by defining values within the function's parameters. The sorted() function can be used to sort nearly anything, as long as the provided logic is fulfilled within its parameters.
def main():

    # This is the list of Numbers that are to be sorted for the first sort.
    numList = [645.41, 37.59, 76.41, 5.31, -34.23, 1.11, 1.10, 23.46, 635.47, -876.32, 467.83, 62.25]

    # This is the list of Tuples that are to be sorted two different ways.
    peopleList = [
        ('Hal', 20), ('Susann', 31), ('Dwight', 19), ('Kassandra', 21), ('Lawrence', 25), 
        ('Cindy', 22), ('Cory', 27), ('Mac', 19), ('Romana', 27), ('Doretha', 32),
        ('Danna', 20), ('Zara', 23), ('Rosalyn', 26), ('Risa', 24), ('Benny', 28),
        ('Juan', 33), ('Natalie', 25)]

    # This function will call the sorted() method to conduct an automatic sort on floats values.
    sortedNumbers = sorted(numList)

    # This function will call the sorted() method to conduct an automatic sort on string values.
    sortedByNames = sorted(peopleList)

    # This function will call the sorted() method with a nested sorted() method inside of it, to sort each tuple. First the tuple will be sorted by the person's name in the nested sort, via personName[0], then the outer sort will sort the list by the person's ages, via personAge[1].
    sortedByAgeAndNames = sorted(sorted(peopleList, key = lambda personName: personName[0]), key = lambda personAge: personAge[1], reverse = True)

    # prints the sorted list of numbers.
    print("============= Numbers Sorted =============")
    print(*sortedNumbers, sep="\n")
    print("\n")

    # prints the sorted tuples of people by name.
    print("============= Names Sorted =============")
    print(*sortedByNames, sep="\n")
    print("\n")

    # prints the sorted tuples of people in priority of age, and then by name, respectively.
    print("============= Sorted by priority of Age>Name =============")
    print(*sortedByAgeAndNames, sep="\n")
    print("\n")

# This if statement will invoke the main method define above.
if __name__=="__main__": 
    main() 