while True:
    try:
        num = int(input("Please input a number"))
        print(num)
        break
    except ValueError:
        print('invalid input for number. Please try again')