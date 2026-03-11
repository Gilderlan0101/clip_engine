#!/bin/bash

# Aborta o script se algum comando falhar
set -e

echo "--- 🛠️ Iniciando formatação de código ---"

echo "Roda Black..."
#blue .

# 2. Roda o isort
echo "Roda isort..."
#isort .

echo "--- 🚀 Iniciando Uvicorn com Reload ---"

# 3. Roda o uvicorn chamando o objeto 'app' no arquivo 'main.py'
# Usamos 'python3 -m uvicorn' para garantir que ele use o ambiente atual
python3 -m uvicorn main:app
