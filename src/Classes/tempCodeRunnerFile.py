import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from analyzer import Analyzer

def analyze_game():
    file_path = filedialog.askopenfilename(filetypes=[("PGN Files", "*.pgn")])
    if not file_path:
        result_label.config(text="No file selected.", fg="#e74c3c")
        return

    file_label.config(text=f"File: {file_path.split('/')[-1]}", fg="#2ecc71")
    result_label.config(text="Analyzing, please wait...", fg="#f1c40f")
    try:
        depth = int(depth_entry.get())
        pos = pos_var.get()
        analyzer = Analyzer(file_path, depth, pos)
        result = analyzer.analyze()  # Assuming it returns the result
        result_label.config(text=result, fg="#2ecc71")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="#e74c3c")

# Root Window
root = tk.Tk()
root.title("Chess Analyzer")
root.geometry("500x400")  # Increased window size
root.configure(bg="#34495e")  # Background color

# Add Icon (optional, needs .ico file in same directory)
# root.iconbitmap("icon.ico")

# Gradient Background Frame
gradient = tk.Canvas(root, width=500, height=400, bg="#34495e", highlightthickness=0)
gradient.pack(fill=tk.BOTH, expand=True)
gradient.create_rectangle(0, 0, 500, 200, fill="#2c3e50", outline="")
gradient.create_rectangle(0, 200, 500, 400, fill="#34495e", outline="")

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

# File Selection Label
file_label = tk.Label(
    root,
    text="No file selected",
    font=("Helvetica", 10),
    fg="#e74c3c",
    bg="#34495e"
)
file_label.place(x=50, y=180)

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
analyze_button.place(x=200, y=220)

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
result_label.place(x=50, y=270)

# Builder Credit
credit_label = tk.Label(
    root,
    text="Built by Aditya Kharmale",
    font=("Helvetica", 10, "italic"),
    fg="#95a5a6",
    bg="#34495e",
)
credit_label.place(x=180, y=370)

root.mainloop()
