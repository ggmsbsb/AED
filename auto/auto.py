import os
import re

# Diretórios
exercicios_dir = r"D:\CDMI\AED\lista"  # Corrigido para a pasta correta
readme_file = r"D:\CDMI\AED\readme.md"

# Inicializa um conjunto vazio para armazenar as bibliotecas únicas
bibliotecas_utilizadas = set()

# Percorre os arquivos de exercícios
for root, dirs, files in os.walk(exercicios_dir):
    for file in files:
        if file.startswith("ex") and file.endswith(".py"):  # Filtra apenas arquivos com prefixo "ex" e extensão ".py"
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:  # Especifica a codificação como UTF-8
                codigo = f.read()
                # Encontra todas as importações de bibliotecas usando regex
                bibliotecas = re.findall(r"import\s+(\w+)|from\s+(\w+)\s+import", codigo)
                for importacao in bibliotecas:
                    for biblioteca in importacao:
                        if biblioteca:
                            bibliotecas_utilizadas.add(biblioteca)

# Ordena as bibliotecas utilizadas
bibliotecas_utilizadas = sorted(list(bibliotecas_utilizadas))

# Formata as bibliotecas para o formato Markdown
bibliotecas_formatadas = "  - " + "\n  - ".join(bibliotecas_utilizadas)

# Atualiza o README.md
with open(readme_file, "a", encoding="utf-8") as readme:  # Especifica a codificação como UTF-8
    readme.write("\nBibliotecas utilizadas nos exercícios:\n\n")
    readme.write(bibliotecas_formatadas)
    readme.write("\n")
