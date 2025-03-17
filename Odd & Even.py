try:
    # Collect input from the user
    n = int(input("Enter an integer between 1 and 100: "))

    # Check if the input is within the valid range
    if 1 <= n <= 100:
        if n % 2 != 0:
            print("Weird")
        else:
            if 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
            elif n > 20:
                print("Not Weird")
    else:
        print("Please enter a number between 1 and 100.")

except ValueError:
    print("Please enter a valid integer.")