import tkinter as tk
from tkinter import ttk

#   Need to specify a title for the application window
#   Add title to application
#   Specify function for search functionality
#   Add functionality to automatically pull asteroid list on application startup


#Create the main window as index and set default window size
index = tk.Tk()
index.title("**APPLICATION TITLE**")
index.geometry("1000x600")
index.columnconfigure(0, weight=1)

#Create a new label to contain a title
ttk.Label(index, text="**ASTEROID TRACKING TITLE HERE**").grid(row=0, column=0)

#Search frame
search_frame = ttk.Frame(index, padding=(30, 10, 0, 10))
search_frame.grid(row=1, column=0)

#Create a Frame to house asteroid list
asteroid_list_fame = ttk.Frame(index)
asteroid_list_fame.grid(row=2, column=0, sticky="NS")

#Frame to house logs
log_frame = ttk.Frame(index)
log_frame.grid(row=3, column=0, sticky="NS")

#Create a frame to house buttons
button_frame = ttk.Frame(index)
button_frame.grid(row=4, column=0)

#Asteroid List
ttk.Label(asteroid_list_fame, text="This is where our list will go from JSON dump",
          width=100, background="grey").grid(pady=100)

#Log List
ttk.Label(log_frame, text="This is where our logs will be", width=100,
          background="black", foreground="white").grid(pady=65)

#Asteroid search bar
asteroid_name = tk.StringVar()
asteroid_name_label = ttk.Label(search_frame, text="Asteroid Name:", width=14)
asteroid_name_label.grid(row=0, column=0)
as_name_entry = ttk.Entry(search_frame, width=55, textvariable=asteroid_name)
as_name_entry.grid(row=0, column=1)
search_button = ttk.Button(search_frame, text="Search")
search_button.grid(row=0, column=2)


#Create an exit button
exit_button = ttk.Button(button_frame, text="Exit", command=index.destroy)
exit_button.grid(row=0, column=3)

#Run mainloop
index.mainloop()