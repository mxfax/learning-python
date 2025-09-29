import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from tkinter import messagebox 
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os  

CHECKMARK = "\u2713"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

main_img = None
logo_img = None
main_img_preview = None
logo_img_preview = None

#upload main img
def UploadMainImg():
    global main_img
    filename = filedialog.askopenfilename()
    if filename:
        print('Selected:', filename)
        main_img = Image.open(filename).convert("RGBA")  # keep alpha channel
        print(main_img.format, main_img.size, main_img.mode)
        # create thumbnail preview
        preview = main_img.copy()
        preview.thumbnail((80, 80))
        global main_img_preview
        main_img_preview = ImageTk.PhotoImage(preview)
        preview_label1.config(image=main_img_preview)
        preview_label1.image = main_img_preview
        AddCheckMainImg()
        BringToFront()

#uploading the logo img
def UploadLogo():
    global logo_img
    filename = filedialog.askopenfilename()
    if filename:
        print('Selected:', filename)
        logo_img = Image.open(filename).convert("RGBA")  # keep alpha channel
        print(logo_img.format, logo_img.size, logo_img.mode)
        # create thumbnail preview
        preview = logo_img.copy()
        preview.thumbnail((80, 80))
        global logo_img_preview
        logo_img_preview = ImageTk.PhotoImage(preview)
        preview_label2.config(image=logo_img_preview)
        preview_label2.image = logo_img_preview
        AddCheckLogo()
        BringToFront()

#show checkmark for successfully uploaded main img file
def AddCheckMainImg():
    new_checkmark = CHECKMARK
    checkbutton1.config(text=new_checkmark)

#show checkmark for successfully uploaded logo file
def AddCheckLogo():
    new_checkmark = CHECKMARK
    checkbutton2.config(text=new_checkmark)

#make window popup in front
def BringToFront():
    window.focus_force()

