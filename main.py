def welcome_message():
    user_name = input("Enter your username")
    message = f'Hello { user_name}.Welcome to the conversion app.'
    print(message)


def conversion_type():
    conversions = ['Grade', 'Quantity', 'Length', 'Mass', 'Temperature']
    message = f'Pick a converter that you would like to use out of the following: {conversions}'
    print(message)

    choice = input('Which converter do you want to use?')
    if choice == 'Grade':
        print("Converting form number grade to letter grade")
        grade = input('Enter grade to be converted:')
        grade = int(grade)
        if grade > 100:
            print("Error ....Number too large to be evaluated")
        elif grade >= 80:
            print("A")
        elif grade >= 70:
            print("B")
        elif grade >= 60:
            print("C")
        elif grade >= 40:
            print("D")
        elif grade >= 20:
            print("E")
        elif grade > 0:
            print("F")
        else:
            print("Error ....Number too small to be evaluated")

    elif choice == 'Temperature':
        print('convert temperature from fahrenheit to celsius')
        temp = input('Enter your temperature in fahrenheit')
        temp = int(temp)
        fahrenheit = (temp-30)/2
        print(f'{fahrenheit}F')

    elif choice == 'Mass':
        print('Convert mass from Grams to Ounces')
        mass = input('Enter mass in grams')
        mass = int(mass)
        ounce = mass * 0.03527396195
        print(f'{ounce}oz')


welcome_message()
conversion_type()
