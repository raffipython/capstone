"""Frontend of program that sets up a GUI to print data
obtained from NASA API for asteroids approaching earth within
the next year. As well as printing data about them, and calculations on
speed/distance/suspected date of impact.

authors: Bryan Wynes, Jacob Scanlan, and Raffi Jubrael
date: 2023/07/27
version: 0.0.3
"""

import json
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import backend as be
import logging
import datetime as dt


def on_item_click(event):
    """ Gets an event object from GUI, and it calls the asteroid data handler function to only show one asteroid
    :param event: tkinter event object from the GUI to indicate which item was clicked on
    :type event: tkinter.Event
    :return: None
    """
    item = ast_tree.selection()[0]
    item_text = ast_tree.item(item, 'text')
    msg = f"{actions.get(5)} {item_text} was clicked, GUI event {event}"
    logging.warning(msg)
    asteroid_data_handler(item_text)


def on_exit():
    """ Custom tkinter method that will write a log entry upon exit
    :return: None
    """
    status_label.config(text="Status: Exited")
    logging.warning(actions.get(2))
    index.destroy()


def clear_gui():
    """ Clears gui from all neos
       :return: None
    """
    for item in ast_tree.get_children():
        ast_tree.delete(item)


def list_sorter(full_list, sort_by):
    """
    TODO
    """
    # sort_by index
    if not sort_by:
        return full_list
    else:
        return sorted(full_list, key=lambda x: x[sort_by])


def sorted_by_name():
    """
    TODO
    """
    asteroid_data_handler(sorted_by=0)
    logging.warning(f"{actions.get(6)}: NAME")


def sorted_by_distance_au():
    """
    TODO
    """
    asteroid_data_handler(sorted_by=1)
    logging.warning(f"{actions.get(6)}: AU")


def sorted_by_distance_miles():
    """
    TODO
    """
    asteroid_data_handler(sorted_by=2)
    logging.warning(f"{actions.get(6)}: MILES")


def sorted_by_threat():
    """
    TODO
    """
    asteroid_data_handler(sorted_by=3)
    logging.warning(f"{actions.get(6)}: THREAT")


def sorted_by_velocity():
    """
    TODO
    """
    asteroid_data_handler(sorted_by=4)
    logging.warning(f"{actions.get(6)}: VELOCITY")


def sorted_by_closest_approach():
    """
    TODO
    """
    asteroid_data_handler(sorted_by=5)
    logging.warning(f"{actions.get(6)}: CLOSEST APPROACH")


def sorted_by_trajectory_date():
    """
    TODO
    """
    asteroid_data_handler(sorted_by=6)
    logging.warning(f"{actions.get(6)}: TRAJECTORY")


def asteroid_data_handler(text="", sorted_by=None):
    """ Gets data from the search text field and searches the database for that asteroid.
    If it is the first time calling this function, it populates the whole list of NEOs in the GUI
    :return: None
    """
    if not text:
        text = asteroid_name_entry.get()
    if text and len(ast_tree.get_children()) > 0:
        valid_name = False
        # Checks if a user searches for an invalid asteroid
        for i in range(0, count):
            if text.strip() == db['data'][i][0]:
                valid_name = True
        if not valid_name:
            messagebox.showinfo("Warning", f"Invalid asteroid name: {text}")
            return
        name, dist_min, dist_min_miles, threat, velocity, ca_date, impact_date = be.asteroid(db, text, count)
        for item in ast_tree.get_children():
            ast_tree.delete(item)
        ast_tree.insert('',
                        'end',
                        text=name,
                        values=(name, dist_min, dist_min_miles, threat, velocity, ca_date, impact_date)
                        )
        # Log SEARCH type and data on the asteroid
        msg = f"{actions.get(3)} {name}, {dist_min}, {dist_min_miles}, {threat}, {velocity}, {ca_date}, {impact_date}"
        logging.warning(msg)

        # Define dtg_value and event_type_value for logging
        dtg = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        event = actions.get(3)  # This gets the event TYPE for SEARCH action

        # Log the same data to the log_tree
        log_tree.insert(
            '', 'end', values=(name, dist_min, dist_min_miles, threat, velocity, ca_date, impact_date, dtg, event))

    # Populating GUI with one NEO data
    else:
        clear_gui()
        data_list = []
        for i in range(count):
            name, dist_min, dist_min_miles, threat, velocity, ca_date, impact_date = be.asteroid(
                db,  db['data'][i][0], count)
            data_list.append([name, dist_min, dist_min_miles, threat, velocity, ca_date, impact_date])
            data_list = list_sorter(data_list, sorted_by)
        # loop through sorted data list and insert to the gui
        for neo in data_list:
            ast_tree.insert(
                '', 'end', text=neo[0], values=(neo[0], neo[1], neo[2], neo[3], neo[4], neo[5], neo[6]))
            # '', 'end', text=name, values=(name, dist_min, dist_min_miles, threat, velocity, ca_date, impact_date))


