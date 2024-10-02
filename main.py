import tkinter as tk
win = tk.Tk()
win.geometry('350x250')
win.title('Unit Converter')
heading = tk.Label(win, text="Unit Converter", font=("Georgia", 20) , fg='blue' , background='#ccffff').pack()
conversion_val = {
    # Length Conversions
    'kilometer to meter': 1000.0, 
    'meter to kilometer': 0.001,  
    'centimeter to meter': 0.01,  
    'meter to centimeter': 100.0, 
    'millimeter to meter': 0.001,  
    'meter to millimeter': 1000.0,
    'inch to centimeter': 2.54,  
    'centimeter to inch': 0.393701,  
    'foot to meter': 0.3048,  
    'meter to foot': 3.28084,  
    'yard to meter': 0.9144,  
    'meter to yard': 1.09361,  
    'mile to kilometer': 1.60934,  
    'kilometer to mile': 0.621371,  

    # Mass Conversions
    'kilogram to gram': 1000.0, 
    'gram to kilogram': 0.001, 
    'pound to kilogram': 0.453592,  
    'kilogram to pound': 2.20462,  
    'ounce to gram': 28.3495,  
    'gram to ounce': 0.035274,  

    # Time Conversions
    'second to minute': 1 / 60.0,  
    'minute to second': 60.0,
    'minute to hour': 1 / 60.0,  
    'hour to minute': 60.0,
    'hour to day': 1 / 24.0,  
    'day to hour': 24.0,
    'day to week': 1 / 7.0,  
    'week to day': 7.0,
    'month to year': 1 / 12.0,  
    'year to month': 12.0,

    # Volume Conversions
    'liter to milliliter': 1000.0,
    'milliliter to liter': 0.001,  
    'gallon to liter': 3.78541,  
    'liter to gallon': 0.264172,  
    'cup to milliliter': 240.0,  
    'milliliter to cup': 0.00422675,  
    'cubic meter to liter': 1000.0,
    'liter to cubic meter': 0.001,

    # Temperature Conversions (constants used for conversion)
    'celsius to fahrenheit': 1.8,  # (celsius * 1.8) + 32
    'fahrenheit to celsius': 0.555556,  # (fahrenheit - 32) * 0.555556
    'celsius to kelvin': 273.15,  
    'kelvin to celsius': -273.15,  

    # Area Conversions
    'square meter to square kilometer': 1e-6,  
    'square kilometer to square meter': 1000000.0,
    'square foot to square meter': 0.092903,  
    'square meter to square foot': 10.7639,  
    'acre to square meter': 4046.86,  
    'square meter to acre': 0.000247105,  

    # Speed Conversions
    'meter per second to kilometer per hour': 3.6,  
    'kilometer per hour to meter per second': 0.277778,  
    'mile per hour to kilometer per hour': 1.60934,  
    'kilometer per hour to mile per hour': 0.621371,  

    # Data Storage Conversions
    'byte to kilobyte': 1 / 1024.0,  
    'kilobyte to byte': 1024.0,
    'kilobyte to megabyte': 1 / 1024.0,  
    'megabyte to kilobyte': 1024.0,
    'megabyte to gigabyte': 1 / 1024.0,  
    'gigabyte to megabyte': 1024.0,
    'gigabyte to terabyte': 1 / 1024.0,  
    'terabyte to gigabyte': 1024.0
}



list_of_units = list(conversion_val.keys())

# menu for select units to convert
optionvalue = tk.StringVar()
optionvalue.set(list_of_units[0])
options_menu = tk.OptionMenu(win, optionvalue , *list_of_units)
options_menu.pack(pady=15)


# entry for input value

# function for entry click
def on_entry_click(event):
   if entry.get() == "Enter Value:":
      entry.delete(0, tk.END)
      entry.configure(foreground="black")

def on_focus_out(event):
   if entry.get() == "":
      entry.insert(0, "Enter Value:")
      entry.configure(foreground="gray")

# entry logic
entry = tk.Entry(win, width=17)
entry.insert(0, 'Enter Value:') 
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)
entry.pack(pady=15)

result_label = None
def convert():
    global result_label
    try: 
        if result_label is not None:
            result_label.destroy()
        result_label = tk.Label(win, text=f'{float(entry.get()) * conversion_val[optionvalue.get()]} {optionvalue.get().split()[2]}', font=("Futura", 12))
        result_label.pack()
    
    except:
        if result_label is not None:
           result_label.destroy()
        result_label = tk.Label(win, text= 'Only Integer and Float Value Accepted', font=("Futura", 12))
        result_label.pack()
             


# button for convert

show = tk.Button(win, text="Convert" , command=convert , bg="#333333" , fg="white" , font=("Futura", 15)) 
show.pack()
win.mainloop()
# NOTE: All code is written by me , except dictionary of different units and conversion rates
