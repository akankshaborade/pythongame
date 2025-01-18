import os
import random
from tkinter import *
from tkinter import font as tkfont
import pygame
from PIL import Image, ImageTk

# Initialize Pygame mixer for sound effects
pygame.mixer.init()

# Define the path to the sound file
sound_file_path = os.path.join(os.path.dirname(__file__), 'mouse-click-104737.wav')

# Load the sound effect
click_sound = None
try:
    click_sound = pygame.mixer.Sound(sound_file_path)
except FileNotFoundError:
    print(f"Sound file not found: {sound_file_path}")

# Initialize Tkinter
root = Tk()
root.geometry('1630x1100+0+0')
root.title('Code Quest')
root.config(bg='black')

# Load and set Orbitron font
font_path = os.path.join(os.path.dirname(__file__), 'Orbitron-Regular.ttf')
try:
    custom_font = tkfont.Font(family="Orbitron", size=48)
    button_font = tkfont.Font(family="Orbitron", size=24)
    copyright_font = tkfont.Font(family="Orbitron", size=12)
except:
    custom_font = tkfont.Font(family="Arial", size=48)
    button_font = tkfont.Font(family="Arial", size=24)
    copyright_font = tkfont.Font(family="Arial", size=12)

def play_click_sound():
    if click_sound:
        click_sound.play()

# Function to show the specified frame
def show_frame(frame):
    frame.tkraise()

def select(event):
    global current_question_index, score
    play_click_sound()  # Play sound on button click

    # Get the selected answer
    selected_answer = event.widget['text']

    # Check if the selected answer is correct
    if selected_answer == correct_answers[current_question_index]:
        score += 1

    # Move to the next question or show the final score if it was the last question
    current_question_index += 1
    if current_question_index < len(selected_questions):
        # Update question and options for the next question
        questionArea.delete(1.0, END)
        questionArea.insert(END, questions[selected_questions[current_question_index]])

        optionButton1.config(text=option_1[selected_questions[current_question_index]])
        optionButton2.config(text=option_2[selected_questions[current_question_index]])
        optionButton3.config(text=option_3[selected_questions[current_question_index]])
        optionButton4.config(text=option_4[selected_questions[current_question_index]])
    else:
        # Display the final score
        questionArea.delete(1.0, END)
        questionArea.insert(END, f"Quiz Completed! Your Score: {score}/{len(selected_questions)}")

        # Disable buttons after the quiz is complete
        optionButton1.config(state=DISABLED)
        optionButton2.config(state=DISABLED)
        optionButton3.config(state=DISABLED)
        optionButton4.config(state=DISABLED)

def restart_quiz():
    global current_question_index, score, selected_questions
    score = 0
    current_question_index = 0
    selected_questions = random.sample(range(len(questions)), 15)  # Randomly select 15 questions
    questionArea.delete(1.0, END)
    questionArea.insert(END, questions[selected_questions[current_question_index]])
    optionButton1.config(text=option_1[selected_questions[current_question_index]], state=NORMAL)
    optionButton2.config(text=option_2[selected_questions[current_question_index]], state=NORMAL)
    optionButton3.config(text=option_3[selected_questions[current_question_index]], state=NORMAL)
    optionButton4.config(text=option_4[selected_questions[current_question_index]], state=NORMAL)

# Quiz data
correct_answers = [
    "int a;", ";", "print()", "float", "4 bytes",
    "#define", "malloc()", "Copies a string", "do-while loop", "True",
    "Call functions dynamically", "&", "-1", "Declares an external variable", "Undefined behavior",
    "def main()", "return 0;", "void", "char", "len()",
    "break", "continue", "static", "const", "x = 5",
    "None", "append()", "len()", "list = [1, 2, 3]", "for i in range(n):",
    "int", "float", "double", "char", "x = 5",
    "x = a + b", "x = a - b", "x = a * b", "x = a / b", "x = a % b",
    "if x > 0:", "else", "switch", "case 1:", "print('Hello, World!')",
    "input()", "fgets()", "puts()", "gets()", "str()"
]

