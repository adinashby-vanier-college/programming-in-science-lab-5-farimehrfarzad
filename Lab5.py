# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n < 1:
        return ""
    
    result = ""
    i = 0
    while i < n:
        if i == 0 or i == n - 1:
            result += "*" * n
        else:
            result += "*" + " " * (n - 2) + "*"
        
        if i != n - 1:
            result += "\n"
        
        i += 1
    
    return result
    
# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += str(j)
        result += "\n"
    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    if n < 1:
        return ""
    
    result = ""
    i = 0
    while i < n:
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        result += spaces + stars
        
        if i != n - 1:
            result += "\n"
        
        i += 1
    
    return result