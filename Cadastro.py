import tkinter as tk
from tkinter import ttk, messagebox

# Lista para armazenar os cadastros
cadastros = []

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    estado = entry_estado.get()
    cidade = entry_cidade.get()
    pais = entry_pais.get()

    if not nome or not email:
        messagebox.showwarning("Campos obrigatórios", "Nome e E-mail são obrigatórios.")
        return

    dados = {
        "Nome": nome,
        "Email": email,
        "Estado": estado,
        "Cidade": cidade,
        "País": pais
    }
    cadastros.append(dados)
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    atualizar_visualizacao()
    limpar_campos()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_pais.delete(0, tk.END)

def atualizar_visualizacao():
    for item in tree.get_children():
        tree.delete(item)
    for i, cadastro in enumerate(cadastros):
        tree.insert("", "end", values=(cadastro["Nome"], cadastro["Email"], cadastro["Estado"], cadastro["Cidade"], cadastro["País"]))

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro com Abas")

# Notebook (abas)
notebook = ttk.Notebook(janela)
notebook.pack(padx=10, pady=10, fill='both', expand=True)

# Aba de Cadastro
aba_cadastro = ttk.Frame(notebook)
notebook.add(aba_cadastro, text='Cadastro')

# Campos de cadastro
tk.Label(aba_cadastro, text="Nome:").grid(row=0, column=0, sticky="e")
entry_nome = tk.Entry(aba_cadastro)
entry_nome.grid(row=0, column=1)

tk.Label(aba_cadastro, text="E-mail:").grid(row=1, column=0, sticky="e")
entry_email = tk.Entry(aba_cadastro)
entry_email.grid(row=1, column=1)

tk.Label(aba_cadastro, text="Estado:").grid(row=2, column=0, sticky="e")
entry_estado = tk.Entry(aba_cadastro)
entry_estado.grid(row=2, column=1)

tk.Label(aba_cadastro, text="Cidade:").grid(row=3, column=0, sticky="e")
entry_cidade = tk.Entry(aba_cadastro)
entry_cidade.grid(row=3, column=1)

tk.Label(aba_cadastro, text="País:").grid(row=4, column=0, sticky="e")
entry_pais = tk.Entry(aba_cadastro)
entry_pais.grid(row=4, column=1)

# Botão cadastrar
btn_cadastrar = tk.Button(aba_cadastro, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=5, column=0, columnspan=2, pady=10)

# Aba de Visualização
aba_visualizar = ttk.Frame(notebook)
notebook.add(aba_visualizar, text='Visualizar Cadastros')

# Tabela de visualização
colunas = ("Nome", "Email", "Estado", "Cidade", "País")
tree = ttk.Treeview(aba_visualizar, columns=colunas, show="headings")

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(fill="both", expand=True)

janela.mainloop()
