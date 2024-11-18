# Documentação do Projeto

Este projeto implementa uma API para resolver problemas de programação linear utilizando o método Simplex. Ele é composto por dois componentes principais: um módulo de back-end que resolve o problema e um servidor que expõe a funcionalidade via uma API REST.

## Estrutura do Projeto

```
backend/
├── simplex.js  # Implementação do método Simplex
├── app.js      # API Express para interação com o método Simplex
```

### Arquivo: simplex.js

#### Descrição

Este módulo implementa o método Simplex utilizando a biblioteca `javascript-lp-solver`. Ele é responsável por criar a estrutura do problema e resolvê-lo.

#### Função: `simplexMethod`

**Parâmetros:**
- `c`: Array de coeficientes da função objetivo.
- `A_ub`: Matriz de coeficientes das restrições do tipo ≤.
- `b_ub`: Array de valores à direita das restrições do tipo ≤.
- `A_eq` (opcional): Matriz de coeficientes das restrições de igualdade.
- `b_eq` (opcional): Array de valores à direita das restrições de igualdade.
- `maximize` (opcional): Booleano para indicar se a função objetivo deve ser maximizada (padrão: false).

**Retorno:**
Objeto com as seguintes propriedades:
- `feasible`: Indica se o problema possui solução.
- `bounded`: Indica se a solução encontrada é limitada.
- `result`: Valor da solução ótima.
- Demais variáveis de decisão e valores correspondentes.

**Exemplo de Uso:**

```javascript
const c = [3, 2];
const A_ub = [[1, 1], [2, 1]];
const b_ub = [8, 10];
const result = simplexMethod(c, A_ub, b_ub, [], [], true);
console.log(result);
```

### Arquivo: app.js

#### Descrição

Este arquivo implementa um servidor HTTP utilizando Express.js. Ele expõe uma API REST para resolver problemas de programação linear.

#### Endpoints

**POST /solve**

Resolve um problema de programação linear enviado no corpo da requisição.

**Parâmetros (Body):**
- `c` (array): Coeficientes da função objetivo.
- `A_ub` (array de arrays): Coeficientes das restrições ≤.
- `b_ub` (array): Lados direitos das restrições ≤.
- `A_eq` (array de arrays, opcional): Coeficientes das restrições de igualdade.
- `b_eq` (array, opcional): Lados direitos das restrições de igualdade.
- `maximize` (booleano, opcional): Maximizar ou minimizar a função objetivo (padrão: false).

**Respostas:**
- `200 OK`: Retorna o resultado da resolução.
    ```json
    {
        "feasible": true,
        "bounded": true,
        "result": 18,
        "x1": 6,
        "x2": 2
    }
    ```
- `400 Bad Request`: Retorna um erro caso o problema não possa ser resolvido.
    ```json
    { "error": "Erro ao resolver o problema." }
    ```

## Como Executar

### Pré-requisitos

- Node.js
- Gerenciador de pacotes npm ou yarn

### Passos

1. Instale as dependências:
     ```bash
     npm install
     ```

2. Inicie o servidor:
     ```bash
     node backend/app.js
     ```

3. Acesse a API em `http://localhost:3000/solve`.

## Tecnologias Utilizadas

- `javascript-lp-solver`: Biblioteca para resolver problemas de programação linear.
- `Express.js`: Framework para construção de servidores web em Node.js.
- `CORS`: Middleware para habilitar requisições entre diferentes origens.