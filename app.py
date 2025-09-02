import tkinter as tk
from tkinter import messagebox, simpledialog

# ======== Base de dados (em memória) ========
estoque = []

# ======== Funções ========
def atualizar_lista():
    """Atualiza a listbox com os produtos do estoque."""
    listbox_estoque.delete(0, tk.END)
    for i, p in enumerate(estoque):
        listbox_estoque.insert(tk.END, f"{i} - {p['local']} | Valor: {p['valor']} | Data de entrda: {p['entrada']} | Proprietario: {p['proprietario']}")

def adicionar_produto():
    """Adiciona um produto ao estoque."""
    local = entry_nome.get().strip()
    proprietario = entry_proprietario.get().strip()
    entrada = entry_Entrada.get().strip()
    valor = entry_valor.get().strip()
    
    if not local or not proprietario or not valor or not valor:
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return
    
    estoque.append({"local": local, "proprietario": proprietario, "entrada": entrada, "valor": valor})
    messagebox.showinfo("Sucesso", f"{local} adicionado ao estoque!")
    
    entry_nome.delete(0, tk.END)
    entry_proprietario.delete(0, tk.END)
    entry_Entrada.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    
    atualizar_lista()

def remover_produto():
    """Remove o produto selecionado na listbox."""
    selecionado = listbox_estoque.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um produto para remover!")
        return
    idx = selecionado[0]
    prod = estoque.pop(idx)
    messagebox.showinfo("Removido", f"{prod['nome']} removido do estoque!")
    atualizar_lista()

def editar_produto():
    """Edita o produto selecionado."""
    selecionado = listbox_estoque.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um produto para editar!")
        return
    idx = selecionado[0]
    prod = estoque[idx]

    novo_nome = simpledialog.askstring("Editar", "Nome:", initialvalue=prod["local"])
    if novo_nome is None:  # Cancelou
        return
    nova_qtde = simpledialog.askstring("Editar", "Quantidade:", initialvalue=prod["entrada"])
    if nova_qtde is None:
        return
    nova_validade = simpledialog.askstring("Editar", "Validade:", initialvalue=prod["valor"])
    if nova_validade is None:
        return

    estoque[idx] = {"nome": novo_nome, "quantidade": nova_qtde, "validade": nova_validade}
    messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
    atualizar_lista()

# ======== Interface ========
root = tk.Tk()
root.title("Gerenciador de Estoque")

# Labels e entradas
tk.Label(root, text="local").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="entrada").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="valor").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Proprietario").grid(row=3, column=0, padx=5, pady=5)

entry_nome = tk.Entry(root)
entry_Entrada = tk.Entry(root)
entry_proprietario = tk.Entry(root)
entry_valor = tk.Entry(root)

entry_nome.grid(row=0, column=1, padx=5, pady=5)
entry_Entrada.grid(row=1, column=1, padx=5, pady=5)
entry_proprietario.grid(row=2, column=1, padx=5, pady=5)
entry_valor.grid(row=3, column=1, padx=5, pady=5)

# Botões
tk.Button(root, text="Adicionar", command=adicionar_produto).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Editar", command=editar_produto).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(root, text="Remover", command=remover_produto).grid(row=6, column=0, columnspan=2, pady=5)

# Listbox
listbox_estoque = tk.Listbox(root, width=50)
listbox_estoque.grid(row=0, column=2, rowspan=6, padx=10, pady=5)

# Inicializa lista
atualizar_lista()

# Loop principal
root.mainloop()
