from scipy.optimize import linprog
import numpy as np
import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedStyle
# Projeto desenvolvido para a disciplina de Otimização I - M210. Este solucionador utiliza o método Simplex para resolver problemas de programação linear com duas até quatro variáveis.
# Para utilizar o método Simplex, trabalhar com matrizes e realizar operações matemáticas, o código utiliza a função `linprog` da biblioteca `scipy.optimize` e a biblioteca `NumPy`:

def simplex_method(c, A_ub, b_ub, A_eq, b_eq, maximize=False):
    # Inverte os coeficientes para maximizar:
    if maximize:     
        c = [-coeff for coeff in c]

    res = linprog(c, A_ub, b_ub, A_eq, b_eq, method='simplex')

    # Inverte o valor da função objetivo:
    if maximize and res.success:
        res.fun = -res.fun
        
    return res

def shadow_prices(A, b, c):
    dual_c = b       
    dual_b = -1.0 * c
    dual_A = -1.0 * np.transpose(A)

    # Inicializa a matriz para o dual_A transformado:
    novo_A = np.zeros((len(A), len(A[0]) + 1))

    for i in range(len(dual_A)):
        novo_A[i, :-1] = dual_A[:, i]
        novo_A[i, -1] = 0 

    novo_A = novo_A[:-1]

    # Encontra o índice do menor valor em dual_b
    min_index = np.argmin(dual_b)

    # Encontra a coluna em novo_A correspondente ao min_index em dual_b
    column_min_b = novo_A[:, min_index]

    # Realiza as operações de divisão:
    division_results = []
    for j in range(len(column_min_b)):
        if column_min_b[j] != 0:
            division_results.append(dual_c[j] / column_min_b[j])
        else:
            division_results.append(np.inf)  # para divisão por zero
            
    # Encontra o índice do maior resultado da divisão que não seja infinito:
    min_division_index = 0
    min_division_index = np.argmax(
        [result if result != np.inf else -np.inf for result in division_results])

    # Calcula o impacto no custo da função objetivo:
    if min_division_index < len(dual_b):
        impacto_custo = (dual_b[min_division_index] -
                         dual_c[min_division_index]) * (-1)
    else:
        impacto_custo = 0  # Caso o índice seja inválido

    # Atualiza o valor de dual_c[min_division_index] pelo impacto calculado:
    if min_division_index < len(dual_c):
        dual_c[min_division_index] = impacto_custo

    # Calcula os preços-sombra de cada restrição:
    result = linprog(dual_c, A_ub=dual_A, b_ub=dual_b, method='simplex')

    return result


