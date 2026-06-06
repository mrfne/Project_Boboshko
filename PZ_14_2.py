# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 1 – 9.
# Вариант 3 https://cf.pptonline.org/files/slide/v/vRAlxeaYzgFDVC2krBdPXQtZbW5McoLJ08In6q/slide-21.jpg
# Задание 2 - Счетчик из ПЗ №9
class CounterApp:
    def __init__(self, root):
        self.counter = 0
        self.window = tk.Toplevel(root)
        self.window.title("Счетчик")
        self.window.geometry("200x150")

        self.label = tk.Label(self.window, text=str(self.counter), font=("Arial", 30))
        self.label.pack(pady=10)

        tk.Button(self.window, text="+", command=self.inc, width=10).pack(pady=5)
        tk.Button(self.window, text="-", command=self.dec, width=10).pack(pady=5)

    def inc(self):
        self.counter += 1
        self.label.config(text=str(self.counter))

    def dec(self):
        self.counter -= 1
        self.label.config(text=str(self.counter))


# Запуск
if __name__ == "__main__":
    root = tk.Tk()
    app = WebDeveloperForm(root)
    tk.Button(root, text="Открыть счетчик", command=lambda: CounterApp(root)).grid(row=14, column=0, columnspan=2, pady=10)
    root.mainloop()
