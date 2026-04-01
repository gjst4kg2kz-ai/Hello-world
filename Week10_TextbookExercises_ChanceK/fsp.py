from breezypythongui import EasyFrame

class CounterDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Counter Demo")
        self.counter = 0
        self.label = self.addLabel(text=str(self.counter), row=0, column=0, columnspan=2)
        self.addButton(text="Next", row=1, column=0, command=self.next)
        self.addButton(text="Reset", row=1, column=1, command=self.reset)

    def next(self):
        self.counter += 1
        self.label["text"] = str(self.counter)

    def reset(self):
        self.counter = 0
        self.label["text"] = str(self.counter)

def main():
    CounterDemo().mainloop()

if __name__ == "__main__":
    main()
