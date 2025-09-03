import tkinter as tk
from tkinter import messagebox

tela = tk.Tk()
tela.geometry("1200x500")
tela.title("Administradora")

exibir = tk.Listbox(tela, width=80, height=20)
exibir.grid(row=0, column=1, rowspan=20, padx=10, pady=10, sticky="nsew")

bancoDeDados = []
id = 0

# ---------------- FUNÇÕES ---------------- #
def atualizarLista():
    exibir.delete(0, tk.END)  # limpa a Listbox
    for imovel in bancoDeDados:
        linha = f"ID: {imovel['id']} | Endereço: {imovel['endereco']} | Proprietário: {imovel['proprietario']} | Entrada: {imovel['entrada']} | Valor: {imovel['valor']} | Descrição: {imovel['descricao']}"
        exibir.insert(tk.END, linha)

def enviarImovel():
    global id
    id += 1
    
    endereco = entryEndereco.get().strip()
    proprietario = entryProprietario.get().strip()
    entrada = entryEntrada.get().strip()
    valor = entryValor.get().strip()
    descricao = entryDescricao.get().strip()

    bancoDeDados.append({
        "id": id,
        "endereco": endereco,
        "proprietario": proprietario,
        "entrada": entrada,
        "valor": valor,
        "descricao": descricao
    })

    entryEndereco.delete(0, tk.END)
    entryProprietario.delete(0, tk.END)
    entryEntrada.delete(0, tk.END)  
    entryValor.delete(0, tk.END)
    entryDescricao.delete(0, tk.END)

    atualizarLista()

def editar():
    selecionado = exibir.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um imóvel para editar!")
        return

    indice = selecionado[0]
    imovel = bancoDeDados[indice]

    # Janela de edição
    janela = tk.Toplevel(tela)
    janela.title("Editar Imóvel")
    janela.geometry("400x300")

    # Campos preenchidos
    tk.Label(janela, text="Endereço:").pack()
    entryE = tk.Entry(janela, width=40)
    entryE.insert(0, imovel["endereco"])
    entryE.pack()

    tk.Label(janela, text="Proprietário:").pack()
    entryP = tk.Entry(janela, width=40)
    entryP.insert(0, imovel["proprietario"])
    entryP.pack()

    tk.Label(janela, text="Entrada:").pack()
    entryEn = tk.Entry(janela, width=40)
    entryEn.insert(0, imovel["entrada"])
    entryEn.pack()

    tk.Label(janela, text="Valor:").pack()
    entryV = tk.Entry(janela, width=40)
    entryV.insert(0, imovel["valor"])
    entryV.pack()

    tk.Label(janela, text="Descrição:").pack()
    entryD = tk.Entry(janela, width=40)
    entryD.insert(0, imovel["descricao"])
    entryD.pack()

    def salvar():
        imovel["endereco"] = entryE.get().strip()
        imovel["proprietario"] = entryP.get().strip()
        imovel["entrada"] = entryEn.get().strip()
        imovel["valor"] = entryV.get().strip()
        imovel["descricao"] = entryD.get().strip()
        atualizarLista()
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

def remover():
    selecionado = exibir.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um imóvel para remover!")
        return

    indice = selecionado[0]
    bancoDeDados.pop(indice)
    atualizarLista()

# ---------------- INTERFACE ---------------- #
tk.Label(tela, text="Digite o endereço:").grid(row=0, column=0, padx=5, pady=5)
entryEndereco = tk.Entry(tela)
entryEndereco.grid(row=1, column=0, padx=5, pady=5)

tk.Label(tela, text="Digite o nome do proprietario:").grid(row=4, column=0, padx=5, pady=5)
entryProprietario = tk.Entry(tela)
entryProprietario.grid(row=5, column=0, padx=5, pady=5)

tk.Label(tela, text="Digite a data de entrada:").grid(row=7, column=0, padx=5, pady=5)
entryEntrada = tk.Entry(tela)
entryEntrada.grid(row=8, column=0, padx=5, pady=5)

tk.Label(tela, text="Digite o valor do imovel:").grid(row=10, column=0, padx=5, pady=5)
entryValor = tk.Entry(tela)
entryValor.grid(row=11, column=0, padx=5, pady=5)

tk.Label(tela, text="Digite a descrição do imovel:").grid(row=13, column=0, padx=5, pady=5)
entryDescricao = tk.Entry(tela)
entryDescricao.grid(row=14, column=0, padx=5, pady=5)

tk.Button(tela, text="Enviar", command=enviarImovel).grid(row=15, column=0, padx=5, pady=5)
tk.Button(tela, text="Editar", command=editar).grid(row=16, column=0, padx=5, pady=5)
tk.Button(tela, text="Remover", command=remover).grid(row=17, column=0, padx=5, pady=5)

tela.mainloop()
