import customtkinter as ctk
from tkinter import messagebox
import string
import random


ctk.set_appearance_mode("Light") 
  
ctk.set_default_color_theme("blue") 

# калькулятор
def calc():
    app = ctk.CTk()
    app.title('Калькулятор')
    app.geometry('370x460')
    app.resizable(False, False)
    w = app.winfo_screenwidth()
    h = app.winfo_screenheight()
    w = w//2
    h = h//2 
    w = w - 185
    h = h - 230
    app.geometry('370x460+{}+{}'.format(w, h))
    def calcular():
        calcuator = output.get('0.0', 'end')
        result = eval(calcuator)
        output.delete('0.0', 'end')
        output.insert('0.0', result)
    FontApp = ('Poppins',20,'bold')

    output = ctk.CTkTextbox(app, width=340, height=60,corner_radius=10, border_width=2, border_color='#3F4143', font=FontApp)
    output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)


    button_1 = ctk.CTkButton(app,text='1', command= lambda:output.insert('end', 1), corner_radius=10, width=80, height=55, font=FontApp)
    button_1.grid(row=1, column=0, padx=5, pady=5)


    button_2 = ctk.CTkButton(app,text='2', command= lambda:output.insert('end', 2), corner_radius=10, width=80, height=55, font=FontApp)
    button_2.grid(row=1, column=1, padx=5, pady=5)


    button_3 = ctk.CTkButton(app,text='3', command=lambda:output.insert('end', 3), corner_radius=10, width=80, height=55, font=FontApp)
    button_3.grid(row=1, column=2, padx=5, pady=5)


    button_4 = ctk.CTkButton(app,text='4', command=lambda:output.insert('end', 4), corner_radius=10, width=80, height=55, font=FontApp)
    button_4.grid(row=2, column=0, padx=5, pady=5)


    button_5 = ctk.CTkButton(app,text='5', command=lambda:output.insert('end', 5), corner_radius=10, width=80, height=55, font=FontApp)
    button_5.grid(row=2, column=1, padx=5, pady=5)


    button_6 = ctk.CTkButton(app,text='6', command=lambda:output.insert('end', 6), corner_radius=10, width=80, height=55, font=FontApp)
    button_6.grid(row=2, column=2, padx=5, pady=5)


    button_7 = ctk.CTkButton(app,text='7', command=lambda:output.insert('end', 7), corner_radius=10, width=80, height=55, font=FontApp)
    button_7.grid(row=3, column=0, padx=5, pady=5)


    button_8 = ctk.CTkButton(app,text='8', command=lambda:output.insert('end', 8), corner_radius=10, width=80, height=55, font=FontApp)
    button_8.grid(row=3, column=1, padx=5, pady=5)


    button_9 = ctk.CTkButton(app,text='9', command=lambda:output.insert('end', 9), corner_radius=10, width=80, height=55, font=FontApp)
    button_9.grid(row=3, column=2, padx=5, pady=5)


    button_0 = ctk.CTkButton(app, text='0', command=lambda:output.insert('end', 0) , corner_radius=10, width=80, height=55, font=FontApp)
    button_0.grid(row=4, column=0, padx=5, pady=5)

    button_dot = ctk.CTkButton(app, text='.', command=lambda:output.insert('end', '.'), corner_radius=10, width=80, height=55, font=FontApp)
    button_dot.grid(row=5, column=0, padx=5, pady=6)

    button_degree2 = ctk.CTkButton(app, text='x²', command=lambda:output.insert('end', '**2'), corner_radius=10, width=80, height=55, font=FontApp)
    button_degree2.grid(row=5, column=1, padx=5, pady=5)

    button_degree3 = ctk.CTkButton(app, text='x³', command=lambda:output.insert('end', '**3'), corner_radius=10, width=80, height=55, font=FontApp)
    button_degree3.grid(row=5, column=2, padx=5, pady=5)

    button_degree = ctk.CTkButton(app, text='xʸ', command=lambda:output.insert('end', '**'), corner_radius=10, width=80, height=55, font=FontApp)
    button_degree.grid(row=5, column=3, padx=5, pady=5)

    button_fract = ctk.CTkButton(app, text='x/2', command=lambda:output.insert('end', '/2'), corner_radius=10, width=80, height=55, font=FontApp)
    button_fract.grid(row=6, column=0, padx=5, pady=5)

    button_pm = ctk.CTkButton(app, text='+/-', corner_radius=10, width=80, height=55, font=FontApp,
                              command=lambda:output.delete('1.0', '1.1') if '-' in output.get('1.0') else output.insert('1.0', '-'))
    button_pm.grid(row=6, column=1, padx=5, pady=5)

    button_delete = ctk.CTkButton(app,text='C', command=lambda:output.delete('0.0', 'end'), corner_radius=10, width=80, height=55, font=FontApp)
    button_delete.grid(row=4, column=1, padx=5, pady=5)

    button_backspace = ctk.CTkButton(app, text='<', corner_radius=10, width=80, height=55, font=FontApp,
                                    command=lambda:output.delete(f"1.{len(output.get('1.0', 'end-1c')) - 1}"))
    button_backspace.grid(row=6, column=2, padx=5, pady=5)

    button_calculator = ctk.CTkButton(app,text='=', command=calcular, corner_radius=10, width=80, height=55, font=FontApp)
    button_calculator.grid(row=4, column=2, padx=5, pady=5)

    button_leave = ctk.CTkButton(app, text='Back', corner_radius=10, width=80, height=55, font=FontApp,
                                 command=lambda:app.destroy())
    button_leave.grid(row=6, column=3, padx=5, pady=5)

    button_sum = ctk.CTkButton(app,text='+', command=lambda:output.insert('end', '+'),fg_color="#EA5738",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=FontApp)
    button_sum.grid(row=1, column=3, padx=5, pady=5)


    button_s = ctk.CTkButton(app,text='-', command=lambda:output.insert('end', '-'),fg_color="#EA5738",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=FontApp)
    button_s.grid(row=2, column=3, padx=5, pady=5)


    btn_multip = ctk.CTkButton(app,text='x', command=lambda:output.insert('end', '*'),fg_color="#EA5738",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=FontApp)
    btn_multip.grid(row=3, column=3, padx=5, pady=5)


    button_divide = ctk.CTkButton(app,text='/', command=lambda:output.insert('end', '*'),fg_color="#EA5738",hover_color="#EA5738", corner_radius=10, width=80, height=55, font=FontApp)
    button_divide.grid(row=4, column=3, padx=5, pady=5)

    app.mainloop()
