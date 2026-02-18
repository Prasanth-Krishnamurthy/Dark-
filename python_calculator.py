def student_calculator():
    try:
        first = float(input("Enter first value: "))
        op = input("Choose operator (+, -, *, /, //, %, **): ")
        second = float(input("Enter second value: "))

        if op == "+":
            answer = first + second
        elif op == "-":
            answer = first - second
        elif op == "*":
            answer = first * second
        elif op == "/":
            if second == 0:
                raise ZeroDivisionError
            answer = first / second
        elif op == "//":
            if second == 0:
                raise ZeroDivisionError
            answer = first // second
        elif op == "%":
            if second == 0:
                raise ZeroDivisionError
            answer = first % second
        elif op == "**":
            answer = first ** second
        else:
            raise ValueError

        print("Your Answer is:", answer)

    except ValueError:
        print("Invalid input! Please enter numbers and correct operator.")
        return student_calculator()

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
        return student_calculator()

    except KeyboardInterrupt:
        print("\nCalculator stopped by user.")
        return

student_calculator()
