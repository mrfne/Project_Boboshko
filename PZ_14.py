# Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).
# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 1 – 9.
# Вариант 3 https://cf.pptonline.org/files/slide/v/vRAlxeaYzgFDVC2krBdPXQtZbW5McoLJ08In6q/slide-21.jpg
import tkinter as tk
from tkinter import ttk

# Задание 1 - Анкета Web-разработчика
class WebDeveloperForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Анкета Web-разработчика")
        self.root.geometry("500x600")

        # Регистрационное имя
        tk.Label(root, text="Регистрационное имя").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.reg_name = tk.Entry(root, width=30)
        self.reg_name.grid(row=0, column=1, padx=10, pady=5)

        # Пароль
        tk.Label(root, text="Пароль").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.password = tk.Entry(root, width=30, show="*")
        self.password.grid(row=1, column=1, padx=10, pady=5)

        # Специализация
        tk.Label(root, text="Ваша специализация").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.spec = ttk.Combobox(root, values=["Web-мастер", "Web-дизайнер", "Frontend", "Backend"], width=27)
        self.spec.set("Web-мастер")
        self.spec.grid(row=2, column=1, padx=10, pady=5)

        # Пол
        tk.Label(root, text="Пол").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.gender = tk.StringVar(value="М")
        tk.Radiobutton(root, text="М", variable=self.gender, value="М").grid(row=3, column=1, sticky="w")
        tk.Radiobutton(root, text="Ж", variable=self.gender, value="Ж").grid(row=3, column=1, padx=40)

        # Навыки
        tk.Label(root, text="Ваши навыки").grid(row=4, column=0, sticky="nw", padx=10, pady=5)
        self.skills = {
            "HTML и CSS": tk.BooleanVar(),
            "Perl": tk.BooleanVar(),
            "ASP": tk.BooleanVar(),
            "Adobe Photoshop": tk.BooleanVar(),
            "JAVA": tk.BooleanVar(),
            "JavaScript": tk.BooleanVar(),
            "Flash": tk.BooleanVar()
        }
        row = 5
        for i, (skill, var) in enumerate(self.skills.items()):
            tk.Checkbutton(root, text=skill, variable=var).grid(row=row + i, column=1, sticky="w", padx=10)

        # Дополнительные сведения
        tk.Label(root, text="Дополнительные сведения о себе").grid(row=12, column=0, sticky="nw", padx=10, pady=5)
        self.info = tk.Text(root, width=40, height=5)
        self.info.grid(row=12, column=1, padx=10, pady=5)

        # Кнопки
        tk.Button(root, text="зарегистрировать", command=self.register).grid(row=13, column=0, pady=20)
        tk.Button(root, text="очистить форму", command=self.clear).grid(row=13, column=1, pady=20)

    def register(self):
        print("Регистрационное имя:", self.reg_name.get())
        print("Пароль:", self.password.get())
        print("Специализация:", self.spec.get())
        print("Пол:", self.gender.get())
        print("Навыки:", [s for s, v in self.skills.items() if v.get()])
        print("Доп. сведения:", self.info.get("1.0", tk.END))

    def clear(self):
        self.reg_name.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.spec.set("Web-мастер")
        self.gender.set("М")
        for var in self.skills.values():
            var.set(False)
        self.info.delete("1.0", tk.END)


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