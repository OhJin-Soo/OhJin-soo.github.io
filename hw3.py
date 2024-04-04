def get_fixed_price(result):
    return result

rate = int(input("할인율은? "))
unit1 = int(input("A 상품의 할인된 가격은? "))
unit2 = int(input("B 상품의 할인된 가격은? "))

result1 = get_fixed_price(unit1 / ((1-(0.01*rate))))
result2 = get_fixed_price(unit2 / ((1-(0.01*rate))))

print("A 상품의 정가는 " + str(int(result1)) + " 원")
print("B 상품의 정가는 " + str(int(result2)) + " 원")
