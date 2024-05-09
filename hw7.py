Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> shopping_bag=[]
... d={'사과' : 10, '바나나' :  2}
... print('[구입]')
... while True:
...     item = input('상품명?')
...     count = d.get(item)
...     if item == '':
...         break
...     print("수량은? ",count)
...     shopping_bag.append(item)
...     print(f'장바구니에 {item} {count}개가 담겼습니다.\n')
... 
... print(f'\n>>> 장바구니 보기:{d}')
... 
... print("[검색]")
... item = input('장바구니에서 확인하고자 하는 상품은?')
... count = d.get(item)
