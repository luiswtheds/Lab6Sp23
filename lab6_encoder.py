#Luis Cabrera

def encode(phrase):
    #iterate through numbers in phrase string to encode
    result = ''
    for i in phrase:
        i = int(i) + 3
        i = str(i)[-1]
        result += f"{i}"
    return result


def decode(phrase):
    #decodes whatever is inputted with option 1-neha bangalore
    result = ''
    for i in phrase:
        i = int(i) - 3
        if i < 0:
            i += 10
        result += f"{i}"
    return result


def main():
    #looping menu
    option = 1
    phrase = ''
    while option != 0:
        #print menu
        print("0. Exit")
        print("1. Enter  new phrase")
        print("2. Print encoded phrase")
        print("3. Print decoded phrase")
        option = int(input("Enter an option: "))

        if option == 1:
            phrase = input('Enter your phrase: ')
        elif option == 2:
            print('Encoded phrase is', encode(phrase))
        elif option == 3:
            print('Decoded phrase is', decode(phrase))


if __name__ == "__main__":
    main()
