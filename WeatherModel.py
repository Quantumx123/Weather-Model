import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


def read_coefficients_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    coefficients = []
    for line in lines:
        a, b, c = map(float, line.strip().split())
        coefficients.append((a, b, c))
    return coefficients


def plot_temperature_model(coefficients):
    # Generate time values
    x = np.linspace(0, 24, 100)

    # Plot each set of coefficients
    for idx, (a, b, c) in enumerate(coefficients):
        y = a*x**2+b*x+c
        plt.plot(x, y, label=f'Temperature  Model {+1}')

    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


def open_file():
    filename = filedialog.askopenfilename(title="Select file",
                                          filetypes=[("Text files",
                                                      "*.txt")])
    if filename:
        coefficients = read_coefficients_from_file(filename)
        plot_temperature_model(coefficients)


root = tk.Tk()
root.title("Weather Modeling Software")

open_button = tk.Button(root, text="Open Coefficients File", command=open_file)
open_button.pack(pady=20)

root.mainloop()