class SimplexApp:
    def __init__(self, root):
        self.root = root 
        self.root.title("Solucionador Método Simplex")

        # Define o tema "radiance" para a interface:
        self.style = ThemedStyle(self.root)
        self.style.set_theme("radiance")      
        
        # Chama o método para criar os widgets:
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Coeficientes da Função Objetivo:", 
                 font=('Helvetica', 12)).grid(row=0, column=0, columnspan=6, pady=5, sticky=tk.W)

        # Cria de entradas da função objetivo:
        self.funcao_obj = self.create_entradas(4, 1)

        # Cria as restrições:
        self.restricoes = self.create_restricoes(5)

        # Variável de controle para otimização (minimizar ou maximizar):
        self.var_opcoes = tk.StringVar(value="minimize")
        
        ttk.Radiobutton(self.root, text="Minimizar", variable=self.var_opcoes, value="minimize",
                    style='TButton').grid(row=13, column=1, pady=5, sticky=tk.W)
        
        ttk.Radiobutton(self.root, text="Maximizar", variable=self.var_opcoes, value="maximize",
                    style='TButton').grid(row=13, column=2, pady=5, sticky=tk.W)

        # Botão Resolver chama o método "solve":
        self.button_solve = ttk.Button(self.root, text="Resolver", command=self.solve, width=20, style='TButton')
        self.button_solve.grid(row=14, column=0, padx=5, pady=5, sticky=tk.W + tk.E)

        # Texto de saída para exibir o resultado:
        self.output = tk.Text(self.root, height=10, width=130, font=('Helvetica', 12), relief='solid', bd=2)
        self.output.grid(row=15, column=0, columnspan=6, padx=10, pady=10, sticky=tk.W) 
        
    def create_entradas(self, quantidade, linha):
        # Cria uma lista de entradas com a quantidade definida de entradas:
        entradas = [ttk.Entry(self.root, font=('Helvetica', 12)) for _ in range(quantidade)]
    
        # Posiciona as entradas na lista em cada coluna correspondente ao índice e linha especificada:
        for i, entry in enumerate(entradas):
            entry.grid(row=linha, column=i, padx=5, pady=5, sticky=tk.W)

        return entradas
    
    def create_restricoes(self, quantidade):
        lista_restricoes = []
        
        # Cria o label das restrições com base na quantidade definida de restrições:
        for i in range(quantidade):
            tk.Label(self.root, text=f"Coeficientes da Restrição {i+1}:", 
                     font=('Helvetica', 12)).grid(row=3 + i * 2, column=0, columnspan=6, pady=5, sticky=tk.W)
        
            # Cria os campos de entradas para os coeficientes da restrição:
            coeficientes = self.create_entradas(4, 4 + i * 2)
        
            # Cria um combobox para selecionar o sinal da restrição (≤, ≥, =):
            sinal_restricao = ttk.Combobox(self.root, values=["≤", "≥", "="], font=('Helvetica', 12), state="readonly", width=2)
            sinal_restricao.grid(row=4 + i * 2, column=4, padx=5, pady=5, sticky=tk.W)
            sinal_restricao.current(0)   
        
            # Cria uma entrada para o lado direito da restrição:
            lado_direito = ttk.Entry(self.root, font=('Helvetica', 12))
            lado_direito.grid(row=4 + i * 2, column=5, padx=5, pady=5, sticky=tk.W)
        
            # Adiciona a restrição a lista:
            lista_restricoes.append((coeficientes, sinal_restricao, lado_direito))
            
        return lista_restricoes

    def solve(self):
        try:
            c = self.get_entradas(self.funcao_obj)
            
            # Inicializa listas vazias para as restrições de desigualdade e igualdade:
            A_ub, b_ub, A_eq, b_eq = [], [], [], []
            
            for coeficientes, sinal_restricao, lado_direito in self.restricoes:
                
                # Obtém os coeficientes da restrição atual:
                coef_atual = self.get_entradas(coeficientes)
                
                # Obtém o valor do lado direito e converte para flutuante:
                ld_atual = float(lado_direito.get() if lado_direito.get() else 0)
                
                # Verifica o sinal da restrição e atualiza as listas:
                if sinal_restricao.get() == "≤":
                    A_ub.append(coef_atual)
                    b_ub.append(ld_atual)
                elif sinal_restricao.get() == "≥":
                    A_ub.append([-val for val in coef_atual])  # inverte os coeficientes 
                    b_ub.append(-ld_atual)
                else:
                    A_eq.append(coef_atual)
                    b_eq.append(ld_atual)

            maximize = self.var_opcoes.get() == "maximize"
            
            # Chama o método simplex para resolver:
            result = simplex_method(c, 
                                    A_ub if A_ub else None, 
                                    b_ub if b_ub else None, 
                                    A_eq if A_eq else None,
                                    b_eq if b_eq else None, 
                                    maximize)
            
            # Exibe o resultado na interface:
            self.exibe_resultado(result, A_ub, b_ub, c)
            
        # Mostra uma mensagem de erro caso ocorra uma exceção de valor inválido:
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira coeficientes válidos.")
                       
    def get_entradas(self, entradas):
        # Converte as entradas para float, substituindo vírgulas por pontos e utilizando 0 para valores vazios:
        return [float(entry.get().replace(',', '.') if entry.get() else 0) for entry in entradas]

    def exibe_resultado(self, result, A, b, c):
        # Limpa o texto de saída:
        self.output.delete(1.0, tk.END)
        
        # Exibe o valor ótimo, solução ótima e os preços-sombra:
        if result.success:
            self.output.insert(tk.END, f"Valor Ótimo: R$ {result.fun:.2f}\n")
            solution = [f"{val:.2f}" for val in result.x]
            self.output.insert(tk.END, f"Solução Ótima: [{', '.join(solution)}]\n")

            if A and b:
                sombra_result = shadow_prices(np.array(A), np.array(b), np.array(c))
                if sombra_result.success:
                    preco_sombra = [f"{val:.2f}" for val in sombra_result.x]
                    self.output.insert(
                        tk.END, f"Preços-sombra (R$): [{', '.join(preco_sombra)}]\n")
                else:
                    self.output.insert(
                        tk.END, "Não foi possível calcular os preços-sombra\n")
            else:
                self.output.insert(
                    tk.END, "Não há restrições para calcular os preços-sombra\n")
        else:
            self.output.insert(tk.END, "Nenhuma solução encontrada\n")

root = tk.Tk()           # Cria a janela principal
app = SimplexApp(root)   # Cria uma instância da classe SimplexApp para configurar a interface
root.mainloop()          # Executa a aplicação