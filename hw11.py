from tkinter import messagebox
import os

class wordMaster:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("단어장")

        self.buildGUI()

        self.words = self.loadData()

    def buildGUI(self):
        l_word = ttk.Label(self.win, text = "단어:")
        self.word = tk.StringVar()
        e_word = ttk.Entry(self.win, textvariable=self.word, width=15)

        l_meaning = ttk.Label(self.win, text="뜻:")
        self.mean = tk.StringVar()
        e_meaning = ttk.Entry(self.win, textvariable=self.mean, width=35)

        b_search = ttk.Button(self.win, text="검색", width=5, command=self.search)
        b_add = ttk.Button(self.win, text="추가", width=5, command=self.add)
        b_reset = ttk.Button(self.win, text="초기화", command=self.reset)
        b_exit = ttk.Button(self.win, text="종료", command=self.exit)

        l_word.grid(row=0, column=0, sticky='e', padx=10)
        e_word.grid(row=0, column=1, sticky='w')
        b_search.grid(row=0, column=2, ipadx=10, ipady=5, sticky='w')
        b_add.grid(row=0, column=3, ipadx=10, ipady=5, sticky='w')

        l_meaning.grid(row=2, column=0, sticky='e', padx=10)
        e_meaning.grid(row=2, column=1, columnspan=3, sticky='w')

        b_reset.grid(row=3, column=0, ipadx=10, ipady=5, padx=10, sticky='w')
        b_exit.grid(row=3, column=1, ipadx=10, ipady=5, sticky='w')

    def loadData(self):
        words = {}
        if not os.path.exists("words.txt") :
            return words
        fp = open("words.txt", "r", encoding="utf-8")

        for line in fp :
            word = line.split(":")
            for i in range(0, len(word)):
                word[i] = word[i].strip()
            key = word[0]
            value = word[1]
            words[key] = value
        fp.close()
        return words

    def add(self):
        w = self.word.get()
        m = self.mean.get()

        self.words[w] = m

        messagebox.showinfo("추가 확인", "단어 " + w + "를 추가했습니다.")

        self.word.set('')
        self.word.set('')

    def search(self):
        w = self.word.get()

        if w not in self.words :
            messagebox.showinfo("검색 오류", w + "란 단어는 없습니다!")
            self.reset()
            return

        m = self.words[w]

        self.mean.set(m)

    def reset(self):
        self.word.set('')
        self.mean.set('')

    def exit(self) :
        fp = open("words.txt", "w", encoding="utf-8")

        for w in self.words.keys():
            m = self.words[w]
            fp.write(w + ":" + m + "\n")

        fp.close()

        self.win.destroy()

wm = wordMaster()
wm.win.mainloop()