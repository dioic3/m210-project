from scipy.optimize import linprog
import numpy as np
import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedStyle

def simplex_method(c, A_ub, b_ub, A_eq, b_eq, maximize=False):
    if maximize:
        c = [-coeff for coeff in c]
    res = linprog(c, A_ub, b_ub, A_eq, b_eq, method='simplex')
    if maximize and res.success:
        res.fun = -res.fun
    return res

class SimplexApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solucionador Método Simplex")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("radiance")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Coeficientes da Função Objetivo:", font=('Helvetica', 12)).grid(row=0, column=0, columnspan=6, pady=5, sticky=tk.W)
        self.funcao_obj = self.create_entradas(4, 1)
        self.restricoes = self.create_restricoes(5)
        self.var_opcoes = tk.StringVar(value="minimize")
        ttk.Radiobutton(self.root, text="Minimizar", variable=self.var_opcoes, value="minimize", style='TButton').grid(row=13, column=1, pady=5, sticky=tk.W)
        ttk.Radiobutton(self.root, text="Maximizar", variable=self.var_opcoes, value="maximize", style='TButton').grid(row=13, column=2, pady=5, sticky=tk.W)
        self.button_solve = ttk.Button(self.root, text="Resolver", command=self.solve, width=20, style='TButton')
        self.button_solve.grid(row=14, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        self.output = tk.Text(self.root, height=10, width=130, font=('Helvetica', 12), relief='solid', bd=2)
        self.output.grid(row=15, column=0, columnspan=6, padx=10, pady=10, sticky=tk.W)

    def create_entradas(self, quantidade, linha):
        entradas = [ttk.Entry(self.root, font=('Helvetica', 12)) for _ in range(quantidade)]
        for i, entry in enumerate(entradas):
            entry.grid(row=linha, column=i, padx=5, pady=5, sticky=tk.W)
        return entradas

    def create_restricoes(self, quantidade):
        lista_restricoes = []
        for i in range(quantidade):
            tk.Label(self.root, text=f"Coeficientes da Restrição {i+1}:", font=('Helvetica', 12)).grid(row=3 + i * 2, column=0, columnspan=6, pady=5, sticky=tk.W)
            coeficientes = self.create_entradas(4, 4 + i * 2)
            sinal_restricao = ttk.Combobox(self.root, values=["≤", "≥", "="], font=('Helvetica', 12), state="readonly", width=2)
            sinal_restricao.grid(row=4 + i * 2, column=4, padx=5, pady=5, sticky=tk.W)
            sinal_restricao.current(0)
            lado_direito = ttk.Entry(self.root, font=('Helvetica', 12))
            lado_direito.grid(row=4 + i * 2, column=5, padx=5, pady=5, sticky=tk.W)
            lista_restricoes.append((coeficientes, sinal_restricao, lado_direito))
        return lista_restricoes

    def solve(self):
        try:
            c = self.get_entradas(self.funcao_obj)
            A_ub, b_ub, A_eq, b_eq = [], [], [], []
            for coeficientes, sinal_restricao, lado_direito in self.restricoes:
                coef_atual = self.get_entradas(coeficientes)
                ld_atual = float(lado_direito.get() if lado_direito.get() else 0)
                if sinal_restricao.get() == "≤":
                    A_ub.append(coef_atual)
                    b_ub.append(ld_atual)
                elif sinal_restricao.get() == "≥":
                    A_ub.append([-val for val in coef_atual])
                    b_ub.append(-ld_atual)
                else:
                    A_eq.append(coef_atual)
                    b_eq.append(ld_atual)
            maximize = self.var_opcoes.get() == "maximize"
            result = simplex_method(c, A_ub if A_ub else None, b_ub if b_ub else None, A_eq if A_eq else None, b_eq if b_eq else None, maximize)
            self.exibe_resultado(result)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira coeficientes válidos.")

    def get_entradas(self, entradas):
        return [float(entry.get().replace(',', '.') if entry.get() else 0) for entry in entradas]

    def exibe_resultado(self, result):
        self.output.delete(1.0, tk.END)
        if result.success:
            self.output.insert(tk.END, f"Valor Ótimo: R$ {result.fun:.2f}\n")
            solution = [f"{val:.2f}" for val in result.x]
            self.output.insert(tk.END, f"Solução Ótima: [{', '.join(solution)}]\n")
        else:
            self.output.insert(tk.END, "Nenhuma solução encontrada\n")

root = tk.Tk()
app = SimplexApp(root)
root.mainloop()
