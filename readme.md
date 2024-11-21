# Método Simplex com Interface Gráfica

## Descrição Geral
Este projeto implementa o Método Simplex para resolver problemas de otimização linear. Ele utiliza a biblioteca Tkinter para criar uma interface gráfica de usuário (GUI) que permite configurar e calcular o problema. O programa aceita como entrada o número de variáveis e restrições, os coeficientes da função objetivo e das restrições, e calcula a solução ótima, o valor máximo da função objetivo, e os preços sombra.

## Requisitos
Certifique-se de instalar os seguintes pacotes antes de executar o código. As dependências estão listadas no arquivo `requirements.txt`:

```plaintext
numpy==<versão>
tk==<versão>
```

Instale os requisitos com:

```bash
pip install -r requirements.txt
```

## Estrutura do Código

### Importação de Bibliotecas
- `numpy`: Para manipulação de arrays e cálculos numéricos.
- `tkinter`: Para criação da interface gráfica.
- `messagebox`: Para exibir mensagens de erro ou informações ao usuário.

### Funções Principais

#### obter_dados
- Coleta e valida os dados inseridos na GUI.
- Retorna os coeficientes da função objetivo, as restrições e os valores constantes.

#### simplex
- Implementa o algoritmo do Método Simplex.
- Resolve o problema de otimização linear, retornando:
    - A solução ótima.
    - O valor máximo da função objetivo.
    - Os preços sombra.

#### iniciar_calculo
- Conecta a interface gráfica com a lógica do Método Simplex.
- Exibe o resultado na interface.

### Função main
- Configura e inicializa a interface gráfica.
- Permite ao usuário:
    - Inserir o número de variáveis e restrições.
    - Adicionar os coeficientes necessários.
    - Calcular os resultados.

## Execução
O programa é executado a partir da função `main`, que inicializa a GUI.

## Fluxo de Execução
1. O usuário executa o programa.
2. Na interface:
     - Insere o número de variáveis e restrições.
     - Clica no botão "Criar Campos" para gerar os campos de entrada necessários.
     - Preenche os coeficientes da função objetivo e das restrições.
     - Clica em "Calcular".
3. O programa valida os dados e realiza o cálculo usando o Método Simplex.
4. O resultado (solução ótima, valor ótimo e preços sombra) é exibido em uma janela pop-up.

## Detalhes do Algoritmo Simplex

### Entrada:
- Vetor de coeficientes da função objetivo (`funcObj`).
- Matriz de coeficientes das restrições (`restric`).
- Vetor dos termos constantes das restrições (`const`).

### Processo:
- Constrói o tableau inicial adicionando variáveis de folga.
- Itera até encontrar uma solução ótima ou detectar inconsistências.
- Utiliza operações de pivô para ajustar o tableau.

### Saída:
- Vetor de solução (`solucao`).
- Valor máximo da função objetivo (`valorOtimo`).
- Preços sombra (`precoSombra`).

## Interface Gráfica

### Entradas:
- Número de variáveis.
- Número de restrições.
- Coeficientes da função objetivo.
- Coeficientes e constantes das restrições.

### Botões:
- "Criar Campos": Gera os campos de entrada para os dados.
- "Calcular": Executa o cálculo e exibe o resultado.

## Exemplo de Uso
1. Execute o programa.
2. Insira 2 como número de variáveis e 2 como número de restrições.
3. Clique em "Criar Campos".
4. Insira os coeficientes:
     - Função objetivo: 3, 5.
     - Restrições:
         - 1, 0 e constante 4.
         - 0, 2 e constante 12.
5. Clique em "Calcular".
6. O resultado será exibido como:

```plaintext
Solução Ótima: [4.0, 6.0]
Lucro Ótimo: 38.0
Preços Sombra: [0.0, 1.0]
```

## Erros Comuns
- Valores inválidos: Insira números válidos nos campos de entrada para evitar erros.
- Número de variáveis/restrições inconsistente: Certifique-se de criar campos antes de calcular.

## Considerações Finais
Este programa é uma aplicação prática para resolver problemas de otimização linear, útil para estudantes e profissionais. A modularidade e clareza do código facilitam futuras melhorias ou adaptações.
