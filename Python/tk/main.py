"""
    #Add widgets in grid

    lbl = tk.Label(root, text="Label 1")    #Create label, pass in root
    lbl.grid(row=0, column=0) #Add to grid

    print(lbl.config().keys()) # Print out all the possibile config keys
    
    btn = tk.Button(root, text="Button 1", command=on_click)  #Add button, pass the root (main window). on_click references function above
    btn.grid(row=0, column=1)      #Add button to window with geometry managers to specify how to add to window

"""

import tkinter as tk
from tkinter import ttk 


def add_to_list(event=None):
    text = entry.get()  # Get the current value of the entry widget
    if text: #If not null
        text_list.insert(tk.END, text) #Insert at the END of the text list (tk.END) - the end of the content of the widget.
        entry.delete(0, tk.END) # Delete content of entry widget from BEGINNING, to END


if __name__== '__main__':

    root = tk.Tk()    #Initialize Main window
    root.title("Simple TKinter App")    #Change title of main window

    #configure rows/columns
    root.columnconfigure(0, weight=1) # set weight for column 0 (1 of 4)
    root.columnconfigure(1, weight=3) # set weight for column 1 (3 of 4)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    frame = ttk.Frame(root)  #Create a frame. A container to hold/organize widgets- USE TTK for theme widgets.
    frame.grid(row=0, column=0, sticky="nsew",padx=5,pady=5) #Add frame to grid. Make stick to north/south/east/west. Add x/y padding
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    
    entry = ttk.Entry(frame) #Pass frame instead of root
    entry.grid(row=0, column=0, sticky="ew") # Add to grid, which has its own columns and rows in the frame

    entry.bind("<Return>", add_to_list) # Bind key to entry widget, (key, function). Function has to accept 'event'

    entry_btn = ttk.Button(frame, text="Add",command=add_to_list)
    entry_btn.grid(row=0, column=1)

    text_list = tk.Listbox(frame) # List box widget, add to frame
    text_list.grid(row=1, column=0,columnspan=2, sticky="nsew") # Add to grid, tell it to span 2 columns. Stick to East West

    frame2 = tk.Frame(root)  #Create a frame. A container to hold/organize widgets
    frame2.grid(row=0, column=1, sticky="nsew",padx=5,pady=5) #Add frame to grid. Make stick to north/south/east/west
    frame2.columnconfigure(0, weight=1)
    frame2.rowconfigure(1, weight=1)
    
    entry = tk.Entry(frame2) #Pass frame instead of root
    entry.grid(row=0, column=0, sticky="ew") # Add to grid, which has its own columns and rows in the frame

    entry.bind("<Return>", add_to_list) # Bind key to entry widget, (key, function). Function has to accept 'event'

    entry_btn = tk.Button(frame2, text="Add",command=add_to_list)
    entry_btn.grid(row=0, column=1)

    text_list = tk.Listbox(frame2) # List box widget, add to frame
    text_list.grid(row=1, column=0,columnspan=2, sticky="nsew") # Add to grid, tell it to span 2 columns. Stick to East West

   
    root.mainloop()  #create main loop for tkinter
