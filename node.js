const express = require('express');
const app = express();

app.use(express.json());

app.post('/data', (req, res) => {
    const data = req.body;
    // lógica para inserir dados no banco de dados
    res.status(201).json(data);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
