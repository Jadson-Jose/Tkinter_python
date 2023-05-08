import customtkinter as ctk

window = ctk.CTk()
window.title("App Teste")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)
window._set_appearance_mode("system")


def new_screen():
    new_window = ctk.CTkToplevel(window, fg_color="teal")
    new_window.geometry("500x250")


btn_new_screen = ctk.CTkButton(master=window, text="Open new window", command=new_screen).place(x=300, y=100)

window.mainloop()