questions = [
    "Q> What is the correct syntax for declaring an integer variable in most programming languages?",
    "Q> Which symbol is commonly used to terminate a statement in many programming languages?",
    "Q> What function is used to print output in Python?",
    "Q> Which data type is used to store decimal values in programming?",
    "Q> What is the typical size of an integer data type in bytes?",
    "Q> Which keyword is used to define a constant in many programming languages?",
    "Q> How do you dynamically allocate memory for an array in C/C++?",
    "Q> What does the function 'strcpy' do in C?",
    "Q> Which loop is guaranteed to execute at least once?",
    "Q> What is the output of: print(10 > 5)?",
    "Q> What is the primary purpose of a function pointer in C?",
    "Q> Which operator is used to get the address of a variable in C?",
    "Q> What is the output of the expression: ~0 in C?",
    "Q> What does the 'extern' keyword do in C?",
    "Q> What will the following code output?\n\nint x = 10; printf(\"%d\", ++x + x++);",
    "Q> What is the correct way to define the main function in Python?",
    "Q> What is the return type of the main function in C?",
    "Q> What is the keyword used to declare a function that does not return a value?",
    "Q> Which data type can hold a single character?",
    "Q> How do you get the length of a list in Python?",
    "Q> What statement is used to exit a loop prematurely?",
    "Q> What statement is used to skip the current iteration of a loop?",
    "Q> Which keyword is used to declare a variable that retains its value between function calls?",
    "Q> What keyword is used to declare a constant variable?",
    "Q> How do you declare a pointer to an integer in C?",
    "Q> What is the value of a null pointer?",
    "Q> What does the function 'append()' do in Python?",
    "Q> What does the function 'len()' return?",
    "Q> How do you declare an array of 10 integers in Python?",
    "Q> What is the syntax for a for loop in Python?",
    "Q> What is the data type of the variable 'x' after the following statement: x = 5?",
    "Q> How do you declare multiple variables of the same type in one line?",
    "Q> What is the syntax for adding two variables 'a' and 'b'?",
    "Q> What is the syntax for subtracting two variables 'a' and 'b'?",
    "Q> What is the syntax for multiplying two variables 'a' and 'b'?",
    "Q> What is the syntax for dividing two variables 'a' and 'b'?",
    "Q> What is the syntax for getting the remainder of two variables 'a' and 'b'?",
    "Q> What is the syntax for checking if 'x' is greater than 0?",
    "Q> What is the syntax for an else statement?",
    "Q> What is the syntax for a switch statement?",
    "Q> What is the syntax for a case in a switch statement?",
    "Q> What is the correct way to print 'Hello, World!' in Python?",
    "Q> What is the function used to read input from the user in Python?",
    "Q> How do you create a list in Python?",
    "Q> What is the purpose of the 'self' parameter in Python class methods?",
    "Q> How do you define a function in Python?",
    "Q> What is the difference between a list and a tuple in Python?",
    "Q> How do you handle exceptions in Python?",
    "Q> What is the output of the expression: 'Hello' + ' World'?",
    "Q> How do you check if a key exists in a dictionary in Python?",
    "Q> What is the purpose of the 'return' statement in a function?",
    "Q> How do you import a module in Python?",
    "Q> What is the syntax for a while loop in Python?",
    "Q> How do you create a class in Python?",
    "Q> What is the purpose of the 'pass' statement in Python?",
    "Q> How do you convert a string to an integer in Python?",
    "Q> What is the output of the expression: [1, 2, 3] * 2?",
    "Q> How do you remove an item from a list in Python?",
    "Q> What is the difference between '==' and 'is' in Python?",
    "Q> How do you create a dictionary in Python?",
    "Q> What is the purpose of the 'with' statement in Python?",
    "Q> How do you sort a list in Python?",
    "Q> What is the output of the expression: 3 ** 2?",
    "Q> How do you create a set in Python?",
    "Q> What is the purpose of the 'global' keyword in Python?",
    "Q> How do you iterate over a dictionary in Python?",
    "Q> What is the output of the expression: 'abc'.upper()?",
    "Q> How do you check the type of a variable in Python?",
    "Q> What is the purpose of the 'len()' function?",
    "Q> How do you concatenate two lists in Python?",
    "Q> What is the output of the expression: 10 // 3?",
    "Q> How do you create a generator in Python?",
    "Q> What is the purpose of the 'yield' statement in Python?",
    "Q> How do you access elements in a nested list in Python?",
    "Q> What is the output of the expression: 'Python'[-1]?",
    "Q> How do you create a copy of a list in Python?",
    "Q> What is the purpose of the 'enumerate()' function in Python?",
    "Q> How do you check if a string contains a substring in Python?",
    "Q> What is the output of the expression: 5 % 2?",
    "Q> How do you format strings in Python?",
    "Q> What is the purpose of the 'strip()' method in Python?",
    "Q> How do you create a virtual environment in Python?",
    "Q> What is the output of the expression: 'Hello'.replace('e', 'a')?"
]

