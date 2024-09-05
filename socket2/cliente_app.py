import tkinter as tk  

root = tk.Tk()  
root.geometry("350x350")
root.title("MyApp")
root.config(bg="#181821")
label = tk.Label(root, text="Qual item você deseja procurar?", fg="white", bg="#181821")
label.place(relx=0.490, rely=0.1, anchor="center")
btn = tk.Button(root, width=24, text="Enviar para o servidor", foreground="white", bg="#3baea0", font=('Arial', 12))
btn.place(relx=0.180, rely=0.6)
root.mainloop()