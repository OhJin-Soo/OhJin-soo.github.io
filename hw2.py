def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(n, unit):
    count = n // unit
    return count

n = get_integer("동전으로 교환하고자 하는 금액은? ")
n1 = exchange(n, 500)
n -= n1 * 500
n2 = exchange(n, 100)
n -= n2 * 100
n3 = exchange(n, 50)
n -= n3 * 50
n4 = exchange(n, 10)

print("500원 동전의 개수는? ", n1)
print("100원 동전의 개수는? ", n2)
print("50원 동전의 개수는? ", n3)
print("10원 동전의 개수는? ", n4)