option_1 = [
    "int a;", ";", "print()", "int", "1 byte",
    "var", "malloc()", "Copies a string", "for loop", "True",
    "Store function names", "*", "0", "Defines a constant", "21",
    "def main()", "None", "void", "char", "4 bytes",
    "break", "continue", "static", "const", "x = 5",
    "None", "append()", "length", "list = [1, 2, 3]", "for i in range(n):",
    "int", "float", "double", "char", "x = 5",
    "x = a + b", "x = a - b", "x = a * b", "x = a / b", "x = a % b",
    "if x > 0:", "else", "switch", "case 1:", "print('Hello, World!')",
    "input()", "fgets()", "puts()", "gets()", "str()"
]

option_2 = [
    "integer a;", ";", "print", "float", "2 bytes",
    "const", "allocate", "Concatenates a string", "while loop", "False",
    "Call functions statically", "&", "-1", "Declares a global variable", "20",
    "def main():", "return 0;", "void", "string", "8 bytes",
    "exit", "skip", "volatile", "final", "x = 5",
    "None", "append", "length()", "array = [1, 2, 3]", "for i in range(n):",
    "int", "float", "double", "string", "x = 5",
    "x = a + b;", "x = a - b;", "x = a * b;", "x = a / b;", "x = a % b;",
    "if (x > 0)", "else", "switch", "case 1:", "print('Hello, World!')",
    "input", "fgets", "puts", "gets", "str"
]

option_3 = [
    "var a;", ":", "cout", "char", "4 bytes",
    "#define", "new", "Compares strings", "do-while loop", "1",
    "Manipulate strings", "@", "1", "Declares an external variable", "22",
    "def main():", "None", "void", "char", "sizeof(int)",
    "break", "continue", "static", "const", "int *ptr;",
    "NULL", "strcat", "strlen", "int arr[10];", "for (int i = 0; i < n; i++)",
    "int", "float", "double", "char", "int x = 5;",
    "int a = 10, b = 20;", "x = a + b;", "x = a - b;", "x = a * b;", "x = a / b;",
    "x = a % b;", "if (x > 0)", "else", "switch", "case 1:",
    "printf(\"Hello, World!\");", "scanf", "fgets", "puts", "gets"
]

option_4 = [
    "declare int a;", ".", "output", "double", "8 bytes",
    "constant", "calloc", "Finds length", "switch", "1",
    "Control loops", "%", "None of the above", "Allocates memory", "Undefined behavior",
    "def main():", "return 0;", "void", "char", "len()",
    "break", "continue", "static", "const", "x = 5",
    "None", "append()", "len()", "list = [1, 2, 3]", "for i in range(n):",
    "int", "float", "double", "char", "x = 5",
    "x = a + b;", "x = a - b;", "x = a * b;", "x = a / b;", "x = a % b;",
    "if (x > 0)", "else", "switch", "case 1:", "print('Hello, World!')",
    "input()", "fgets()", "puts()", "gets()", "str()"
]

# Initialize score and question index
score = 0
current_question_index = 0
selected_questions = random.sample(range(len(questions)), 15)  # Randomly select 15 questions

# Create frames for each page
main_frame = Frame(root, bg='black')
signup_frame = Frame(root, bg='white')
login_frame = Frame(root, bg='white')
start_frame = Frame(root, bg='white')  # New Start frame
quiz_frame = Frame(root, bg='black')  # New Quiz frame

