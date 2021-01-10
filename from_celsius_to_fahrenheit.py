# This program was created by Larry Nkengbeza
# This program was created on January of 2021
# This program turns a number from celcius to farenhiet

def celsius_to_fahrenheit():
    # input
    num_str = (input("Enter a number in fahrenheit: "))
    print("")

    # process
    try:
        num = int(num_str)
        tempfahr = (9/5)*num+32

    # output
        print("The temperature in fahrenheit is: {0}". format(tempfahr))
    except Exception:
        print("This is not an integer.")
    finally:
        print("Thanks for using the program.")

def main():
    celsius_to_fahrenheit()


if __name__ == "__main__":
    main()
