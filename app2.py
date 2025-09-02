import tkinter as tk

tela = tk.Tk()
tela.geometry("1200x500")
tela.title("Administradora")

bancoDeDados = []
id = 0

def enviarImovel():
    global id
    id +=1 
    
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
    print(bancoDeDados)

    entryEndereco.delete(0, tk.END)
    entryProprietario.delete(0, tk.END)
    entryEntrada.delete(0, tk.END)
    entryValor.delete(0, tk.END)
    entryDescricao.delete(0, tk.END)

tk.Label(tela, text="Digite o endereço:").grid(row=0, column=0, padx=5, pady=5)
entryEndereco = tk.Entry(tela)
entryEndereco.grid(row=1, column=0, padx=5,pady=5)

tk.Label(tela, text="Digite o nome do proprietario:").grid(row=4, column=0, padx=5, pady=5)
entryProprietario = tk.Entry(tela)
entryProprietario.grid(row=5, column=0, padx=5,pady=5)

tk.Label(tela, text="Digite a data de entrada:").grid(row=7, column=0, padx=5, pady=5)
entryEntrada = tk.Entry(tela)
entryEntrada.grid(row=8, column=0, padx=5,pady=5)

tk.Label(tela, text="Digite o valor do imovel:").grid(row=10, column=0, padx=5, pady=5)
entryValor = tk.Entry(tela)
entryValor.grid(row=11, column=0, padx=5,pady=5)

tk.Label(tela, text="Digite a descrição do imovel:").grid(row=13, column=0, padx=5, pady=5)
entryDescricao = tk.Entry(tela)
entryDescricao.grid(row=14, column=0, padx=5,pady=5)

tk.Button(tela, text="Enviar", command=enviarImovel).grid(row=15, column=0, padx=5, pady=5)

tela.mainloop()