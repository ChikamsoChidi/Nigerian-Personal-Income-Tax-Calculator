import customtkinter as ctk
import PIT_calculator as PIT


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Personal Income Tax Calculator")
app.geometry("400x300")
app.configure(fg_color="#b7cce0")  # very pale blue background


# Load PNG image
app.iconbitmap("img.ico")

# Label
label = ctk.CTkLabel(app, text="Enter Income",  font=("Arial", 14, "bold")  )
label.pack(pady=(10, 5))

# Small Textbox (Entry)
textbox = ctk.CTkEntry(app, placeholder_text="Type a number...")
textbox.pack(pady=10)

def checkbox1_action():
    if checkbox.get() == 1:   # If box 1 is checked
        checkbox2.deselect()   # Deselect box 2

def checkbox2_action():
    if checkbox2.get() == 1:   # If box 2 is checked
        checkbox.deselect()   # Deselect box 1


# Checkbox (for monthly salary)
checkbox = ctk.CTkCheckBox(
    app,
    text="Monthly Income",
    command=checkbox1_action,
    fg_color="#e67e22",      # muted orange
    hover_color="#f5b041",   # paler orange on hover
    text_color="black"       # clear text color
)
checkbox.pack(pady=10)

# Checkbox (for annual salary)
checkbox2 = ctk.CTkCheckBox(
    app,
    text="Annual Income",
    command=checkbox2_action,
    fg_color="#e67e22",      # muted orange
    hover_color="#f5b041",   # paler orange on hover
    text_color="black"       # clear text color
)
checkbox2.pack(pady=10)

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
def calculate_result():
    try:
        if checkbox.get() == 0 and checkbox2.get() == 0:
            result_label.configure(text="Select a duration")
        elif checkbox2.get() == 1:
            value = parse_input(textbox.get())
            value = PIT.PIT(value)  # convert input to number
            value = display_num(value)
            result_label.configure(text=f"Personal Income Tax: ₦ {value}")
            
        elif checkbox.get() == 1:
            value = parse_input(textbox.get()) # convert input to number
            value = value * 12
            value = PIT.PIT(value)  # convert input to number
            value = display_num(value)
            result_label.configure(text=f"Personal Income Tax: ₦ {value}")

    except ValueError:
        result_label.configure(text="Please enter a valid number!")

button = ctk.CTkButton(
    app, 
    text="Calculate Personal Income Tax",
    fg_color="#e67e22",      # muted orange (not too bright)
    hover_color="#f5b041",   # paler orange for hover
    text_color="white",      # good contrast
    command=calculate_result
)
button.pack(pady=10)

app.mainloop()
