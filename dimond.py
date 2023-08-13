def print_hollow_diamond(n):
    # Printing the upper triangle
    for rows in range(1, n + 1):
        print(" " * (n - rows), end="")
        print("*", end="")

        if rows > 1:
            print(" " * ((rows - 1) * 2 - 1), end="")
            print("*", end="")
        print()

    # Printing the lower triangle
    for rows in range(n - 1, 0, -1):
        print(" " * (n - rows), end="")
        print("*", end="")

        if rows > 1:
            print(" " * ((rows - 1) * 2 - 1), end="")
            print("*", end="")
        print()

# Size of the diamond pattern
n = 5
print_hollow_diamond(n)
