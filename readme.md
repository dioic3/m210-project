# Simplex Solver

Este projeto é uma aplicação web que resolve problemas de programação linear usando o método Simplex. A interface permite que os usuários insiram coeficientes para a função objetivo e restrições, e obtenham a solução ótima.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
├── .gitignore
├── simplex-web-app/
│   ├── backend/
│   │   ├── app.js
│   │   ├── readme.md
│   │   └── simplex.js
│   ├── front-end/
│   │   ├── index.html
│   │   ├── readme.md
│   │   ├── script.js
│   │   └── style.css
└── package.json
```


## Pré-requisitos

- Node.js
- Gerenciador de pacotes npm ou yarn

## Como Executar

### Passos

1. Clone o repositório:

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. Instale as dependências do projeto:

    ```bash
    npm install
    ```

3. Inicie o servidor back-end:

    ```bash
    node simplex-web-app/backend/app.js
    ```

4. Abra o arquivo `index.html` localizado em `simplex-web-app/front-end/` em um navegador web.

## Como Usar

1. Insira a quantidade de variáveis.
2. Insira os coeficientes da função objetivo.
3. Adicione as restrições necessárias.
4. Marque a opção "Maximizar" se desejar maximizar a função objetivo.
5. Clique em "Resolver" para obter a solução.

## Tecnologias Utilizadas

- `javascript-lp-solver`: Biblioteca para resolver problemas de programação linear.
- `Express.js`: Framework para construção de servidores web em Node.js.
- `CORS`: Middleware para habilitar requisições entre diferentes origens.
- `tkinter`: Biblioteca para criação de interfaces gráficas em Python.
- `scipy.optimize`: Biblioteca para otimização em Python.
- `NumPy`: Biblioteca para operações matemáticas em Python.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.