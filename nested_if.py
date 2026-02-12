n=int(input())
if n>=18:
    print("Adult")
    if n>=21:
        print("Run for candidate")
    else:
        print("Cannot run for candidate")
else:
    print("Not an adult")