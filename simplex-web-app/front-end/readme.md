# Simplex Solver Front-End

Este projeto é uma aplicação web que resolve problemas de programação linear usando o método Simplex. A interface permite que os usuários insiram coeficientes para a função objetivo e restrições, e obtenham a solução ótima.

## Estrutura dos Arquivos

- `index.html`: Estrutura HTML da aplicação.
- `style.css`: Estilos CSS para a interface.
- `script.js`: Lógica JavaScript para manipulação da interface e comunicação com o back-end.

## Como Funciona

### index.html

Este arquivo contém a estrutura básica da aplicação, incluindo:

- Um campo para inserir a quantidade de variáveis.
- Campos para inserir os coeficientes da função objetivo.
- Seção para adicionar restrições.
- Checkbox para selecionar se a função objetivo deve ser maximizada.
- Botão para resolver o problema.
- Área para exibir os resultados.

### style.css

Este arquivo define os estilos para a interface, incluindo:

- Estilos para o corpo da página, títulos, seções e botões.
- Estilos específicos para inputs e botões de ação.

### script.js

Este arquivo contém a lógica para:

- Atualizar os campos de entrada da função objetivo com base na quantidade de variáveis.
- Adicionar novas restrições dinamicamente.
- Coletar os dados inseridos pelo usuário e enviá-los para o back-end.
- Exibir os resultados retornados pelo back-end.

### Funcionalidades

1. **Quantidade de Variáveis**: O usuário pode definir a quantidade de variáveis que deseja usar.
2. **Função Objetivo**: O usuário insere os coeficientes da função objetivo.
3. **Restrições**: O usuário pode adicionar múltiplas restrições, definindo coeficientes, sinais e valores do lado direito.
4. **Maximizar**: O usuário pode selecionar se deseja maximizar a função objetivo.
5. **Resolver**: Ao clicar no botão "Resolver", os dados são enviados para o back-end, que retorna a solução ótima.

### Como Usar

1. Abra o arquivo `index.html` em um navegador web.
2. Insira a quantidade de variáveis.
3. Insira os coeficientes da função objetivo.
4. Adicione as restrições necessárias.
5. Marque a opção "Maximizar" se desejar maximizar a função objetivo.
6. Clique em "Resolver" para obter a solução.

### Requisitos

- Navegador web moderno.
- Servidor back-end configurado para resolver problemas de programação linear.

### Exemplo de Uso

1. Defina a quantidade de variáveis como 3.
2. Insira os coeficientes da função objetivo: 2, 3, 4.
3. Adicione uma restrição: 1x1 + 1x2 + 1x3 ≤ 10.
4. Marque a opção "Maximizar".
5. Clique em "Resolver" e veja a solução exibida na área de resultados.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.