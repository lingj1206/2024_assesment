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
    volume = length * length * length
    surface_area = length * length * 6
    return f'Volume is: {volume}, Surface area is: {surface_area}'


def cuboid(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)
    return f"volume is: {volume}, Surface area is: {surface_area}"


shape_list = ["cube", "cuboid", "sphere", "cylinder", "square based pyramid", "xxx"]

while True:
    random_shape = shape("pick a shape: ", shape_list)

    if random_shape == "cube":
        length = num_check("what is the length: ", "please enter ea positive integer", int)
        result = cube(length)



    print(result)
