import tkinter as tk

def fahrenheit_to_celsius():
  fahrenheit = enterTemperature.get()
  celsius = (5/9) * (float(fahrenheit) - 32)
  labelResult["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

mainWindow = tk.Tk()
mainWindow.title("Temperature converter")

frameEntry = tk.Frame(master=mainWindow)
enterTemperature = tk.Entry(master=frameEntry, width=10)
labelTemp = tk.Label(master=frameEntry, text="\N{DEGREE FAHRENHEIT}")
btnConvert = tk.Button(master=mainWindow, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
labelResult = tk.Label(master=mainWindow, text="\N{DEGREE CELSIUS}")

enterTemperature.grid(row=0, column=0, sticky="e")
labelTemp.grid(row=0, column=1, sticky="w")
frameEntry.grid(row=0, column=0, padx=10)
btnConvert.grid(row=0, column=1, pady=10)
labelResult.grid(row=0, column=2, padx=10)

mainWindow.mainloop()