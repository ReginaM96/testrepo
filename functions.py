# we run into the end of the function and exit
def f():
    print("Hello, world!")
# returns here

# early return from void function
def g(x, y):
    if y == 0:
        print("y can't be 0")
        return # returns here

    print("Calculating...")
    z = (x * x + y * y) / y
    print("The answer is", z)

# return from non-void
def h(firstName, surname):
    f()  # functions can invoke other functions!!
    if firstName == "" or surname == "":
        return "Default Name" # returns here
    return firstName + " " + surname # returns here
