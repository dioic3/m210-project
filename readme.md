# Simplex Solver

Este projeto é uma aplicação web que resolve problemas de programação linear usando o método Simplex. A interface permite que os usuários insiram coeficientes para a função objetivo e restrições, e obtenham a solução ótima.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
├── m210-project/
├── code-simplex.py
└── readme.md
```

## Pré-requisitos

- Node.js
- Gerenciador de pacotes npm ou yarn
- Python 3.x
- Bibliotecas Python: `numpy`, `tkinter`

## Como Executar

### Passos

1. Clone o repositório:

    ```bash
    git clone https://github.com/dioic3/m210-project.git
    cd m210-project
    ```

2. Instale as dependências do Python:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute a aplicação Python:

    ```bash
    python code-simplex.py
    ```

## Como Usar

1. Insira a quantidade de variáveis.
2. Insira os coeficientes da função objetivo.
3. Adicione as restrições necessárias.
4. Marque a opção "Maximizar" se desejar maximizar a função objetivo.
5. Clique em "Resolver" para obter a solução.

## Explicação do Código

O arquivo `code-simplex.py` contém uma implementação do método Simplex usando Python e a biblioteca `tkinter` para a interface gráfica. Aqui está um resumo das principais funções:

- `obter_dados(entry_vars, entry_cons, entry_obj)`: Coleta os dados de entrada do usuário e os converte em arrays NumPy.
- `simplex(funcObj, restricoes, constantes)`: Implementa o algoritmo Simplex para encontrar a solução ótima.
- `iniciar_calculo(entry_vars, entry_cons, entry_obj)`: Inicia o cálculo chamando `obter_dados` e `simplex`, e exibe os resultados.
- `main()`: Configura a interface gráfica usando `tkinter` e define os campos de entrada e botões.

## Tecnologias Utilizadas

- `javascript-lp-solver`: Biblioteca para resolver problemas de programação linear.
- `Express.js`: Framework para construção de servidores web em Node.js.
- `CORS`: Middleware para habilitar requisições entre diferentes origens.
- `tkinter`: Biblioteca para criação de interfaces gráficas em Python.
- `NumPy`: Biblioteca para operações matemáticas em Python.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.