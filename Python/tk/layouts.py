import tkinter as tk

root = tk.Tk()
#root.geometry('250x170')

label1 = tk.Label(root, text='Label 1')
entry1 = tk.Entry(root)

label2 = tk.Label(root, text='Label 2')
entry2 = tk.Entry(root)

button1 = tk.Button(root, text='Button 1')
button2 = tk.Button(root, text='Button 2')


"""
Pack Method

label1.pack(padx=5, pady=5, side=tk.LEFT)
entry1.pack(padx=5, pady=5, side=tk.LEFT)

label2.pack(padx=5, pady=5, side=tk.LEFT)
entry2.pack(padx=5, pady=5, side=tk.LEFT)

button1.pack(padx=5, pady=5)
button2.pack(padx=5, pady=5)

#Grid Method

label1.grid(row=0,column=0, padx=5, pady=5)
entry1.grid(row=0,column=1, padx=5, pady=5)
label2.grid(row=1,column=0, padx=5, pady=5)
entry2.grid(row=1,column=1, padx=5, pady=5)
button1.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
button2.grid(row=3, column=0, padx=5, pady=5,columnspan=2)
"""

#Pack Method

label1.pack(padx=5, pady=5, expand=True, fill=tk.X)
entry1.pack(padx=5, pady=5, expand=True, fill=tk.X)

label2.pack(padx=5, pady=5, expand=True, fill=tk.X)
entry2.pack(padx=5, pady=5, expand=True, fill=tk.X)

button1.pack(padx=5, pady=5, expand=True, fill=tk.X)
button2.pack(padx=5, pady=5, expand=True, fill=tk.X)
"""
#Place Method

label1.place(x=10, y=10)
entry1.place(x=70, y=10)
label2.place(x=10, y=50)
entry2.place(x=70, y=50)

"""

root.mainloop()