# генератор паролей
def pwgen():
    pwgen = ctk.CTk()
    pwgen.title('Генератор паролей')
    pwgen.geometry('400x330')
    pwgen.resizable(False, False)
    w = pwgen.winfo_screenwidth()
    h = pwgen.winfo_screenheight()
    w = w//2
    h = h//2 
    w = w - 200
    h = h - 165
    pwgen.geometry('400x330+{}+{}'.format(w, h))

    def generate_password():
        result_entry.configure(state='normal')
        result_entry.delete(0, 'end')
        try:
            length = int(length_entry.get())
            characters = ""
            
            if include_letters_var.get():
                characters += string.ascii_letters
            if include_digits_var.get():
                characters += string.digits
            if include_symbols_var.get():
                characters += string.punctuation

            if not characters:
                error1 = ctk.CTk()
                error1.title('Ошибка')
                error1.geometry('200x150')
                error1.resizable(False, False)
                w = error1.winfo_screenwidth()
                h = error1.winfo_screenheight()
                w = w//2
                h = h//2 
                w = w - 100
                h = h - 75
                error1.geometry('200x150+{}+{}'.format(w, h))
                label = ctk.CTkLabel(error1, text="Выберите хотя бы один\nтип символов")
                label.place(x=27, y=50)
                def cancel1():
                    error1.destroy()
                cancel_button = ctk.CTkButton(error1, text='Закрыть', text_color='black', corner_radius=12, border_width=2, border_color='dim gray', command=cancel1)
                cancel_button.place(x=31, y=105)
                error1.mainloop()           
            password = ''.join(random.choice(characters) for _ in range(length))
            result_entry.insert(0, password)
            result_entry.configure(state='readonly')
        except ValueError:
            error = ctk.CTk()
            error.title('Ошибка')
            error.geometry('200x150')
            error.resizable(False, False)
            w = error.winfo_screenwidth()
            h = error.winfo_screenheight()
            w = w//2
            h = h//2 
            w = w - 100
            h = h - 75
            error.geometry('200x150+{}+{}'.format(w, h))
            label = ctk.CTkLabel(error, text="Введите корректное число\nдля длины\nпароля")
            label.place(x=18, y=50)
            def cancel():
                error.destroy()
            cancel_button = ctk.CTkButton(error, text='Закрыть', text_color='black', corner_radius=12, border_width=2, border_color='dim gray', command=cancel)
            cancel_button.place(x=31, y=105)
            error.mainloop()

    def clear():
        result_entry.configure(state='normal')
        result_entry.delete(0, 'end')
    title_label = ctk.CTkLabel(pwgen, text="Генератор паролей", font=ctk.CTkFont(size=20, weight="bold"))
    title_label.pack(pady=10)

    length_label = ctk.CTkLabel(pwgen, text="Длина пароля:")
    length_label.pack()

    length_entry = ctk.CTkEntry(pwgen)
    length_entry.pack(pady=5)

    include_letters_var = ctk.BooleanVar(value=True)
    include_letters_check = ctk.CTkCheckBox(pwgen, text="Буквы (a-z, A-Z)", checkbox_width=20, checkbox_height=20,  variable=include_letters_var)
    include_letters_check.place(x=130, y=115)

    include_digits_var = ctk.BooleanVar(value=True)
    include_digits_check = ctk.CTkCheckBox(pwgen, text="Цифры (0-9)", checkbox_width=20, checkbox_height=20, variable=include_digits_var)
    include_digits_check.place(x=130, y=140)

    include_symbols_var = ctk.BooleanVar(value=True)
    include_symbols_check = ctk.CTkCheckBox(pwgen, text="Спецсимволы (!@#$ и т.д.)", checkbox_width=20, checkbox_height=20, variable=include_symbols_var)
    include_symbols_check.place(x=130, y=165)

    lbl_output = ctk.CTkLabel(pwgen, text='Сгенерированный пароль:', font=('Calibri', 16))
    lbl_output.place(x=110, y=265)

    clear_button = ctk.CTkButton(pwgen, text='Очистить', fg_color=("#DB3E39", "#821D1A"), width=15, border_color='dim gray', corner_radius=12, border_width=2, command=clear)
    clear_button.place(x=200, y=250, anchor='center')
    generate_button = ctk.CTkButton(pwgen, text="Сгенерировать", border_color='dim gray', corner_radius=12, border_width=2, command=generate_password)
    generate_button.place(x=130, y=200)

    result_entry = ctk.CTkEntry(pwgen, width=395,)
    result_entry.place(x=3, y=295)

    pwgen.mainloop()

