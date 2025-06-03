import tkinter as tk
from tkinter import ttk, messagebox, filedialog

cadastros = []
indice_edicao = None

def cadastrar():
    global indice_edicao

    dados = {
        "Nome": entry_nome.get(),
        "Email": entry_email.get(),
        "Estado": entry_estado.get(),
        "Cidade": entry_cidade.get(),
        "País": entry_pais.get(),
        "Telefone": entry_telefone.get(),
        "Documento": entry_documento.get(),
        "Nascimento": entry_nascimento.get(),
        "Pai": entry_pai.get(),
        "Mãe": entry_mae.get(),
        "Endereço": entry_endereco.get(),
        "Bairro": entry_bairro.get(),
        "Anexo": anexo_path.get()
    }

    if not dados["Nome"] or not dados["Email"]:
        messagebox.showwarning("Campos obrigatórios", "Nome e E-mail são obrigatórios.")
        return

    if indice_edicao is None:
        cadastros.append(dados)
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    else:
        cadastros[indice_edicao] = dados
        indice_edicao = None
        btn_cadastrar.config(text="Cadastrar")
        messagebox.showinfo("Sucesso", "Cadastro editado com sucesso!")

    atualizar_visualizacao()
    limpar_campos()

def limpar_campos():
    global indice_edicao
    for campo in entradas:
        campo.delete(0, tk.END)
    anexo_path.set("")
    indice_edicao = None
    btn_cadastrar.config(text="Cadastrar")

def atualizar_visualizacao():
    tree.delete(*tree.get_children())
    for i, cadastro in enumerate(cadastros):
        tree.insert("", "end", iid=str(i), values=(
            cadastro["Nome"], cadastro["Email"], cadastro["Telefone"], cadastro["Nascimento"]
        ))

def excluir_cadastro():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Seleção necessária", "Selecione um cadastro para excluir.")
        return
    confirm = messagebox.askyesno("Confirmar exclusão", "Tem certeza que deseja excluir este cadastro?")
    if confirm:
        index = int(selected_item[0])
        del cadastros[index]
        atualizar_visualizacao()
        messagebox.showinfo("Excluído", "Cadastro excluído com sucesso!")

def editar_cadastro():
    global indice_edicao
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Seleção necessária", "Selecione um cadastro para editar.")
        return

    index = int(selected_item[0])
    cadastro = cadastros[index]
    indice_edicao = index

    campos = [
        "Nome", "Email", "Estado", "Cidade", "País",
        "Telefone", "Documento", "Nascimento", "Pai", "Mãe",
        "Endereço", "Bairro", "Anexo"
    ]

    for campo, entry in zip(campos, entradas + [anexo_path]):
        if isinstance(entry, tk.Entry):
            entry.delete(0, tk.END)
            entry.insert(0, cadastro[campo])
        else:
            entry.set(cadastro[campo])

    btn_cadastrar.config(text="Salvar Edição")
    notebook.select(aba_cadastro)

def selecionar_anexo():
    caminho = filedialog.askopenfilename(title="Selecionar Documento")
    if caminho:
        anexo_path.set(caminho)

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro com Abas")

notebook = ttk.Notebook(janela)
notebook.pack(padx=10, pady=10, fill='both', expand=True)

# Aba de Cadastro
aba_cadastro = ttk.Frame(notebook)
notebook.add(aba_cadastro, text='Cadastro')

# Labels e Entradas
labels = [
    "Nome", "E-mail", "Estado", "Cidade", "País",
    "Telefone", "Documento", "Data de Nascimento",
    "Nome do Pai", "Nome da Mãe", "Endereço", "Bairro"
]

entradas = []
for i, texto in enumerate(labels):
    tk.Label(aba_cadastro, text=f"{texto}:").grid(row=i, column=0, sticky="e")
    entry = tk.Entry(aba_cadastro, width=40)
    entry.grid(row=i, column=1, padx=5, pady=2)
    entradas.append(entry)

# Anexo
anexo_path = tk.StringVar()
tk.Label(aba_cadastro, text="Anexar Documento:").grid(row=len(labels), column=0, sticky="e")
tk.Entry(aba_cadastro, textvariable=anexo_path, state="readonly", width=30).grid(row=len(labels), column=1, sticky="w")
tk.Button(aba_cadastro, text="Selecionar Arquivo", command=selecionar_anexo).grid(row=len(labels), column=2, padx=5)

# Botão cadastrar/editar
btn_cadastrar = tk.Button(aba_cadastro, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=len(labels)+1, column=0, columnspan=3, pady=10)

# Aba de Visualização
aba_visualizar = ttk.Frame(notebook)
notebook.add(aba_visualizar, text='Visualizar Cadastros')

# Tabela de visualização
colunas = ("Nome", "Email", "Telefone", "Nascimento")
tree = ttk.Treeview(aba_visualizar, columns=colunas, show="headings")

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill="both", expand=True)

# Botões de ação
frame_botoes = tk.Frame(aba_visualizar)
frame_botoes.pack(pady=10)

btn_editar = tk.Button(frame_botoes, text="Editar Selecionado", command=editar_cadastro)
btn_editar.pack(side="left", padx=10)

btn_excluir = tk.Button(frame_botoes, text="Excluir Selecionado", command=excluir_cadastro)
btn_excluir.pack(side="left", padx=10)

janela.mainloop()