# Load background image once
background_image = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'background.png'))

layout_image_path = os.path.join(os.path.dirname(__file__), 'layout.png')
layout_image_pil = Image.open(layout_image_path).resize((1550, 550), Image.Resampling.LANCZOS)
layout_image = ImageTk.PhotoImage(layout_image_pil)

# Load and resize the arrow image
arrow_image_path = os.path.join(os.path.dirname(__file__), 'arrow.png')
arrow_image = Image.open(arrow_image_path)
arrow_image = arrow_image.resize((50, 50))  # Resize to 50x50 pixels
arrow_image = ImageTk.PhotoImage(arrow_image)

# Place all frames in the same position
for frame in (main_frame, signup_frame, login_frame, start_frame, quiz_frame):
    frame.place(relwidth=1, relheight=1)

# Load background image for main page
background_label = Label(main_frame, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create the title label in main frame
title_label = Label(main_frame, text="Code Quest", font=custom_font, bg='black', fg='green')
title_label.place(relx=0.5, rely=0.4, anchor='center')

# Create Login button in main frame
login_button = Button(main_frame, text="Login", font=button_font, command=lambda: [play_click_sound(), show_frame(login_frame)], bg='blue', fg='white')
login_button.place(relx=0.7, rely=0.6, anchor='center')

# Create Sign Up button in main frame
signup_button = Button(main_frame, text="Sign Up", font=button_font, command=lambda: [play_click_sound(), show_frame(signup_frame)], bg='green', fg='white')
signup_button.place(relx=0.3, rely=0.6, anchor='center')

# Add copyright label in main frame
copyright_label = Label(main_frame, text="© 2024 CODE QUEST. All Rights Reserved.", font=copyright_font, bg='black', fg='Green')
copyright_label.place(relx=0.5, rely=0.9, anchor='center')

# Load background image for sign-up page
signup_background_label = Label(signup_frame, image=background_image)
signup_background_label.place(relwidth=1, relheight=1)

# Create a frame for the sign-up form with a border
form_frame_signup = Frame(signup_frame, bg='black', bd=2, relief='ridge')
form_frame_signup.pack(padx=100, pady=100)

signup_label = Label(form_frame_signup, text='Sign Up Form', font=('Orbitron', 26), bg='black', fg='white')
signup_label.pack(pady=(20, 10))

email_label = Label(form_frame_signup, text='Email ID:', font=('Orbitron', 24), bg='black', fg='white')
email_label.pack(pady=(10, 0))
email_entry = Entry(form_frame_signup, font=('Orbitron', 24), width=20)
email_entry.pack(padx=20, pady=(0, 10))

username_label = Label(form_frame_signup, text='Username:', font=('Orbitron', 24), bg='black', fg='white')
username_label.pack(pady=(10, 0))
username_entry = Entry(form_frame_signup, font=('Orbitron', 24), width=20)
username_entry.pack(padx=20, pady=(0, 10))

password_label = Label(form_frame_signup, text='Password:', font=('Orbitron', 24), bg='black', fg='white')
password_label.pack(pady=(10, 0))
password_entry = Entry(form_frame_signup, show='*', font=('Orbitron', 24), width=20)
password_entry.pack(padx=20, pady=(0, 10))

# Update submit button to also show the login page after clicking
submit_button_signup = Button(form_frame_signup, text='Submit', font=('Orbitron', 26), command=lambda: [play_click_sound(), show_frame(login_frame)], bg='green', fg='white')
submit_button_signup.pack(pady=(20, 10))

# Load background image for login page
login_background_label = Label(login_frame, image=background_image)
login_background_label.place(relwidth=1, relheight=1)

# Create a frame for the login form with a border
form_frame_login = Frame(login_frame, bg='black', bd=2, relief='ridge')
form_frame_login.pack(padx=100, pady=100)

# Login Form
login_label = Label(form_frame_login, text='Login Form', font=('Orbitron', 26), bg='black', fg='white')
login_label.pack(pady=( 20, 10))

username_label_login = Label(form_frame_login, text='Username:', font=('Orbitron', 24), bg='black', fg='white')
username_label_login.pack(pady=(10, 0))
username_entry_login = Entry(form_frame_login, font=('Orbitron', 24), width=20)
username_entry_login.pack(padx=20, pady=(0, 10))

password_label_login = Label(form_frame_login, text='Password:', font=('Orbitron', 24), bg='black', fg='white')
password_label_login.pack(pady=(10, 0))
password_entry_login = Entry(form_frame_login, show='*', font=('Orbitron', 24), width=20)
password_entry_login.pack(padx=20, pady=(0, 10))

# Update login button to go to start page after clicking
login_button_submit = Button(form_frame_login, text='Login', font=('Orbitron', 26), command=lambda: [play_click_sound(), show_frame(start_frame)], bg='blue', fg='white')
login_button_submit.pack(pady=(20, 10))

# Load background image for start page
start_background_label = Label(start_frame, image=background_image)
start_background_label.place(relwidth=1, relheight=1)

# Create Start frame
start_label = Label(start_frame, text='Welcome to Code Quest!', font=('Orbitron', 36), bg='white', fg='black')
start_label.pack(pady=(50, 20))

# Create Start button in Start frame
start_button = Button(start_frame, text='Start', font=('Orbitron', 26), command=lambda: [play_click_sound(), show_frame(quiz_frame)], bg='green', fg='white')
start_button.pack(pady=(20, 10))

# Load background image for quiz page
quiz_background_label = Label(quiz_frame, image=background_image)
quiz_background_label.place(relwidth=1, relheight=1)

# Add layout image to quiz page
layout_label = Label(quiz_frame, image=layout_image, bg='black')
layout_label.place(relx=0.5, rely=0.5, anchor='center')

# Create question area
questionArea = Text(quiz_frame, font=button_font, width=45, height=2, wrap=WORD, bg='black', fg='white', bd=0)
questionArea.place(x=142, y=180)
questionArea.insert(END, questions[selected_questions[current_question_index]])

# Create option buttons
labelA = Label(quiz_frame, text='A:', bg='black', fg='white', font=button_font)
labelA.place(x=110, y=360)

optionButton1 = Button(quiz_frame, text=option_1[selected_questions[current_question_index]], font=button_font, bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2', height=2, width=20)
optionButton1.place(x=180, y=350)

labelB = Label(quiz_frame, text='B:', bg='black', fg='white', font=button_font)
labelB.place(x=850, y=360)

optionButton2 = Button(quiz_frame, text=option_2[selected_questions[current_question_index]], font=button_font, bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2', height=2, width=20)
optionButton2.place(x=900, y=350)

labelC = Label(quiz_frame, text='C:', bg='black', fg='white', font=button_font)
labelC.place(x=90, y=550)

optionButton3 = Button(quiz_frame, text=option_3[selected_questions[current_question_index]], font=button_font, bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2', height=2, width=20)
optionButton3.place(x=120, y=525)

labelD = Label(quiz_frame, text='D:', bg='black', fg='white', font=button_font)
labelD.place(x=850, y=550)

optionButton4 = Button(quiz_frame, text=option_4[selected_questions[current_question_index]], font=button_font, bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2', height=2, width=20)
optionButton4.place(x=880, y=525)

# Bind button click events to the select function
optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

# Add backspace arrow to the sign-up form
back_arrow_signup = Label(signup_frame, image=arrow_image, bg='white', cursor='hand2')
back_arrow_signup.place(relx=0.01, rely=0.01, anchor='nw')
back_arrow_signup.bind("<Button-1>", lambda e: show_frame(main_frame))

# Add back arrow to the login form
back_arrow_login = Label(login_frame, image=arrow_image, bg='white', cursor='hand2')
back_arrow_login.place(relx=0.02, rely=0.02, anchor='nw')
back_arrow_login.bind("<Button-1>", lambda e: show_frame(main_frame))

# Add back arrow to the start frame
back_arrow_start = Label(start_frame, image=arrow_image, bg='white', cursor='hand2')
back_arrow_start.place(relx=0.02, rely=0.02, anchor='nw')
back_arrow_start.bind("<Button-1>", lambda e: show_frame(main_frame))

# Show the main frame initially
show_frame(main_frame)

root.mainloop()