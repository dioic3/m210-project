// backend/simplex.js
const solver = require("javascript-lp-solver");

function simplexMethod(c, A_ub, b_ub, A_eq = [], b_eq = [], maximize = false) {
    const problem = {
        optimize: "x0",
        opType: maximize ? "max" : "min",
        constraints: {},
        variables: {},
    };

    // Define variáveis e coeficientes da função objetivo
    c.forEach((coef, idx) => {
        problem.variables[`x${idx + 1}`] = { x0: coef };
    });

    // Adiciona restrições ≤
    A_ub.forEach((row, i) => {
        row.forEach((val, j) => {
            const varName = `x${j + 1}`;
            if (!problem.variables[varName]) problem.variables[varName] = {};
            problem.variables[varName][`r${i + 1}`] = val;
        });
        problem.constraints[`r${i + 1}`] = { max: b_ub[i] };
    });

    // Adiciona restrições de igualdade
    A_eq.forEach((row, i) => {
        row.forEach((val, j) => {
            const varName = `x${j + 1}`;
            if (!problem.variables[varName]) problem.variables[varName] = {};
            problem.variables[varName][`eq${i + 1}`] = val;
        });
        problem.constraints[`eq${i + 1}`] = { equal: b_eq[i] };
    });

    // Resolve o problema
    const result = solver.Solve(problem);
    return result;
}

module.exports = simplexMethod;
