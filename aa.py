from scipy.optimize import linprog
import numpy as np

def simplex_method(c, A_ub, b_ub, A_eq, b_eq, maximize=False):
    # Inverte os coeficientes para maximizar:
    if maximize:
        c = [-coeff for coeff in c]

    res = linprog(c, A_ub, b_ub, A_eq, b_eq, method='simplex')

    # Inverte o valor da função objetivo:
    if maximize and res.success:
        res.fun = -res.fun

    return res

# O código implementa a função `shadow_prices`, que calcula os preços-sombra de um problema de programação linear usando o método Simplex.

def shadow_prices(A, b, c):
    dual_c = b
    dual_b = -1.0 * c
    dual_A = -1.0 * np.transpose(A)

    # Inicializa a matriz para o dual_A transformado:
    novo_A = np.zeros((len(A), len(A[0]) + 1))

    for i in range(len(dual_A[0])):
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

def main():
    # Entrada de dados pelo terminal
    c = list(map(float, input("Coeficientes da função objetivo (separados por espaço): ").split()))

    num_restricoes = int(input("Número de restrições: "))

    A_ub, b_ub, A_eq, b_eq = [], [], [], []

    for i in range(num_restricoes):
        coeficientes = list(map(float, input(f"Coeficientes da restrição {i+1} (separados por espaço): ").split()))
        sinal = input(f"Sinal da restrição {i+1} (<=, >=, =): ")
        while True:
            try:
                lado_direito = float(input(f"Lado direito da restrição {i+1}: "))
                break
            except ValueError:
                print("Por favor, insira um número válido.")

        if sinal == "<=":
            A_ub.append(coeficientes)
            b_ub.append(lado_direito)
        elif sinal == ">=":
            A_ub.append([-val for val in coeficientes])
            b_ub.append(-lado_direito)
        else:
            A_eq.append(coeficientes)
            b_eq.append(lado_direito)

    maximize = input("Deseja maximizar a função objetivo? (s/n): ").lower() == 's'

    # Chama o método simplex para resolver:
    result = simplex_method(c,
                            A_ub if A_ub else None,
                            b_ub if b_ub else None,
                            A_eq if A_eq else None,
                            b_eq if b_eq else None,
                            maximize)

    # Exibe o resultado no terminal:
    if result.success:
        print(f"Valor Ótimo: R$ {result.fun:.2f}")
        solution = [f"{val:.2f}" for val in result.x]
        print(f"Solução Ótima: [{', '.join(solution)}]")

        if A_ub and b_ub:
            sombra_result = shadow_prices(np.array(A_ub), np.array(b_ub), np.array(c))
            if sombra_result.success:
                preco_sombra = [f"{val:.2f}" for val in sombra_result.x]
                print(f"Preços-sombra (R$): [{', '.join(preco_sombra)}]")
            else:
                print("Não foi possível calcular os preços-sombra")
        else:
            print("Não há restrições para calcular os preços-sombra")
    else:
        print("Nenhuma solução encontrada")

if __name__ == "__main__":
    main()
