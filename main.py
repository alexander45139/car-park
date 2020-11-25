# main program

from datetime import time
import carpark

end = False  # boolean tells program if it should end
park = carpark.carpark(6, 9)  # object from carpark class is created with no. of rows and columns

while not end:
    # display menu of options
    print("1. Reset all spaces in the car park to 'empty'")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit")
    print()

    option = input("Enter your choice: ")  # input from user

    #  accepts choice
    if option != "5":
        if option == "1":
            park.empty()
        elif option == "2":
            park.park_car()
        elif option == "3":
            park.remove_car()
        elif option == "4":
            park.display()
        elif option == "5":
            print("Goodbye")
            time.sleep(2)
            end = True
        else:
            option = ("Invalid choice - please re-enter: ")

    print()
    print()
