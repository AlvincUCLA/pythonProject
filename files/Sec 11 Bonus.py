try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))
    if width == length:
        print("It looks like a square instead of a rectangle.")

    else:
        area = width * length
        print("The area of the rectangle is: ", area)

except ValueError:
    print("Please enter a number!")
