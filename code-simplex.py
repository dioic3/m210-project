#Importação de bibliotecas 
import numpy as np
import tkinter as tk
from tkinter import messagebox

def obter_dados(entry_vars, entry_cons, entry_obj):
    try:
        num_variables = int(entry_vars.get())
        num_constraints = int(entry_cons.get())

        funcObj = []
        for i in range(num_variables):
            coefficient = float(entry_obj[i].get())
            funcObj.append(-coefficient)
        funcObj = np.array(funcObj)

        restric = []
        for i in range(num_constraints):
            row = []
            for j in range(num_variables):
                coefficient = float(entry_restric[i][j].get())
                row.append(coefficient)
            restric.append(row)
        restric = np.array(restric)

        const = []
        for i in range(num_constraints):
            constant = float(entry_const[i].get())
            const.append(constant)
        const = np.array(const)

        return funcObj, restric, const
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        return None, None, None

def simplex(funcObj, restricoes, constantes):

    #Quantidade de variáveis e constantes
    n_vars = len(funcObj)
    n_cons = len(constantes)

    #Adicionando as variáveis às constantes em um vetor 
    restricoes = np.hstack([restricoes, np.eye(n_cons)])
    funcObj = np.hstack([funcObj, np.zeros(n_cons)])
    
    #Cria um tableau inicial
    tableau = np.vstack([np.hstack([restricoes, constantes.reshape(-1, 1)]), np.hstack([funcObj, 0])])

    #Iteração até que o método encontre a solução ótima
    while True:
        #Checando se a solução é ótima
        if np.all(tableau[-1, :-1] >= 0):
            break

        #Encontrando a coluna pivô
        pivot_col = np.argmin(tableau[-1, :-1])

        #Encontrando a linha pivô
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios < 0] = np.inf
        pivot_row = np.argmin(ratios)

        #Operação que utiliza os valores pivô
        pivot_val = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_val
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i] -= tableau[pivot_row] * tableau[i, pivot_col]

    #Extraindo a solução 
    solucao = np.zeros(n_vars)
    for i in range(n_vars):
        col = tableau[:, i]
        if (col == 0).sum() == n_cons:
            row = np.where(col[:-1] == 1)[0][0]
            solucao[i] = tableau[row, -1]

    #Preço sombra
    precoSombra = tableau[-1, n_vars:-1]

    return solucao, tableau[-1, -1], precoSombra

def iniciar_calculo(entry_vars, entry_cons, entry_obj):
    funcObj, restric, const = obter_dados(entry_vars, entry_cons, entry_obj)
    if funcObj is not None:
        solucao, valorOtimo, precoSombra = simplex(funcObj, restric, const)
        messagebox.showinfo("Resultado", f'Solução Ótima: {solucao}\nLucro Ótimo: {valorOtimo}\nPreços Sombra: {precoSombra}')

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

    def criar_campos():
        num_variables = int(entry_vars.get())
        num_constraints = int(entry_cons.get())

        global entry_obj, entry_restric, entry_const
        entry_obj = []
        entry_restric = []
        entry_const = []

        for widget in frame.winfo_children()[4:]:
            widget.destroy()

        tk.Label(frame, text="Coeficientes da Função Objetivo:").grid(row=2, column=0, columnspan=2)
        for i in range(num_variables):
            entry = tk.Entry(frame)
            entry.grid(row=3, column=i)
            entry_obj.append(entry)

        tk.Label(frame, text="Coeficientes das Restrições:").grid(row=4, column=0, columnspan=2)
        for i in range(num_constraints):
            row = []
            for j in range(num_variables):
                entry = tk.Entry(frame)
                entry.grid(row=5 + i, column=j)
                row.append(entry)
            entry_restric.append(row)

        tk.Label(frame, text="Termos Constantes das Restrições:").grid(row=5 + num_constraints, column=0, columnspan=2)
        for i in range(num_constraints):
            entry = tk.Entry(frame)
            entry.grid(row=6 + num_constraints, column=i)
            entry_const.append(entry)

        tk.Button(frame, text="Calcular", command=lambda: iniciar_calculo(entry_vars, entry_cons, entry_obj)).grid(row=7 + num_constraints, column=0, columnspan=2, pady=10)

    tk.Button(frame, text="Criar Campos", command=criar_campos).grid(row=2, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()