import tkinter as tk

def main():
    window = tk.Tk()
    file_text = open('test.txt', 'r').read().split()

main()