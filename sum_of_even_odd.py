#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# This program calculate the sum of even and odd numbers based on user's choice


def main():
    while True:
        # Declaring variables
        counter = 0
        even_sum_list = []
        odd_sum_list = []

        # Ask user how much number they want to add up
        user_input = input("How many numbers would you like to enter?: ")

        try:
            # Casting to int
            user_input_as_int = int(user_input)
            # Check if the input is a positive number
            if user_input_as_int <= 0:
                print(
                    "Invalid number. You cannot input a negative number.\nPlease input a positive number."
                )
                break

        except:
            # If the user enters a invalid input
            print("Invalid number. Please input a positive number.")
            break

        while counter < user_input_as_int:

            # Ask user to input their number
            user_num = input("Enter a number: ")

            try:
                # Casting to int
                user_num_as_int = int(user_num)

                # Check if the input is a positive number
                if user_num_as_int <= 0:
                    print(
                        "Invalid number. You cannot input a negative number.\nPlease input a positive number."
                    )
                    continue
                if user_num_as_int % 2 == 0:
                    # Add even number to list
                    even_sum_list.append(user_num_as_int)
                else:
                    # Add odd number to list
                    odd_sum_list.append(user_num_as_int)

                # Add the user number to the total sum
                # total_sum += user_num_as_int
                counter += 1

            except:
                # If the user enters a invalid input
                print("Invalid number. Please input a positive number.")

        # Calculating the sum of the even numbers
        total_sum_even = sum(even_sum_list)

        # Calculating the sum of the odd numbers
        total_sum_odd = sum(odd_sum_list)

        # Display total sum of even numbers
        print("The total sum of the even numbers is {}.".format(total_sum_even))
        print(*even_sum_list, sep=" + ", end=" ")
        print("= {}".format(total_sum_even))
        print("")

        # Display total sum of odd numbers
        print("The total sum of the odd numbers is {}.".format(total_sum_odd))
        print(*odd_sum_list, sep=" + ", end=" ")
        print("= {}".format(total_sum_odd))

        break


if __name__ == "__main__":
    main()
