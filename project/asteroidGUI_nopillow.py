import tkinter as tk
from tkinter import ttk
import backend

#   Need to specify a title for the application window
#   Add title to application
#   Specify function for search functionality
#   Add functionality to automatically pull asteroid list on application startup

DATABASE = {}



#Create the main window as index and set default window size
index = tk.Tk()
index.title("Near Earth Objects Viewer")
index.geometry("1000x600")
index.resizable(False, False)
index.columnconfigure(1, weight=1)

#Create a new label to contain a title
main_title = ttk.Label(index, text="Near Earth Objects Viewer")
main_title.grid(row=0, column=1, pady=30)
main_title.config(font=(24))

#Search frame
search_frame = ttk.Frame(index)
search_frame.grid(row=1, column=1, sticky="SW")

#Create a Frame to house asteroid list
asteroid_list_fame = ttk.Frame(index)
asteroid_list_fame.grid(row=2, column=0, columnspan=2)

#Frame to house logs
log_frame = ttk.Frame(index)
log_frame.grid(row=3, column=0, columnspan=2)

#Create a frame to house buttons
button_frame = ttk.Frame(index)
button_frame.grid(row=4, column=0, columnspan=2)

# image link https://th.bing.com/th?id=OIF.d%2fCjgd%2fJ42C1VjiLa2RSXg&pid=ImgDet&rs=1
img = tk.PhotoImage(file="asteroid.gif")
imagelab = ttk.Label(index, image=img)
imagelab.grid(row=0, column=0, rowspan=2)

#Asteroid List
ttk.Label(asteroid_list_fame, text="This is where our asteroid list will go from JSON dump",
          background="grey", width=100).grid(row=0,column=0,sticky="N")
asteroid_columns = ("Column1", "Column2", "Column3", "Column4", "We can add more..")
ast_tree = ttk.Treeview(asteroid_list_fame, columns=asteroid_columns, show='headings')
ast_tree.grid(row=1, column=0)
for col in asteroid_columns:
    ast_tree.heading(col, text=col)

#Log List
ttk.Label(log_frame, text="This is where our logs will be",
          background="black", foreground="white", width=100).grid(row=0,column=0, sticky="N")
log_columns = ("Column1", "Column2", "Column3", "Column4", "We can add more..")
log_tree = ttk.Treeview(log_frame, columns=log_columns, show='headings')
log_tree.grid(row=1, column=0)
for col in log_columns:
    log_tree.heading(col, text=col)

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
