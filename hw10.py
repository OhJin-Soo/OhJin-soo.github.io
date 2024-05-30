import pickle
import os

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = sum(s)
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_scores(filename, scores):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            scores = pickle.load(f)
        return scores
    return None

def main():
    filename = 'score.bin'
    scores = load_scores(filename)
    
    if scores is None:
        print('[점수 입력]')
        scores = input_scores()
    else:
        print('[파일 읽기]')
    
    print('\n[점수 출력]')
    print('개인점수: ', end='')
    show_scores(scores)
    
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')
    
    if scores is not None:
        save_scores(filename, scores)

def search(lst, n):
    if n not in lst:
        return None
    return lst.index(n)

if __name__ == '__main__':
    main()
