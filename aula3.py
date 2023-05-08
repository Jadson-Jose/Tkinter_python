import customtkinter as ctk

window = ctk.CTk()
window.title("App Teste")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)
window._set_appearance_mode("system")


window.mainloop()
