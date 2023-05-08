import customtkinter as ctk

window = ctk.CTk()
window.title("App Teste")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)

textbox = ctk.CTkTextbox(window, width=300, height=350, scrollbar_button_color="green",
                         scrollbar_button_hover_color="red", border_color="red", border_width=2,
                         corner_radius=15, fg_color="teal", border_spacing=20, activate_scrollbars=True)
textbox.pack()

textbox.insert("0.0", "Titulo do seu texto\n\n" + "Ola dev, estou aqui programando interfaces graficas com o"
                                              "custom Tkinter.\n\n"*20)


window.mainloop()
