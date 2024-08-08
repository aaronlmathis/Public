"""
widgets.py

Display grid of all TKInter widgets.

"""

import tkinter as tk
from tkinter import ttk 

# Event Handler functions



if __name__=='__main__':
    
    root = tk.Tk()    #Initialize Main window
    root.title("Simple TKinter App")    #Change title of main window

    #configure rows/columns
    root.columnconfigure(0, weight=1) # set weight for column 0 (1 of 4)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    frame1 = ttk.Frame(root,borderwidth=1, relief='sunken', padding=5)  #Create a frame. A container to hold/organize widgets- USE TTK for theme widgets.
    frame1.grid(row=0, column=0, sticky="nsew",padx=5,pady=5) #Add frame to grid. Make stick to north/south/east/west. Add x/y padding
    frame1.columnconfigure(0, weight=1)
    frame1.rowconfigure(1, weight=1)
    
    #Row 1
    btn_lbl = ttk.Label(frame1, text="Button: ")    #Create label, pass in root
    btn_lbl.grid(row=0, column=0,padx=5,pady=5) #Add to grid

    btn = ttk.Button(frame1, text="Button 1")  #Add button, pass the root (main window). on_click references function above
    btn.grid(row=0, column=1,padx=5,pady=5)      #Add button to window with geometry managers to specify how to add to window

    cmb_box_lbl = ttk.Label(frame1, text="ComboBox:")
    cmb_box_lbl.grid(row=1, column=0, padx=5,pady=5)

    cmb_box = ttk.Combobox(frame1, text="Combo Box")
    cmb_box.grid(row=1,column=1, padx=5,pady=5)
    
    #Frame 2
    frame2 = ttk.Frame(root,borderwidth=1, relief='solid', padding=5)  #Create a frame. A container to hold/organize widgets- USE TTK for theme widgets.
    frame2.grid(row=1, column=0, sticky="nsew",padx=5,pady=5) #Add frame to grid. Make stick to north/south/east/west. Add x/y padding
    frame2.columnconfigure(0, weight=1)
    frame2.rowconfigure(1, weight=1)
    
    #Row 1
    chk_btn_lbl = ttk.Label(frame2, text="CheckButton: ")    #Create label, pass in root
    chk_btn_lbl.grid(row=0, column=0) #Add to grid

    chk_btn = ttk.Checkbutton(frame2, text="Check Button")  #Add button, pass the root (main window). on_click references function above
    chk_btn.grid(row=0, column=1)      #Add button to window with geometry managers to specify how to add to window

    rad_btn_lbl = ttk.Label(frame2, text="RadioButton: ")
    rad_btn_lbl.grid(row=1,column=0)

    rad_btn = ttk.Radiobutton(frame2, text="Radio Button")
    rad_btn.grid(row=1, column=1)




    root.mainloop()  #create main loop for tkinter