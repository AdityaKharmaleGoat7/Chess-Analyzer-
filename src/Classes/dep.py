import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from analyzer import Analyzer

def analyze_game():
    # Check if a file is selected or if a FEN string is entered
    if file_radio_var.get() == "file":
        # Ask the user to select a PGN file
        file_path = filedialog.askopenfilename(filetypes=[("PGN Files", "*.pgn")])
        if not file_path:
            result_label.config(text="No file selected.", fg="#e74c3c")
            return

        file_label.config(text=f"File: {file_path.split('/')[-1]}", fg="#2ecc71")
        fen_input = None  # No FEN string
    elif file_radio_var.get() == "fen":
        # Get FEN string from entry field
        fen_input = fen_entry.get().strip()
        if not fen_input:
            result_label.config(text="Please enter a FEN string.", fg="#e74c3c")
            return
        file_label.config(text="FEN String Provided", fg="#2ecc71")
        file_path = None  # No file selected
    else:
        result_label.config(text="Please select an input method.", fg="#e74c3c")
        return

    result_label.config(text="Analyzing, please wait...", fg="#f1c40f")

    try:
        # Get the analysis depth and position
        depth = int(depth_entry.get())
        pos = pos_var.get()
        
        # If file input is selected, pass the file path to the Analyzer.
        # If FEN input is selected, pass the FEN string.
        analyzer = Analyzer(file_path if file_path else fen_input, depth, pos)
        result = analyzer.analyze()  # Assuming it returns the result
        result_label.config(text=result, fg="#2ecc71")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="#e74c3c")

# Root Window
root = tk.Tk()
root.title("Chess Analyzer")
root.geometry("500x500")  # Increased window size for FEN input
root.configure(bg="#34495e")  # Background color

# Gradient Background Frame
gradient = tk.Canvas(root, width=500, height=500, bg="#34495e", highlightthickness=0)
gradient.pack(fill=tk.BOTH, expand=True)
gradient.create_rectangle(0, 0, 500, 200, fill="#2c3e50", outline="")
gradient.create_rectangle(0, 200, 500, 500, fill="#34495e", outline="")

# Title Label
title_label = tk.Label(
    root,
    text="Chess Analyzer",
    font=("Helvetica", 24, "bold"),
    fg="#ecf0f1",
    bg="#2c3e50",
)
title_label.place(x=150, y=20)

# Depth Input
depth_label = tk.Label(root, text="Analysis Depth:", font=("Helvetica", 12), fg="#ecf0f1", bg="#34495e")
depth_label.place(x=50, y=100)
depth_entry = ttk.Entry(root, width=10)
depth_entry.insert(0, "12")  # Placeholder for default depth
depth_entry.place(x=200, y=100)

# Position Selector
pos_label = tk.Label(root, text="Player Position:", font=("Helvetica", 12), fg="#ecf0f1", bg="#34495e")
pos_label.place(x=50, y=140)
pos_var = tk.StringVar(value="white")
pos_dropdown = ttk.OptionMenu(root, pos_var, "white", "white", "black")
pos_dropdown.place(x=200, y=140)

# File/FEN Selection
file_radio_var = tk.StringVar(value="file")

file_radio = ttk.Radiobutton(root, text="Select PGN File", variable=file_radio_var, value="file", command=lambda: toggle_input_method("file"))
file_radio.place(x=50, y=180)
fen_radio = ttk.Radiobutton(root, text="Enter FEN String", variable=file_radio_var, value="fen", command=lambda: toggle_input_method("fen"))
fen_radio.place(x=200, y=180)

# FEN Input
fen_label = tk.Label(root, text="FEN String:", font=("Helvetica", 12), fg="#ecf0f1", bg="#34495e")
fen_label.place(x=50, y=220)
fen_entry = ttk.Entry(root, width=30)
fen_entry.place(x=200, y=220)
fen_entry.config(state="disabled")

# File Selection Label
file_label = tk.Label(
    root,
    text="No file selected",
    font=("Helvetica", 10),
    fg="#e74c3c",
    bg="#34495e"
)
file_label.place(x=50, y=260)

# Analyze Button
analyze_button = tk.Button(
    root,
    text="Analyze Game",
    font=("Helvetica", 12),
    bg="#16a085",
    fg="#ecf0f1",
    activebackground="#1abc9c",
    activeforeground="#ecf0f1",
    relief="flat",
    command=analyze_game,
    padx=10,
    pady=5,
)
analyze_button.place(x=200, y=300)

# Result Display
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 12),
    wraplength=400,
    fg="#ecf0f1",
    bg="#34495e",
    height=4,
    width=40,
    relief="groove",
    bd=2,
)
result_label.place(x=50, y=350)

# Builder Credit
credit_label = tk.Label(
    root,
    text="Built by Aditya Kharmale",
    font=("Helvetica", 10, "italic"),
    fg="#95a5a6",
    bg="#34495e",
)
credit_label.place(x=180, y=470)

# Function to toggle between file and FEN input
def toggle_input_method(method):
    if method == "file":
        fen_entry.config(state="disabled")
    elif method == "fen":
        fen_entry.config(state="normal")

root.mainloop()
