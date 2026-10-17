import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame


window = tk.Tk()

pygame.mixer.init()
pygame.mixer.music.load("pink panther (320).mp3")
pygame.mixer.music.play(-1)

image = Image.open("cute_game.png")

image = image.resize((500,600))
background = ImageTk.PhotoImage(image)
background_label = tk.Label(
    window,
    image=background
)

background_label.place(x=0,y=0)

number = random.randint(1,100)

window.title("GUESS GAME")
window.geometry("500x600")
window.configure(bg="#724EC7")

#title = tk.Label(
#ٌ    window,
#    text="GUESS GAME",
#    font=("Arial", 30),
#    bg= "#D46C96"
#)

#title.place(x=150,y=10)

number_input = tk.Entry(
    window,
    font=("Arial",20)
)

number_input.place(x=110, y=205, width=300, height=55)

message = tk.Label(
    window,
    text="",
    font=("Arial",13),
    bg="#7C40D6"
)

message.place(x=130, y=268, width=250, height=50)

attempts=0

attempts_label= tk.Label(
    window,
    text="Attempts:0/5",
    font=("Arial",16),
    bg="#E7BBF3"
)

attempts_label.place(x=200, y=380)

def guess():
    global attempts

    attempts = attempts + 1

    usernumber = int(number_input.get())

    attempts_label.config(text=f"Attempts:{attempts}/5")

    if usernumber == number:
        message.config(text="you won🥳")
        guess_button.config(state="disabled")

    elif attempts >= 5:
        message.config(text=f"😢 You lost! The number was {number}.")
        guess_button.config(state="disabled")

    elif usernumber < number:
        message.config(text="go higher⬆️")

    else:
        message.config(text="go lower⬇️")

guess_button = tk.Button(
    window,
    text="GUESS",
    font=("Arial",18),
    bg="#C01EEC",
    command=guess

)
guess_button.place(x=200, y=420, width=100, height=50)

window.mainloop()