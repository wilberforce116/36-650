### Problem 5

def print_pyramid(num_rows):
    if num_rows < 0 or not isinstance(num_rows, int):
        return("Invalid input")

    for i in range(num_rows):
        print(" "*(num_rows - (i+1)) + "*" + " *"*i + " "*(num_rows - (i+1)))


print_pyramid(-3)
print_pyramid(0)
print_pyramid(6)
print_pyramid(2.3)

