### Problem 4

def print_triangle(num_rows):
    if num_rows < 0 or not isinstance(num_rows, int):
        return("Invalid input")
    start = 1
    for i in range(num_rows):
        my_list = [x for x in range(start,start+i+1)]
        start = my_list[-1] + 1
        print(*my_list)

print_triangle(-3)
print_triangle(0)
print_triangle(6)
print_triangle(2.3)

