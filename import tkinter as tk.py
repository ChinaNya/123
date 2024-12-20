import tkinter as tk
import random
from tkinter import messagebox

# Словарь для хранения логинов и паролей
users = {
    '1': '123',
    '2': '321'
}

# Функция для проверки логина и пароля
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users and users[username] == password:
        login_window.destroy()  # Закрыть окно входа
        create_game_window()     # Создать окно игры
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")

# Функция для определения победителя
def determine_winner(user_choice):
    options = ['Камень', 'Ножницы', 'Бумага']
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "Ничья!"
    elif (user_choice == 'Камень' and computer_choice == 'Ножницы') or \
         (user_choice == 'Ножницы' and computer_choice == 'Бумага') or \
         (user_choice == 'Бумага' and computer_choice == 'Камень'):
        result = "Вы победили!"
    else:
        result = "Компьютер победил!"

    result_label.config(text=f"Компьютер выбрал: {computer_choice}\n{result}")

# Функция для создания окна игры
def create_game_window():
    global result_label

    # Создание основного окна игры
    game_window = tk.Tk()
    game_window.title("Камень, Ножницы, Бумага")
    game_window.configure(bg='gray')  # Установка фона окна игры

    # Создание кнопок для выбора
    rock_button = tk.Button(game_window, text="Камень", command=lambda: determine_winner('Камень'), bg='lightgray')
    rock_button.pack(pady=10)

    scissors_button = tk.Button(game_window, text="Ножницы", command=lambda: determine_winner('Ножницы'), bg='lightgray')
    scissors_button.pack(pady=10)

    paper_button = tk.Button(game_window, text="Бумага", command=lambda: determine_winner('Бумага'), bg='lightgray')
    paper_button.pack(pady=10)

    # Метка для отображения результата
    result_label = tk.Label(game_window, text="", font=("Arial", 14), bg='gray', fg='white')
    result_label.pack(pady=20)

    # Запуск основного цикла игры
    game_window.mainloop()

# Создание окна для входа
login_window = tk.Tk()
login_window.title("Вход")
login_window.configure(bg='gray')  # Установка фона окна входа

# Метки и поля для ввода логина и пароля
tk.Label(login_window, text="Логин:", bg='gray', fg='white').pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

tk.Label(login_window, text="Пароль:", bg='gray', fg='white').pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

# Кнопка для входа
login_button = tk.Button(login_window, text="Войти", command=login, bg='lightgray')
login_button.pack(pady=20)

# Запуск основного цикла
login_window.mainloop()