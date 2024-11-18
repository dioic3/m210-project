let constraintCount = 0;

function updateObjectiveInputs() {
    const variableCount = parseInt(document.getElementById("variable-count").value);
    const objectiveInputs = document.getElementById("objective-inputs");
    objectiveInputs.innerHTML = "";

    for (let i = 0; i < variableCount; i++) {
        const input = document.createElement("input");
        input.type = "number";
        input.placeholder = `Coeficiente x${i + 1}`;
        input.classList.add("obj-coeff");
        objectiveInputs.appendChild(input);
    }
}

function addConstraint() {
    const variableCount = parseInt(document.getElementById("variable-count").value);
    constraintCount++;

    const container = document.getElementById("constraints-container");

    const constraintDiv = document.createElement("div");
    constraintDiv.classList.add("constraint");

    // Campos de coeficientes
    for (let i = 0; i < variableCount; i++) {
        const input = document.createElement("input");
        input.type = "number";
        input.placeholder = `Coeficiente x${i + 1}`;
        input.classList.add("constraint-coeff");
        constraintDiv.appendChild(input);
    }

    // Combobox para o sinal da restrição
    const select = document.createElement("select");
    select.innerHTML = `
        <option value="<=">≤</option>
        <option value=">=">≥</option>
        <option value="=">=</option>
    `;
    constraintDiv.appendChild(select);

    // Campo para o lado direito da restrição
    const rhsInput = document.createElement("input");
    rhsInput.type = "number";
    rhsInput.placeholder = "Lado direito";
    rhsInput.classList.add("constraint-rhs");
    constraintDiv.appendChild(rhsInput);

    // Botão para remover restrição
    const removeButton = document.createElement("button");
    removeButton.textContent = "Remover";
    removeButton.onclick = () => container.removeChild(constraintDiv);
    constraintDiv.appendChild(removeButton);

    container.appendChild(constraintDiv);
}

async function solve() {
    // Coletar coeficientes da função objetivo
    const c = Array.from(document.querySelectorAll(".obj-coeff")).map((input) => parseFloat(input.value) || 0);

    const A_ub = [];
    const b_ub = [];
    const A_eq = [];
    const b_eq = [];

    // Coletar coeficientes e restrições
    document.querySelectorAll(".constraint").forEach((constraint) => {
        const coeffs = Array.from(constraint.querySelectorAll(".constraint-coeff")).map((input) => parseFloat(input.value) || 0);
        const sign = constraint.querySelector("select").value;
        const rhs = parseFloat(constraint.querySelector(".constraint-rhs").value) || 0;

        if (sign === "<=") {
            A_ub.push(coeffs);
            b_ub.push(rhs);
        } else if (sign === ">=") {
            A_ub.push(coeffs.map((val) => -val));
            b_ub.push(-rhs);
        } else {
            A_eq.push(coeffs);
            b_eq.push(rhs);
        }
    });

    const maximize = document.getElementById("maximize").checked;

    const data = { c, A_ub, b_ub, A_eq, b_eq, maximize };

    try {
        const response = await fetch("http://localhost:3000/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        const outputElement = document.getElementById("output");

        if (result.feasible && result.bounded) {
            let outputText = "Solução Ótima Encontrada:\n";
            outputText += `Valor Ótimo: ${result.result}\n\n`;
            outputText += "Valores das Variáveis:\n";
            for (const [variable, value] of Object.entries(result)) {
                if (variable !== "result" && variable !== "feasible" && variable !== "bounded") {
                    outputText += `${variable}: ${value}\n`;
                }
            }
            outputElement.textContent = outputText;
        } else if (!result.bounded) {
            outputElement.textContent = "A solução não é limitada.";
        } else {
            outputElement.textContent = "Não foi possível encontrar uma solução viável.";
        }
    } catch (error) {
        document.getElementById("output").textContent = "Erro ao resolver o problema.";
    }
}

// Inicializa os campos de entrada da função objetivo
updateObjectiveInputs();
