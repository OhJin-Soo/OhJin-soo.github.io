shopping_bag=[]
d={'샌드위치' : 10, '주스' :  5}
print('[구입]')
while True:
    item = input('상품명?')
    count = d.get(item)
    if item == '':
         break
    print("수량은? ",count)
    shopping_bag.append(item)
    print(f'장바구니에 {item} {count}개가 담겼습니다.\n')
 
print(f'\n>>> 장바구니 보기:{d}')
 
print("[검색]")
item = input('장바구니에서 확인하고자 하는 상품은?')
if  item != "샌드위치" and item != "주스":
        print(f"장바구니에 {item}은(는) 없습니다.")
else:
        count = d.get(item)
        print(f"{item}(는) {count}개 담겨있습니다.")
