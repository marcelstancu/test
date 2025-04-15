def greet(name):
    print("Hello, " + name)

def add_numbers(a, b):
    return a + b

def main():
    name = "World"
    greet(name)
    result = add_numbers(5, "10")  # Error: Adding integer and string
    print("The result is: " + result)  # Error: Concatenating string and integer

if __name__ == "__main__":
    main()
