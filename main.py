
import tkinter as tk

def calcular_imc():
    altura = float(entrada_altura.get())
    peso = float(entrada_peso.get())
    imc = peso / (altura/100) ** 2
    resultado_label.config(text=f"IMC: {imc:.2f}")

def reiniciar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)
    resultado_label.config(text="Resultado")

janela = tk.Tk()
janela.title("Cálculo do IMC - Índice de Massa Corporal")

label_nome = tk.Label(janela, text="Nome do Paciente:")
entrada_nome = tk.Entry(janela, width=50)
label_endereco = tk.Label(janela, text="Endereço Completo:")
entrada_endereco = tk.Entry(janela, width=50)
label_altura = tk.Label(janela, text="Altura (cm):")
entrada_altura = tk.Entry(janela, width=25)
label_peso = tk.Label(janela, text="Peso (Kg):")
entrada_peso = tk.Entry(janela, width=25)
resultado_label = tk.Label(janela, text="Resultado", relief="sunken", width=20, height=5)
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_imc)
botao_reiniciar = tk.Button(janela, text="Reiniciar", command=reiniciar_campos)
botao_sair = tk.Button(janela, text="Sair", command=janela.quit)

label_nome.grid(row=1, column=0, sticky="w")
entrada_nome.grid(row=1, column=1, columnspan=3, padx=10, pady=5)
label_endereco.grid(row=2, column=0, sticky="w")
entrada_endereco.grid(row=2, column=1, columnspan=3, padx=10, pady=5)
label_altura.grid(row=3, column=0, sticky="w")
entrada_altura.grid(row=3, column=1,columnspan=1, padx=10, pady=5)
label_peso.grid(row=4, column=0, sticky="w")
entrada_peso.grid(row=4, column=1,columnspan=1, padx=10, pady=5)
resultado_label.grid(row=4, column=2, columnspan=2, pady=5)
botao_calcular.grid(row=5, column=1, padx=2, pady=5)
botao_reiniciar.grid(row=5, column=2, padx=2, pady=5)
botao_sair.grid(row=5, column=3, padx=10, pady=5)

janela.mainloop()