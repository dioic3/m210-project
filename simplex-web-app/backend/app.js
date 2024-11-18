// backend/app.js
const express = require("express");
const cors = require("cors");
const simplexMethod = require("./simplex");

const app = express();
app.use(cors());
app.use(express.json());

app.post("/solve", (req, res) => {
    const { c, A_ub, b_ub, A_eq, b_eq, maximize } = req.body;
    try {
        const result = simplexMethod(c, A_ub, b_ub, A_eq, b_eq, maximize);
        res.json(result);
    } catch (error) {
        res.status(400).json({ error: "Erro ao resolver o problema." });
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
