# Importação de bibliotecas
import numpy as np
import tkinter as tk
from tkinter import messagebox

# Função para obter dados das entradas do usuário
def obter_dados(entry_vars, entry_cons, entry_obj):
    try:
        # Obtém o número de variáveis e restrições
        num_variables = int(entry_vars.get())
        num_constraints = int(entry_cons.get())

        # Obtém os coeficientes da função objetivo
        funcObj = []
        for i in range(num_variables):
            coefficient = float(entry_obj[i].get())
            funcObj.append(-coefficient)  # Negativo para maximização
        funcObj = np.array(funcObj)

        # Obtém os coeficientes das restrições
        restric = []
        for i in range(num_constraints):
            row = []
            for j in range(num_variables):
                coefficient = float(entry_restric[i][j].get())
                row.append(coefficient)
            restric.append(row)
        restric = np.array(restric)

        # Obtém os termos constantes das restrições
        const = []
        for i in range(num_constraints):
            constant = float(entry_const[i].get())
            const.append(constant)
        const = np.array(const)

        return funcObj, restric, const
    except ValueError:
        # Exibe mensagem de erro se houver valores inválidos
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        return None, None, None

# Função que implementa o método Simplex
def simplex(funcObj, restricoes, constantes):
    # Quantidade de variáveis e constantes
    n_vars = len(funcObj)
    n_cons = len(constantes)

    # Adiciona variáveis de folga às restrições
    restricoes = np.hstack([restricoes, np.eye(n_cons)])
    funcObj = np.hstack([funcObj, np.zeros(n_cons)])
    
    # Cria o tableau inicial
    tableau = np.vstack([np.hstack([restricoes, constantes.reshape(-1, 1)]), np.hstack([funcObj, 0])])

    # Iteração até encontrar a solução ótima
    while True:
        # Verifica se a solução é ótima
        if np.all(tableau[-1, :-1] >= 0):
            break

        # Encontra a coluna pivô (menor valor na última linha)
        pivot_col = np.argmin(tableau[-1, :-1])

        # Encontra a linha pivô (menor razão positiva)
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios < 0] = np.inf
        pivot_row = np.argmin(ratios)

        # Realiza a operação de pivoteamento
        pivot_val = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_val
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i] -= tableau[pivot_row] * tableau[i, pivot_col]

    # Extrai a solução
    solucao = np.zeros(n_vars)
    for i in range(n_vars):
        col = tableau[:, i]
        if (col == 0).sum() == n_cons:
            row = np.where(col[:-1] == 1)[0][0]
            solucao[i] = tableau[row, -1]

    # Preço sombra
    precoSombra = tableau[-1, n_vars:-1]

    return solucao, tableau[-1, -1], precoSombra

# Função para iniciar o cálculo
def iniciar_calculo(entry_vars, entry_cons, entry_obj):
    funcObj, restric, const = obter_dados(entry_vars, entry_cons, entry_obj)
    if funcObj is not None:
        solucao, valorOtimo, precoSombra = simplex(funcObj, restric, const)
        messagebox.showinfo("Resultado", f'Solução Ótima: {solucao}\nLucro Ótimo: {valorOtimo}\nPreços Sombra: {precoSombra}')

# Função principal para criar a interface gráfica
def main():
    root = tk.Tk()
    root.title("Método Simplex")

    tk.Label(root, text="Método Simplex", font=("Helvetica", 16)).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="Número de Variáveis:").grid(row=0, column=0)
    entry_vars = tk.Entry(frame)
    entry_vars.grid(row=0, column=1)

    tk.Label(frame, text="Número de Restrições:").grid(row=1, column=0)
    entry_cons = tk.Entry(frame)
    entry_cons.grid(row=1, column=1)

    # Função para criar campos de entrada dinâmicos
    def criar_campos():
        num_variables = int(entry_vars.get())
        num_constraints = int(entry_cons.get())

        global entry_obj, entry_restric, entry_const
        entry_obj = []
        entry_restric = []
        entry_const = []

        # Remove widgets antigos
        for widget in frame.winfo_children()[4:]:
            widget.destroy()

        # Cria campos para coeficientes da função objetivo
        tk.Label(frame, text="Coeficientes da Função Objetivo:").grid(row=2, column=0, columnspan=2)
        for i in range(num_variables):
            entry = tk.Entry(frame)
            entry.grid(row=3, column=i)
            entry_obj.append(entry)

        # Cria campos para coeficientes das restrições
        tk.Label(frame, text="Coeficientes das Restrições:").grid(row=4, column=0, columnspan=2)
        for i in range(num_constraints):
            row = []
            for j in range(num_variables):
                entry = tk.Entry(frame)
                entry.grid(row=5 + i, column=j)
                row.append(entry)
            entry_restric.append(row)

        # Cria campos para termos constantes das restrições
        tk.Label(frame, text="Termos Constantes das Restrições:").grid(row=5 + num_constraints, column=0, columnspan=2)
        for i in range(num_constraints):
            entry = tk.Entry(frame)
            entry.grid(row=6 + num_constraints, column=i)
            entry_const.append(entry)

        # Botão para iniciar o cálculo
        tk.Button(frame, text="Calcular", command=lambda: iniciar_calculo(entry_vars, entry_cons, entry_obj)).grid(row=7 + num_constraints, column=0, columnspan=2, pady=10)

    # Botão para criar campos de entrada
    tk.Button(frame, text="Criar Campos", command=criar_campos).grid(row=2, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()