
const readline = require('readline');
const { solveSimplex } = require('./simplex');
const math = require('mathjs');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function readMatrix(rows, cols, name, callback) {
    console.log(`Digite os elementos da matriz ${name} (${rows}x${cols}):`);
    let matrix = [];
    let rowCounter = 0;

    function readRow() {
        rl.question(`Linha ${rowCounter + 1}: `, (input) => {
            matrix.push(input.split(' ').map(Number));
            rowCounter++;
            if (rowCounter < rows) {
                readRow();
            } else {
                callback(matrix);
            }
        });
    }

    readRow();
}

function readVector(size, name, callback) {
    rl.question(`Digite os elementos do vetor ${name} (${size} elementos): `, (input) => {
        const vector = input.split(' ').map(Number);
        callback(vector);
    });
}

rl.question('Digite o número de variáveis: ', (numVars) => {
    rl.question('Digite o número de restrições: ', (numConstraints) => {
        readVector(Number(numVars), 'c', (c) => {
            readMatrix(Number(numConstraints), Number(numVars), 'A', (A) => {
                readVector(Number(numConstraints), 'b', (b) => {
                    const [optimalSolution, shadowPrices, objectiveValue] = solveSimplex(c, A, b);

                    const optimalSolutionRounded = optimalSolution.map(value => math.round(value, 2));
                    const shadowPricesRounded = shadowPrices.map(value => math.round(value, 2));
                    const objectiveValueRounded = math.round(objectiveValue, 2);

                    console.log('Ponto ótimo:', optimalSolutionRounded);
                    console.log('Preços sombra:', shadowPricesRounded);
                    console.log('Valor da função objetivo:', objectiveValueRounded);

                    rl.close();
                });
            });
        });
    });
});