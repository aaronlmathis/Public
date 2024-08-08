import tkinter as tk


def on_click():
    lbl.config(text="Button Clicked")

if __name__== '__main__':
    root = tk.Tk()    #Initialize Main window
    root.title("Simple TKinter App")    #Change title of main window

    #Add widgets in grid

    lbl = tk.Label(root, text="Label 1")    #Create label, pass in root
    lbl.grid(row=0, column=0) #Add to grid

    print(lbl.config().keys()) # Print out all the possibile config keys
    
    btn = tk.Button(root, text="Button 1", command=on_click)  #Add button, pass the root (main window). on_click references function above
    btn.grid(row=0, column=1)      #Add button to window with geometry managers to specify how to add to window

   
    root.mainloop()  #create main loop for tkinter