# информация
def info():
    info = ctk.CTk()
    info.title('Информация')
    info.geometry('500x500')
    info.resizable(False, False)
    w = info.winfo_screenwidth()
    h = info.winfo_screenheight()
    w = w//2
    h = h//2 
    w = w - 250
    h = h - 250
    info.geometry('500x500+{}+{}'.format(w, h))

    

    info.mainloop()

# игра    
def game():
    game = ctk.CTk()
    game.title('Крестики-Нолики')
    game.geometry('270x270')
    game.resizable(False, False)
    w = game.winfo_screenwidth()
    h = game.winfo_screenheight()
    w = w//2
    h = h//2 
    w = w - 135
    h = h - 135
    game.geometry('270x270+{}+{}'.format(w, h))
    global current_player
    current_player = 'X'
    board = [["" for _ in range(3)] for _ in range(3)]

    def check_winner():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != "":
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        return None

    def button_click(row, col):
        global current_player
        if board[row][col] == "" and not check_winner():
            board[row][col] = current_player
            buttons[row][col].configure(text=current_player)
            winner = check_winner()
            if winner:
                messagebox.showinfo("Победа!", f"Победил {winner}")
                game.destroy()
            elif all(board[i][j] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Ничья", "Ничья!")
                game.destroy()
            else:
                current_player = "O" if current_player == "X" else "X"

    def reset_board():
        global board, current_player
        board = [["" for _ in range(3)] for _ in range(3)]
        current_player = "X"
        for row in buttons:
            for button in row:
                button.configure(text="")

    buttons = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = ctk.CTkButton(game, text="", width=80, height=80, font=("Arial", 24), command=lambda i=i, j=j: button_click(i, j))
            buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

    game.mainloop()

root = ctk.CTk() 
root.geometry("800x800") 
root.title("Project")
root.resizable(False, False)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2 
w = w - 400 
h = h - 400
root.geometry('800x800+{}+{}'.format(w, h))


button = ctk.CTkButton(master=root, text='Калькулятор', text_color='White', fg_color='#0000CD', hover_color='Royal Blue', border_color='gray', corner_radius=12, height=40, command=calc)
button.place(x=320, y=10)
button = ctk.CTkButton(master=root, text='Генератор паролей', text_color='White', fg_color='#0000CD', hover_color='Royal Blue', corner_radius=12, height=40, command=pwgen)
button.place(x=320, y=60)
button = ctk.CTkButton(master=root, text='Информация', text_color='White', fg_color='#0000CD', hover_color='Royal Blue', corner_radius=12, height=40, command=info)
button.place(x=320, y=160)
button = ctk.CTkButton(master=root, text='Игра', text_color='White', fg_color='#0000CD', hover_color='Royal Blue', corner_radius=12, height=40, command=game)
button.place(x=320, y=110)

label = ctk.CTkLabel(master=root, text='Проект', text_color='Maroon', font=('Calibri Bold', 100))
label.place(x=245, y=670)
theme_checkbox = ctk.CTkCheckBox(root, text='Темная тема',
                                command=lambda:ctk.set_appearance_mode("Dark") if theme_checkbox.get() == 1
                                else ctk.set_appearance_mode("Light"))
theme_checkbox.grid(row=0, column=8)

root.mainloop()