#!/usr/bin/env python3
# Created by: Joyceline .
# Created on: November 6 2026
# This program asks the user for a positive integer, then uses a while loop
# to calculate and display the sum of all whole numbers from 0 up to that number.
# It also includes input validation to prevent crashes from invalid text or decimals.


def main():

    counter = 0
    total_number = 0

    # Get the user input as a string
    user_number_as_string = input("Enter a positive integer: ")
    print("")

    # Try to catch invalid inputs like text or decimals
    try:
        user_number_int = int(user_number_as_string)

        # Check if the entered integer is valid (greater than 0)
        if user_number_int < 0:
            print("User number is an invalid integer.")

        # If the user enters 0, the sum is 0
        elif user_number_int == 0:
            print(f"The sum of total numbers from 0 to {user_number_int} is {total_number}.")

        # If it's a valid positive integer, run the while loop
        else:
            while counter < user_number_int:
                counter = counter + 1
                print(f"Tracking {counter} time(s) through the loop.")
                total_number = total_number + counter

            # Display the final result after the loop has completed
            print("")
            print(
                f"The sum of total numbers from 0 to {user_number_int} is {total_number}."
            )

    except:
        print(f"'{user_number_as_string}' is an invalid integer.")


if __name__ == "__main__":
    main()
