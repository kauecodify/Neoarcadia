import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy.optimize import newton

def calcular_vpl(taxa, fluxos):
    return sum(fluxo / ((1 + taxa) ** i) for i, fluxo in enumerate(fluxos))

# calcular TIR (método Newton)
def calcular_tir(fluxos):
    def func(taxa):
        return sum(fluxo / ((1 + taxa) ** i) for i, fluxo in enumerate(fluxos))
 
    try:
        tir = newton(func, 0.1)  # Newton para raiz da função
        return tir * 100  # converte percentual
    except Exception as e:
        return None

def calcular():
    try:
        taxa = float(entry_taxa.get()) / 100  # conversão para decimal
        if not (0 <= taxa < 1):
            raise ValueError("A taxa de desconto deve estar entre 0 e 100%.")

        fluxos = list(map(float, entry_fluxos.get().split(",")))
        if len(fluxos) < 2:
            raise ValueError("Insira pelo menos um fluxo de caixa e o valor inicial.")

        vpl = calcular_vpl(taxa, fluxos)
        
        tir = calcular_tir(fluxos)
        
        if tir is None:
            label_tir.config(text="TIR: Não encontrada.")
        else:
            # resultado
            label_vpl.config(text=f"VPL: R$ {vpl:.2f}")
            label_tir.config(text=f"TIR: {tir:.2f}%")
            
    except ValueError as e:
        messagebox.showerror("Erro nos Dados", f"Erro nos dados de entrada: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


#INTERFACE

janela = tk.Tk()
janela.title("NeoArcadia - Análise Financeira")
janela.geometry("600x300")
janela.configure(bg="gray")

titulo = tk.Label(janela, text="Análise para novos Investimentos em projetos", font=("Arial", 16, "bold"), bg="gray", fg="white")
titulo.pack(pady=10)

label_taxa = tk.Label(janela, text="Taxa de Desconto (%):", bg="gray", fg="white")
label_taxa.pack()
entry_taxa = tk.Entry(janela, width=30)
entry_taxa.pack(pady=5)

label_fluxos = tk.Label(janela, text="Fluxos de Caixa (separados por vírgula):", bg="gray", fg="white")
label_fluxos.pack()
entry_fluxos = tk.Entry(janela, width=30)
entry_fluxos.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular VPL e TIR", command=calcular, bg="#846512", fg="white", font=("Arial", 15, "bold"))
botao_calcular.pack(pady=20)

label_vpl = tk.Label(janela, text="VPL: R$ 0.00", font=("Arial", 12), bg="gray", fg="white")
label_vpl.pack()

label_tir = tk.Label(janela, text="TIR: 0.00%", font=("Arial", 12), bg="gray", fg="white")
label_tir.pack()

janela.mainloop()
