import tkinter as tk
from logic import generate_interval, check_answer, replay_interval, INTERVALS

# Tworzenie okna GUI
window = tk.Tk()
window.title("Ear Training")
window.geometry("300x400")
window.configure(bg="#9A9ACD")

score = [0]

def new_interval():
    interval_name = generate_interval()
    correct_interval.set(interval_name)

def submit_answer():
    user_interval = interval_var.get()
    correct_interval_name = correct_interval.get()

    if check_answer(user_interval, correct_interval_name):
        score[0] += 2
        score_label.config(text=f"Wynik: {score[0]}", fg="green")
    else:
        score[0] -= 3
        score_label.config(text=f"Wynik: {score[0]}", fg="red")
    new_interval()

# Tworzenie widżetów GUI
question_label = tk.Label(window, text="Jaki to interwał?", bg="#9A9ACD", fg="white", font=("Arial", 16))
question_label.pack()

interval_var = tk.StringVar()
interval_optionmenu = tk.OptionMenu(window, interval_var, *INTERVALS.keys())
interval_optionmenu.config(width=20)
interval_optionmenu.pack()

check_button = tk.Button(window, text="Sprawdź", command=submit_answer, bg="#9A9ACD", fg="white", font=("Arial", 14), relief="solid")
check_button.pack(pady=10)

replay_button = tk.Button(window, text="Odtwórz ponownie", command=replay_interval, bg="#9A9ACD", fg="white", font=("Arial", 14), relief="solid")
replay_button.pack(pady=5)

new_interval_button = tk.Button(window, text="Nowy interwał", command=new_interval, bg="#9A9ACD", fg="white", font=("Arial", 14), relief="solid")
new_interval_button.pack(pady=5)

score_label = tk.Label(window, text="Wynik: 0", fg="black", bg="#9A9ACD", font=("Arial", 14))
score_label.pack(side="top")

correct_interval = tk.StringVar()

new_interval()
window.mainloop()
