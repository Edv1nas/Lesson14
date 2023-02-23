while True:
    firstnumber_raw = input("Enter your first number:\n")
    try:
        firstnumber = float(firstnumber_raw)
    except ValueError:
        print(firstnumber_raw, "' is not a valid number, try again.")
    else:
        break