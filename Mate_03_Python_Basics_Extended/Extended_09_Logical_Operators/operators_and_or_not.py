# Operators: and, or, not
x = 1
y = 2

if x == 1 and y == 2:
    print('x = 1, y = 2')

if x == 1 or y == 2:
    print('x = 1, y = 2')

if x == 1 and (y == 1 or y == 2):
    print('x = 1, y = 2')

if not x == 2:
    print('x = 1, y = 2')
print('--------------------------------')

# ternary operator
age = 18
ternary = "Adult" if age >= 18 else "Child"
print(ternary)
