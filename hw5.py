def read_single_digit(n) :
    index = ['영','일','이','삼','사','오','육','칠','팔','구']
    if 0 <= n <= 9 :
        return index[n]

def read_number(n) :
    index = ['영','일','이','삼','사','오','육','칠','팔','구']
    if 100 <= n <= 999 :
        n_str = str(n)
        result = ''
        for digit in n_str :
            result += index[int(digit)] +' '
    return result.strip()

n = int(input('세 자리 정수 입력 :'))
print(read_number(n))
