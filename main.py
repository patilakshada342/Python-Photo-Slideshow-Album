import tkinter as tk
import time
from PIL import Image, ImageTk

#main Window
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# list of Image path
image_paths = [
        "Images/Img1.jpg",
    "Images/Img2.jpg",
    "Images/Img3.jpg",
    "Images/Img4.jpg",
    "Images/Img5.jpg"
]

image_size=(700,700)
images=[]
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img) #adding each image in the list

# convert pil image to tkinter compactible image
final_images=[]
for img in images:
    photo=ImageTk.PhotoImage(img)
    final_images.append(photo)

#label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)

#slideshow function
def slideshow():
    for photo in final_images:      
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)

#button
play_button= tk.Button(
    root,
    text='Play the slideshow',
    font=("Arial",17),
    command=slideshow
)

play_button.pack(pady=40)

root.mainloop()