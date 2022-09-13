import tkinter

window = tkinter.Tk()
window.title("My first project")
window.minsize(width=500, height=300)

window_label = tkinter.Label(text="Whats up mf", font=("Arial", 24))
window_label.pack()

window.mainloop()