# Initialize variables
db = {}
count = 0

# Create the main window as index and set default window size
index = tk.Tk()
index.title("Near Earth Objects Viewer")
index.geometry("1070x680")
index.resizable(False, False)

# Font for labels
bold_font = ("TkDefaultFont", 12, "bold")

# Create a label to display the status
status_label = ttk.Label(index, text="Status: Starting...")
status_label.grid(row=5, column=0, columnspan=2, pady=5)

# Create a new label to contain a title
main_title = ttk.Label(index, text="Near Earth Objects Viewer")
main_title.grid(row=0, column=1, pady=30, padx=160, sticky='W')
main_title.config(font=("TkDefaultFont", 20, "bold"))

# Search frame
search_frame = ttk.Frame(index)
search_frame.grid(row=1, column=1, sticky="W")

# Create a Frame to house asteroid list
asteroid_list_fame = ttk.Frame(index)
asteroid_list_fame.grid(row=2, column=0, columnspan=2)

# Frame to house logs
log_frame = ttk.Frame(index)
log_frame.grid(row=3, column=0, columnspan=2, sticky='EW')

# Create a frame to house buttons
button_frame = ttk.Frame(index)
button_frame.grid(row=4, column=0, columnspan=2)

# Image link https://th.bing.com/th?id=OIF.d%2fCjgd%2fJ42C1VjiLa2RSXg&pid=ImgDet&rs=1
img = tk.PhotoImage(file="asteroid.gif")
imagelab = ttk.Label(index, image=img)
imagelab.grid(row=0, column=0, rowspan=2, sticky='EW')

# Asteroid List
ast_label = ttk.Label(asteroid_list_fame, text="Current Known Asteroids",
                      background="grey", font=bold_font)
ast_label.configure(anchor="center")
ast_label.grid(row=0, column=0, sticky="EW")

# API fields: Designation (des), Distance (dist)
asteroid_columns = ("Designation", "Distance (AU)", "Distance (Miles)", "Threat", "Velocity", "Closest Approach",
                    "Date if trajectory changed")
ast_tree = ttk.Treeview(asteroid_list_fame, columns=asteroid_columns, show='headings')
ast_tree.grid(row=1, column=0)
ast_tree.bind("<<TreeviewSelect>>", on_item_click)

for col in asteroid_columns:
    ast_tree.heading(col, text=col)
    ast_tree.column(col, anchor="center", stretch=False, width=150)

# Log Label
log_label = ttk.Label(log_frame, text="Event Logs",
                      background="grey", foreground="black", font=bold_font)
log_label.configure(anchor="center")
log_label.grid(row=0, column=0, sticky="EW")

# Log Treeview
log_columns = ("Asteroid", "Au Distance", "Distance Miles", "threat", "Velocity", "Closest approach", "Impact date",
               "DTG", "Event Type")
