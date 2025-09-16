import customtkinter as ctk
import PIT_calculator as PIT

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Personal Income Tax Calculator")
app.geometry("400x300")

# Label
label = ctk.CTkLabel(app, text="Enter Annual Income")
label.pack(pady=(20, 5))

# Small Textbox (Entry)
textbox = ctk.CTkEntry(app, placeholder_text="Type a number...")
textbox.pack(pady=10)

# Label
label2 = ctk.CTkLabel(app, text="Enter Monthly Income")
label2.pack(pady=(20, 5))

# Small Textbox (Entry)
textbox2 = ctk.CTkEntry(app, placeholder_text="Type a number...")
textbox2.pack(pady=10)

# Result label (initially empty)
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)


def parse_input (string):
    string = string.replace(" ","")
    string = string.replace(",","")
    string = float(string)
    return string

def display_num(num):
    return "{:,}".format(num)
    


# Button action
def multiply_input():
    try:
        if textbox.get() and textbox.get():
            result_label.configure(text="Please enter a number into only one field!")
        elif textbox.get():
            value = parse_input(textbox.get())
            value = PIT.PIT(value)  # convert input to number
            value = display_num(value)
            result_label.configure(text=f"Result: {value}")
        elif textbox2.get():
            value = parse_input(textbox2.get()) # convert input to number
            value = value * 12
            value = PIT.PIT(value)  # convert input to number
            value = display_num(value)
            result_label.configure(text=f"Result: {value}")

    except ValueError:
        result_label.configure(text="Please enter a valid number!")

button = ctk.CTkButton(app, text="Calculate Personal Income Tax", command=multiply_input)
button.pack(pady=10)

app.mainloop()
