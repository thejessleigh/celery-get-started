class NumericalInputError(Exception):
    pass


while True:
    try:
        num = input("Please input a number")
        if not num.isdigit():
            raise NumericalInputError()
        print(num)
        break
    except NumericalInputError:
        print('invalid input for number. Please try again')
    finally:
        print("Heyo! We've completed a full cycle")