log_tree = ttk.Treeview(log_frame, columns=log_columns, show='headings')
log_tree.grid(row=1, column=0, sticky='EW')
# Creates widths for each log column
column_widths = [117, 97, 117, 77, 85, 155, 134, 154, 114]
for col, width in zip(log_columns, column_widths):
    log_tree.heading(col, text=col)
    log_tree.column(col, anchor="center", stretch=True, width=width)

# Asteroid search bar
asteroid_name = tk.StringVar()
asteroid_name_label = ttk.Label(search_frame, text="Asteroid Name:", width=14, font=14)
asteroid_name_label.grid(row=0, column=0)
asteroid_name_entry = ttk.Entry(search_frame, width=60, textvariable=asteroid_name)
asteroid_name_entry.grid(row=0, column=1)
search_button = ttk.Button(search_frame, text="Search", width=10, command=asteroid_data_handler)
search_button.grid(row=0, column=2)

# Scroll bars for ast list and log list
ast_scroll = ttk.Scrollbar(asteroid_list_fame, orient="vertical", command=ast_tree.yview)
log_scroll = ttk.Scrollbar(log_frame, orient="vertical", command=log_tree.yview)
ast_scroll.grid(row=1, column=1, sticky="ns")
log_scroll.grid(row=1, column=1, sticky="ns")

# Set scroll commands
ast_tree["yscrollcommand"] = ast_scroll.set
log_tree["yscrollcommand"] = log_scroll.set

# Create an exit button
exit_button = ttk.Button(button_frame, text="Exit", command=index.destroy)
exit_button.grid(row=0, column=0)

# Create Sorting buttons
sort_name_button = ttk.Button(button_frame, text="Sort by Name", command=sorted_by_name)
sort_name_button.grid(row=0, column=1)
sort_au_button = ttk.Button(button_frame, text="Sort by AU", command=sorted_by_distance_au)
sort_au_button.grid(row=0, column=2)
sort_miles_button = ttk.Button(button_frame, text="Sort by Miles", command=sorted_by_distance_miles)
sort_miles_button.grid(row=0, column=3)
sort_threat_button = ttk.Button(button_frame, text="Sort by Threat", command=sorted_by_threat)
sort_threat_button.grid(row=0, column=4)
sort_velocity_button = ttk.Button(button_frame, text="Sort by Velocity", command=sorted_by_velocity)
sort_velocity_button.grid(row=0, column=5)
sort_ca_button = ttk.Button(button_frame, text="Sort by CA", command=sorted_by_closest_approach)
sort_ca_button.grid(row=0, column=6)
sort_traj_button = ttk.Button(button_frame, text="Sort by TRAJ", command=sorted_by_trajectory_date)
sort_traj_button.grid(row=0, column=7)


# Run mainloop
if __name__ == '__main__':
    DAYS = 30  # NEOs approaching filter limit in days
    api_data = be.neos_approaching(DAYS)
    db = json.loads(api_data.content)
    count = db['count']

    # Logging configurations
    FORMAT = '%(asctime)s - %(message)s'
    current_date = dt.datetime.now().strftime("%Y-%b-%d")
    # I had to add my desktop filepath in, but it worked.
    LOG_FILENAME = f"{current_date}.txt"
    logging.basicConfig(filename=LOG_FILENAME,
                        level=logging.WARNING,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%b-%d %H:%M:%S')

    actions = {1: "START", 2: "STOP", 3: "SEARCH", 4: "ERROR", 5: "GUI EVENT", 6: "SORT EVENT"}
    logging.warning(actions.get(1))

    if api_data.status_code == 200:
        status_label.config(text="Status: Started")
        asteroid_data_handler()
        index.mainloop()
        logging.warning(actions.get(2))
    else:
        status_label.config(text="Status: Error")
        print("Something wrong, could not fetch data. Exiting.")
        logging.warning(actions.get(4))
        sys.exit(1)
