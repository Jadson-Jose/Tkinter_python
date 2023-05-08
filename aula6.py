import customtkinter as ctk

window = ctk.CTk()
window.title("App Teste")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)

tabview = ctk.CTkTabview(window, width=400, corner_radius=20, border_width=1, border_color="red", fg_color="teal",
                         segmented_button_fg_color="red", segmented_button_selected_color="green",
                         segmented_button_selected_hover_color="blue", segmented_button_unselected_color="yellow")
tabview.pack()
tabview.add("Names")
tabview.add("Age")
tabview.add("Sex")
tabview.tab("Names").grid_columnconfigure(0, weight=1)
tabview.tab("Age").grid_columnconfigure(0, weight=1)
tabview.tab("Sex").grid_columnconfigure(0, weight=1)

text = ctk.CTkLabel(tabview.tab("Names"), text="Jadson Silva\nMarcia Nina\nMaria\nJoao")
text.pack()

idd = ctk.CTkLabel(tabview.tab("Age"), text="42\n35\n20\n42")
idd.pack()

idd = ctk.CTkLabel(tabview.tab("Sex"), text="Masculino\nFeminino\nFeminino\nMasculino")
idd.pack()


window.mainloop()
