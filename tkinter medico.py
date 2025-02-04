import tkinter as tk

# Criar janela principal
root = tk.Tk()
root.title("Interface com 5 Objetos")
root.geometry("500x300")

# Criar Rótulos e Caixas de Entrada lado a lado
tk.Label(root, text="Nome do Paciente :", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_nome = tk.Entry(root, width=20).
entrada_nome.grid(row=1, column=1, padx=10, pady=5)


tk.Label(root, text="Idade:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entrada_ingredientes = tk.Entry(root, width=20)
entrada_ingredientes.grid(row=1, column=1, padx=10, pady=5, sticky='w')

tk.Label(root, text="Diagnostico:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entrada_md = tk.Entry(root, width=20)
entrada_md.grid(row=2, column=1, padx=10, pady=5, sticky="e")

tk.Label (root, text="Medico Responsavel :",font=("Arial")).grid(row=3,column=0,padx=10,pady=5,sticky="e")
entrada_qt=tk.Entry(root,width=20)
entrada_qt.grid(row=3,column=1,padx=10,pady=5,sticky="e")

tk.Label (root, text="Leito:",font=("Arial")).grid(row=4,column=0,padx=10,pady=5,sticky="e")
entrada_lt=tk.Entry(root,width=20)
entrada_lt.grid(row=4,column=1,padx=10,pady=5,sticky="e")


# Criar um rótulo para exibir o resultado
label_resultado = tk.Label(root, text="Salvar:", font=("Arial", 12), fg="blue")
label_resultado.grid(row=6, column=0, columnspan=2, pady=10)


# Função para exibir os dados digitados
def exibir_dados():
    nome = entrada_nome.get()
    ingredientes = entrada_ingredientes.get()
    modo_preparo = entrada_md.get()
    gg = entrada_qt.get()
    leito=entrada_lt.get()
    label_resultado.config(text=f"Nome do paciente: {entrada_nome}, Idade: {ingredientes}, Diagnostico: {modo_preparo}, Medico Responsavel:{gg}, Leito {leito}")

# Função para limpar os campos
def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_ingredientes.delete(0, tk.END)
    entrada_md.delete(0, tk.END)
    entrada_lt.delete(0,tk.END)
    entrada_qt.delete(0,tk.END)
    label_resultado.config(text="Resultado:")

# Criar Botões e posicioná-los
botao_exibir = tk.Button(root, text="Exibir", command=exibir_dados)
botao_exibir.grid(row=7, column=0, padx=10, pady=10, sticky="e")

botao_limpar = tk.Button(root, text="Limpar", command=limpar_campos)
botao_limpar.grid(row=7, column=1, padx=10, pady=10, sticky="w")

# Iniciar o loop da aplicação
root.mainloop()