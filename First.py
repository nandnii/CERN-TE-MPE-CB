# Function to print Duplicates
def Duplicates(x):
    repeated = []
    for letter in input_list:
        n = input_list.count(letter)
        if n > 1:
            if repeated.count(letter) == 0:
                repeated.append(letter)
    return repeated

if __name__ == "__main__":
    # User input for list
    input_str = input("Enter space seperated list of characters: ")
    input_list = input_str.split(' ')
    input_list = [element.strip() for element in input_list]

    # Default list
    # input_list = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]

    print(Duplicates(input_list))