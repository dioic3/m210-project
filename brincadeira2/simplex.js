
const math = require('mathjs');

function initializeTable(c, A, b) {
    const m = A.length;
    const n = A[0].length;
    const table = math.zeros(m + 1, n + m + 1)._data;

    for (let j = 0; j < n; j++) {
        table[0][j] = -c[j];
    }
    table[0][n + m] = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            table[i + 1][j] = A[i][j];
        }
        table[i + 1][n + i] = 1;
        table[i + 1][n + m] = b[i];
    }

    return table;
}

function isOptimal(table) {
    return table[0].slice(0, -1).every(value => value >= 0);
}

function getPivotColumn(table) {
    return table[0].slice(0, -1).indexOf(Math.min(...table[0].slice(0, -1)));
}

function getPivotLine(table, enteringCol) {
    const rhs = table.slice(1).map(row => row[row.length - 1]);
    const column = table.slice(1).map(row => row[enteringCol]);

    const ratios = rhs.map((value, index) => column[index] > 0 ? value / column[index] : Infinity);
    return ratios.indexOf(Math.min(...ratios)) + 1;
}

function updateTable(table, pivotRow, pivotCol) {
    const pivotElement = table[pivotRow][pivotCol];
    table[pivotRow] = table[pivotRow].map(value => value / pivotElement);

    for (let row = 0; row < table.length; row++) {
        if (row === pivotRow) continue;
        const multiplier = table[row][pivotCol];
        table[row] = table[row].map((value, index) => value - multiplier * table[pivotRow][index]);
    }
}

function solveSimplex(c, A, b) {
    let table = initializeTable(c, A, b);
    let iteration = 0;

    while (!isOptimal(table)) {
        console.log(`Iteração ${iteration}:`);
        console.log(math.round(table, 2));
        console.log();

        const pivotCol = getPivotColumn(table);
        const pivotRow = getPivotLine(table, pivotCol);
        updateTable(table, pivotRow, pivotCol);

        iteration += 1;
    }

    console.log(`Iteração ${iteration}:`);
    console.log(math.round(table, 2));
    console.log();

    const optimalPoint = table.slice(1).map(row => row[row.length - 1]);
    const shadowPrices = table[0].slice(0, -1);
    const z = table[0][table[0].length - 1];

    return [optimalPoint, shadowPrices, z];
}

module.exports = { solveSimplex };