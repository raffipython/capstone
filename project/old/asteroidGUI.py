import tkinter as tk
from tkinter import ttk
import urllib.request
import io
from PIL import ImageTk, Image

#   Need to specify a title for the application window
#   Add title to application
#   Specify function for search functionality
#   Add functionality to automatically pull asteroid list on application startup


#Create the main window as index and set default window size
index = tk.Tk()
index.title("**APPLICATION TITLE**")
index.geometry("1000x600")
index.resizable(False, False)
index.columnconfigure(1, weight=1)

#Create a new label to contain a title
main_title = ttk.Label(index, text="**ASTEROID TRACKING TITLE HERE**")
main_title.grid(row=0, column=1, pady=30)
main_title.config(font=(24))

#Search frame
search_frame = ttk.Frame(index)
search_frame.grid(row=1, column=1, sticky="SW")

#Create a Frame to house asteroid list
asteroid_list_fame = ttk.Frame(index)
asteroid_list_fame.grid(row=2, column=0, columnspan=2, ipady=75)

#Frame to house logs
log_frame = ttk.Frame(index)
log_frame.grid(row=3, column=0, columnspan=2, ipady=55)

#Create a frame to house buttons
button_frame = ttk.Frame(index)
button_frame.grid(row=4, column=0, columnspan=2)

#Add an image
image_link = "https://th.bing.com/th?id=OIF.d%2fCjgd%2fJ42C1VjiLa2RSXg&pid=ImgDet&rs=1"

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data)).resize((260, 130))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image

img = WebImage(image_link).get()
imagelab = ttk.Label(index, image=img)
imagelab.grid(row=0, column=0, rowspan=2)

#Asteroid List
ttk.Label(asteroid_list_fame, text="This is where our asteroid list will go from JSON dump",
          background="grey", width=150).grid(sticky="N")

#Log List
ttk.Label(log_frame, text="This is where our logs will be",
          background="black", foreground="white", width=150).grid(sticky="N")

#Asteroid search bar
asteroid_name = tk.StringVar()
asteroid_name_label = ttk.Label(search_frame, text="Asteroid Name:", width=14, font=(14))
asteroid_name_label.grid(row=0, column=0)
as_name_entry = ttk.Entry(search_frame, width=75, textvariable=asteroid_name)
as_name_entry.grid(row=0, column=1)
search_button = ttk.Button(search_frame, text="Search", width=10)
search_button.grid(row=0, column=2)


#Create an exit button
exit_button = ttk.Button(button_frame, text="Exit", command=index.destroy)
exit_button.grid(row=0, column=3)

#Run mainloop
index.mainloop()