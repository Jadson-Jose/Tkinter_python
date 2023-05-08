import customtkinter as ctk

window = ctk.CTk()
window.title("App Teste")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)


def open():
    dialog = ctk.CTkInputDialog(title="Box the Dialog", text="Cell Phone Number")
    print("Phone Number: ", dialog.get_input())


btn = ctk.CTkButton(window, text="Open box dialog", command=open)
btn.pack()

window.mainloop()