#add uploaded logo to the main image
def AddLogo():
    global main_img, logo_img
    if not main_img:
        messagebox.showerror("Error", "Please upload a main image first")
        return
    if not logo_img:
        messagebox.showerror("Error", "Please upload a logo image first")
        return

    # Create a copy of the main image to work with
    watermarked = main_img.copy()
    
    # Resize logo if resize option is checked and check for the proper size
    if resize_var.get():
        try:
            new_width = int(x_entry.get())
            new_height = int(y_entry.get())
            if new_height < main_img.size[0] and new_width < main_img.size[1]:
                logo_img = logo_img.resize((new_width, new_height))
            else:
                messagebox.showerror("Error", f"the size should be less than {main_img.size[0]} x {main_img.size[1]}")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for resize")
            return

    # Apply transparency if selected
    if transparency_var.get():
        try:
            transparency = int(trans_x_entry.get())
            if 0 <= transparency <= 100:
                logo_img.putalpha(int(255 * (transparency / 100)))
            else:
                messagebox.showerror("Error", "Transparency must be between 0 and 100")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid transparency value (0-100)")
            return

    # Calculate position
    main_width, main_height = watermarked.size
    logo_width, logo_height = logo_img.size
    
    # Define position based on checkbox selection
    position = {
        "tl": (0, 0),
        "tr": (main_width - logo_width, 0),
        "bl": (0, main_height - logo_height),
        "br": (main_width - logo_width, main_height - logo_height),
        "center": ((main_width - logo_width) // 2, (main_height - logo_height) // 2)
    }.get(position_var.get(), (0, 0))  # default to top-left if invalid value

    # Paste the logo onto the main image
    if logo_img.mode == 'RGBA':
        watermarked.paste(logo_img, position, logo_img)
    else:
        watermarked.paste(logo_img, position)

    # Save the watermarked image
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg;*.jpeg"),
            ("GIF files", "*.gif"),
            ("BMP files", "*.bmp"),
            ("All files", "*.*")
        ]
    )
    
    try:
        if save_path and validate_save_path(save_path):
            watermarked.save(save_path)
            messagebox.showinfo("Success", f"Image saved successfully to:\n{save_path}")
            watermarked.show()
        elif save_path:  # If path exists but extension is invalid
            messagebox.showerror("Error", "Please use a valid image format (.png, .jpg, .jpeg, .gif, or .bmp)")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid file format. {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


#add text watermark
def AddText():
    global main_img
    if not main_img:
        messagebox.showerror("Error", "Please upload a main image first")
        return
        
    #create a copy of the main image to work with
    watermarked = main_img.copy()
    
    #get text from entry
    watermark_text = text_entry.get()
    if not watermark_text:
        messagebox.showerror("Error", "Please enter text for watermark")
        return
        
    #create text layer with transparency
    txt_layer = Image.new('RGBA', main_img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    
    #calculate font size based on image size (20% of image width)
    font_size = int(main_img.size[0] * 0.2)
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        messagebox.showwarning("Warning", "Arial font not found. Using default font.")
        font = ImageFont.load_default()
        
    #get text size using textbbox instead of textsize
    left, top, right, bottom = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = right - left
    text_height = bottom - top
    
    #calculate position based on radio selection
    main_width, main_height = watermarked.size
    position = {
        "tl": (0, 0),
        "tr": (main_width - text_width, 0),
        "bl": (0, main_height - text_height),
        "br": (main_width - text_width, main_height - text_height),
        "center": ((main_width - text_width) // 2, (main_height - text_height) // 2)
    }.get(position_var.get(), (0, 0))
    
    #apply transparency if selected
    opacity = 255
    if transparency_var.get():
        try:
            transparency = int(trans_x_entry.get())
            if 0 <= transparency <= 100:
                opacity = int(255 * (transparency / 100))
            else:
                messagebox.showerror("Error", "Transparency must be between 0 and 100")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid transparency value (0-100)")
            return
                
    #draw text on the layer
    draw.text(position, watermark_text, fill=(0, 0, 0, opacity), font=font)
    
    #combine images
    watermarked = Image.alpha_composite(watermarked.convert('RGBA'), txt_layer)
    
    #save the watermarked image
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        watermarked.save(save_path)
        print(f"Text watermarked image saved to {save_path}")
        watermarked.show()


#hide and show resize X, Y text fields
def toggle_resize_fields():
    if resize_var.get():
        x_label.grid(column=2, row=7, sticky="e")
        x_entry.grid(column=3, row=7, sticky="w")
        y_label.grid(column=2, row=8, sticky="e")
        y_entry.grid(column=3, row=8, sticky="w")
    else:
        x_label.grid_remove()
        x_entry.grid_remove()
        y_label.grid_remove()
        y_entry.grid_remove()

def toggle_transparency_fields():
    if transparency_var.get():
        trans_x_label.grid(column=2, row=10, sticky="e")
        trans_x_entry.grid(column=3, row=10, sticky="w")

    else:
        trans_x_label.grid_remove()
        trans_x_entry.grid_remove()

def validate_save_path(save_path):
    """Validate if the file extension is supported"""
    valid_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    if not save_path:
        return False
    file_ext = os.path.splitext(save_path)[1].lower()
    return file_ext in valid_extensions


window = tk.Tk()
resize_var = tk.BooleanVar()
transparency_var = tk.BooleanVar()
window.title("Watermarked")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200, bg=YELLOW)

#thumbnail frames and labels
preview_frame1 = tk.Frame(window, bg="black", bd=2, relief="solid", width=84, height=84)
preview_frame1.grid(column=2, row=0)
preview_label1 = tk.Label(preview_frame1, bg=YELLOW)
preview_label1.place(relx=0.5, rely=0.5, anchor="center")

preview_frame2 = tk.Frame(window, bg="black", bd=2, relief="solid", width=84, height=84)
preview_frame2.grid(column=5, row=0)
preview_label2 = tk.Label(preview_frame2, bg=YELLOW)
preview_label2.place(relx=0.5, rely=0.5, anchor="center")

#checkbutton for successfull upload of the main image
checkbutton1 = Label(fg=GREEN, bg=YELLOW)
checkbutton1.config(text="")
checkbutton1.grid(column=2, row=1)

#checkbutton for successfull upload of the logo
checkbutton2 = Label(fg=GREEN, bg=YELLOW)
checkbutton2.config(text="")
checkbutton2.grid(column=5, row=1)

#buttons layout
button = tk.Button(window, text='Upload Main Img', command=UploadMainImg, bg=YELLOW, bd=0, highlightthickness=0)
button.grid(column=2, row=2, padx=(0, 20))
button.config(pady=2, padx=2)
button2 = tk.Button(window, text='Upload Logo', command=UploadLogo, bg=YELLOW, bd=0, highlightthickness=0)
button2.grid(column=5, row=2)
button2.config(pady=2, padx=2)
button3 = tk.Button(window, text='Place Logo', command=AddLogo, bg=YELLOW, bd=0, highlightthickness=0)
button3.grid(column=3, row=13, padx=(0, 20))
button3.config(pady=2, padx=2)
button4 = tk.Button(window, text='Add Text Watermark', command=AddText, bg=YELLOW, bd=0, highlightthickness=0)
button4.grid(column=3, row=14, padx=(0, 20))
button4.config(pady=2, padx=2)

#checkbutton for resize option
resize_check = tk.Checkbutton(window, text="Do you want to resize Logo?", variable=resize_var, bg=YELLOW, command= toggle_resize_fields)
resize_check.grid(column=2, row=6, columnspan=2, sticky="w")

x_label = tk.Label(window, text="X:", bg=YELLOW)
y_label = tk.Label(window, text="Y:", bg=YELLOW)
x_entry = tk.Entry(window, width=5)
y_entry = tk.Entry(window, width=5)

#checkbutton for resize option
transparency_check = tk.Checkbutton(window, text="Do you want to add transparency to the Logo?", variable=transparency_var, bg=YELLOW, command= toggle_transparency_fields)
transparency_check.grid(column=2, row=9, columnspan=2, sticky="w")
trans_x_label = tk.Label(window, text="Transparency %(0-100): ", bg=YELLOW)
trans_x_entry = tk.Entry(window, width=5)

#text watermark UI elements
text_label = tk.Label(window, text="Watermark Text:", bg=YELLOW)
text_label.grid(column=2, row=3, sticky="e")
text_entry = tk.Entry(window, width=20)
text_entry.grid(column=3, row=3, sticky="w")

#replace the checkbox variables with a single StringVar for position
#add this after the window creation and before the position frame creation
position_var = tk.StringVar(value="tl")  # default to top-left

#logo position selection frame
position_frame = tk.Frame(window, bg=YELLOW, bd=2, relief="solid", width=150, height=150)
position_frame.grid(column=0, row=11, columnspan=6, sticky="nsew")
position_frame.grid_propagate(False)

#replace individual checkbuttons with radio buttons
tk.Radiobutton(position_frame, text="Top Left", variable=position_var, 
               value="tl", bg=YELLOW).place(relx=0.0, rely=0.0, anchor="nw")
tk.Radiobutton(position_frame, text="Top Right", variable=position_var, 
               value="tr", bg=YELLOW).place(relx=1.0, rely=0.0, anchor="ne")
tk.Radiobutton(position_frame, text="Bottom Left", variable=position_var, 
               value="bl", bg=YELLOW).place(relx=0.0, rely=1.0, anchor="sw")
tk.Radiobutton(position_frame, text="Bottom Right", variable=position_var, 
               value="br", bg=YELLOW).place(relx=1.0, rely=1.0, anchor="se")
tk.Radiobutton(position_frame, text="Center", variable=position_var, 
               value="center", bg=YELLOW).place(relx=0.5, rely=0.5, anchor="center")


window.mainloop()
