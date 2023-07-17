if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit ")
        print(" ")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            num_string = input("Please enter your password to encode: ")
            a = encoder(num_string)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            b = decoder(a)
            print(f"The encoded password is {a}, and the original password is {b}. ")
        elif choice == 3:
            break