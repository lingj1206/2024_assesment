import math


def num_check(question, error, num_type):
    while True:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def shape(question, shape_list):
    error = "Please choose one of the following shapes: cube, cuboid, sphere, cylinder or square based pyramid"

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in shape_list:
            if response == item:
                return item

        print(error)


def cube(length):
    volume = length ** 3
    surface_area = length ** 2 * 6
    return f'Volume is: {volume}, Surface area is: {surface_area}'


def cuboid(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)
    return f"volume is: {volume}, Surface area is: {surface_area}"


def cylinder(radius, height):
    volume = 3.14159 * radius ** 2 * height
    surface_area = 2 * 3.14159 * radius * height + 2 * 3.14159 * radius * radius
    return f"volume is: {volume}, Surface area is: {surface_area}"


def sphere(radius):
    volume = 1.333 * 3.14159 * radius ** 3
    surface_area = 4 * 3.14159 * radius * radius
    return f"volume is: {volume}, Surface area is: {surface_area}"


# def sq_pyramid(length, height):
#     volume =
#     surface_area =
#     return f"volume is: {volume}, Surface area is: {surface_area}"



shape_list = ["cube", "cuboid", "sphere", "cylinder", "square pyramid", "xxx"]

while True:
    random_shape = shape("pick a shape: ", shape_list)

    if random_shape == "xxx":
        break

    elif random_shape == "cube":
        length = num_check("what is the length: ", "please enter a positive integer", float)
        result = cube(length)

    elif random_shape == "cuboid":
        length = num_check("what is the length: ", "please enter a positive integer", float)
        width = num_check("what is the width: ", "please enter a positive integer", float)
        height = num_check("what is the height: ", "please enter a positive integer", float)
        result = cuboid(length, width, height)

    print(result)
