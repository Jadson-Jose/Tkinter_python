import customtkinter as ctk

window = ctk.CTk()
window.title("App Teste")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)

ctk.CTkLabel(window, text="Menu de opcoes. Aula - 09", font=("arial bold", 20)).pack(pady=20, padx=5)

ctk.CTkLabel(window, text="Escolha o seu mes de nascimento: ", font=("arial bold", 14)).pack()

mes = ctk.CTkOptionMenu(window,
                  values=["Janeiro", "Fevereiro", "marco", "Abril", "Maio", "junho", "Outros..."])
mes.pack(pady=10)
mes.set("Maio")
window.mainloop()
