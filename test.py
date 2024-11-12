import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy.optimize import newton

def calcular_vpl(taxa_mensal, fluxos):
    return sum(fluxo / ((1 + taxa_mensal) ** i) for i, fluxo in enumerate(fluxos))

def calcular_tir(fluxos):
    def func(taxa):
        return sum(fluxo / ((1 + taxa) ** i) for i, fluxo in enumerate(fluxos))
    return newton(func, 0.1)

def mostrar_dados():
    try:
        investimento_inicial = float(entry_investimento.get())
        fluxo_mensal = float(entry_fluxo_mensal.get())
        meses = int(entry_meses.get())
        taxa_ano = 0.10
        taxa_mensal = taxa_ano / 12
        fluxos = [-investimento_inicial] + [fluxo_mensal] * meses
        vpl = calcular_vpl(taxa_mensal, fluxos)
        tir = calcular_tir(fluxos) * 100
        for i in range(meses):
            text_fluxos.insert(tk.END, f"Mês {i + 1}: R${fluxo_mensal}\n")
        messagebox.showinfo("Resultado", f"VPL: R${vpl:.2f}\nTIR: {tir:.2f}%")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")

janela = tk.Tk()
janela.title("Análise de Investimento")
janela.geometry("400x400")

tk.Label(janela, text="Investimento Inicial (R$):").pack()
entry_investimento = tk.Entry(janela)
entry_investimento.pack()

tk.Label(janela, text="Fluxo Mensal (R$):").pack()
entry_fluxo_mensal = tk.Entry(janela)
entry_fluxo_mensal.pack()

tk.Label(janela, text="Número de Meses:").pack()
entry_meses = tk.Entry(janela)
entry_meses.pack()

btn_mostrar = tk.Button(janela, text="Visualizar Dados e Calcular", command=mostrar_dados)
btn_mostrar.pack()

text_fluxos = tk.Text(janela, height=10, width=30)
text_fluxos.pack()

janela.mainloop()
