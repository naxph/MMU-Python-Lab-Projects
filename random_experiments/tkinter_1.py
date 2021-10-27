import tkinter as tk 

mainWindow = tk.Tk()

mainFrame = tk.Frame()
subFrame = tk.Frame()

mainLabel = tk.Label(text="Enter your name:", foreground="blue", background="yellow", master=mainFrame)
mainLabel.pack()

mainEntry = tk.Entry(width=50,master=mainFrame)
mainEntry.insert(0, "Heng Yep Gay")
mainEntry.pack()

mainButton = tk.Button(text="Click Me!", width=25, height=5, master=subFrame)
mainButton.pack()

mainFrame.pack()
subFrame.pack()

mainWindow.mainloop()