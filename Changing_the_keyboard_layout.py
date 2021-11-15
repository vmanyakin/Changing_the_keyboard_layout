import tkinter as tk
import pygame


# Text conversion function
def engrus(text):
    translate = ''
    sp1 = " qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,./1234567890:%@=-+*$&!№$^(){}_"
    sp2 = " йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ.1234567890:%@=-+*$&!№$^(){}_"
    for letter in text:
        if letter in sp2:
            a = sp2.index(letter)
            b = sp1[a]
            translate += b
        elif letter in sp1:
            a = sp1.index(letter)
            b = sp2[a]
            translate += b
        else:
            translate += '???'

    return translate


def click_me():
    text1.delete('1.0', tk.END)
    result = text.get('1.0', 'end-1c')
    text1.insert('1.0',engrus(result))


pygame.mixer.init()
def play():
    pygame.mixer.music.load('music/music_1.mp3')
    pygame.mixer.music.play(loops=-1)

def stop():
    pygame.mixer.music.stop()

# Сreating a window
window = tk.Tk()
window.geometry('870x510+600+200')
window.configure(bg='black')
window.title('Программа для смены раскладки клавиатуры')
play()

label = tk.Label(text='Привет! Для того, чтобы сменить раскладку клавиатуры, вставь текст и нажми на кнопку!',
                 bg='black',
                 fg='white',
                 font=("Times New Roman Baltic", 14),
                 )
label.place(x=20, y=10)

# Сreating a text window
text = tk.Text(padx=10, pady=10, width=30, height=25)
text.place(x=50, y=50)

text1 = tk.Text(padx=10, pady=10, width=30, height=25)
text1.place(x=500, y=50)

# Creating a button
click = tk.Button(text='Нажми\nна меня!',
                  bg='white', fg='black',
                  width=7,
                  height=7,
                  font=("Times New Roman Baltic", 14),
                  command=click_me
                  )
click.place(x=360, y=200)



click = tk.Button(text='stop\nmusic',
                  bg='white', fg='black',
                  width=5,
                  height=5,
                  font=("Times New Roman", 10),
                  command=stop
                  )
click.place(x=805, y=15)


window.mainloop()

