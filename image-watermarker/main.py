from tkinter import *

from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
from time import time

filename = ""
window = Tk()
window.title("Image Watermarking")
window.config(padx=50,pady=50)
canvas = Canvas(width = 300,height = 200)
canvas.grid(row = 0, column = 0)

quote_text = canvas.create_text(150, 10, text="Upload the image you want to watermark",  font=("Arial", 10, "bold"))


def get_filename():
    filename = filedialog.askopenfilename(title = "Select a file to open")
    print(filename)
    im = Image.open(filename)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "Created by Samin Batra"
    font = ImageFont.truetype('arial.ttf', 72)
    textwidth, textheight = draw.textsize(text,font)

    print(textwidth)
    print(textheight)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width/2
    y = height/2
    print(f"Width: {width}")
    print(f"Height: {height}")
    print(x)
    print(y)
    draw.text((x, y), text, font = font)
    # im.show()
    file_name = filename.split("/")
    img_path = "/".join(file_name[:len(file_name)-1])
    print(f"Img path: {img_path}")
    watermarked_file = img_path + "/" + file_name[-1].split(".")[0] + "-watermarked" + "."+file_name[-1].split(".")[1]
    im.save(watermarked_file)
    top = Toplevel(window)
    top.geometry("400x100")
    top.title("Notice")
    Label(top, text=f"Image has been watermarked. Check location: {watermarked_file}", wraplength = 300,font=('Arial 10'), justify = CENTER).place(x=0, y=20)
    # return filename

file_button = Button(text = "Select a file", highlightthickness=0, command=get_filename)
file_button.grid(row=0, column=0)

window.mainloop()