def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    area = 3.14 * radius * radius
    return area

def main():
    radius = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
    area = get_circle_area(radius)
    print("반지름", radius, "인 원의 넓이 = 3.14 x", radius, "x", radius, "=", "{:.2f}".format(area))

main()
