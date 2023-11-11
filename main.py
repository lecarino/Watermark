from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageFont
import urllib.error

window = Tk()
window.title("Watermark Generator")
window.config(padx=20, pady=20)

def read_file():
    size = (600,600)
    watermark_text = 'Larrenz Carino'
    font = ImageFont.truetype('coneria-script/Demo_ConeriaScript.ttf', size= 75)
    url_or_file = image_entry.get()
    try:
        with Image.open(urlopen(url_or_file)) as img:
            
            # Resize image using ImageOps.cover 
            img_covered = ImageOps.cover(img, size)

            #watermark
            draw = ImageDraw.Draw(img_covered)
            draw.text((300,300),watermark_text, fill=(255, 255, 255), font=font, align='center', anchor='mm')

            #save img as png
            img_covered.save('watermarked_img.png')
    except urllib.error.HTTPError:
        # Handle the HTTP error (404 Not Found) gracefully
        print("Image not found at the specified URL.")
    except ValueError:
        try: 
            with Image.open(url_or_file) as img:
                # Resize image using ImageOps.cover 
                img_covered = ImageOps.cover(img, size)

                #watermark
                draw = ImageDraw.Draw(img_covered)
                draw.text((300,300),watermark_text, fill=(255, 255, 255), font=font, align='center', anchor='mm')

                #save image as png
                img_covered.save('watermarked_img.png')
        except Exception as e:
            print(f'Error: {e}')
            return
    
    saved_img = Image.open('watermarked_img.png')
    photo = ImageTk.PhotoImage(saved_img)
    # Create a new Label for each image
    new_label = Label(window, image=photo)
    new_label.image = photo
    new_label.grid(row=3, column=1, columnspan=2)



# Label
image_label = Label(window, text="Image URL or File Path:")
image_label.grid(row=1, column=0)

# Entry
image_entry = Entry(window, width=35)
image_entry.grid(row=1, column=1, columnspan=2)
image_entry.focus()

# Button
add_button = Button(window, text="Upload Image URL or File Path", width=36, command=read_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
