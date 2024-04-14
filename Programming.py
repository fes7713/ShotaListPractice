
def function2(value):
    return value

def function1(value):
    value = function2(value)

    a = value + 1
    return a

if __name__ == "__main__":
    array = []

    numbers = [1, 2, 3, 4, 5, 6]

    numbers.append(1)

    print(numbers)

    data = {"CheesesCake": "Yummy", "ChocolateCake": 220, "PlainCake": "120", "StroberryCake": 250}

    print(data["CheesesCake"])


    print(numbers.pop())

    print(function1(1))

