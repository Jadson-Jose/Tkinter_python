import customtkinter as ctk

window = ctk.CTk()
window.title("App Teste")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)


frame_1 = ctk.CTkFrame(master=window, width=200, height=330, fg_color="teal", bg_color="transparent", border_width=10,
                       corner_radius=30, border_color="red").place(x=10, y=60)

frame_2 = ctk.CTkFrame(window, width=200, height=330, fg_color="green").place(x=230, y=60)
frame_3 = ctk.CTkFrame(window, width=200, height=330, fg_color="white").place(x=450, y=60)

window.mainloop()
