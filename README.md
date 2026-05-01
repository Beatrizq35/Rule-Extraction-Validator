# Rule Extraction Validator - PIBIC Project

Este projeto foi desenvolvido para automatizar a validação de extração de regras a partir de documentos PDF, utilizando a biblioteca **Docling**. O objetivo principal é calcular a métrica de **Recall (Revocação)** para verificar se todas as regras presentes no gabarito oficial (**Ground Truth**) foram corretamente identificadas pela IA no documento de entrada.

## Pipeline de Processamento

O programa segue um fluxo dividido em três etapas principais:

1.  **Extraction**: O motor do **Docling** converte o PDF original para o formato Markdown, preservando a estrutura semântica do texto.
2.  **Loading Ground Truth**: Utilizando a biblioteca **Pandas**, o sistema carrega o arquivo CSV contendo as regras esperadas (coluna `rule`).
3.  **Analysis**: O script compara o conteúdo extraído com o gabarito, quantifica os acertos e gera um relatório detalhado das falhas.

---

## Estrutura de Pastas

```text
rules-validator/
├── core/               # Módulos de extração e análise
├── datasets/           # Arquivos originais .pdf para análise
├── ground-truth/       # Arquivos gabarito .csv 
├── outputs/            # Relatórios de falhas gerados automaticamente
├── main.py             # Script principal (Orquestrador)
└── requirements.txt    # Lista de dependências
```

---

## Preparando o Ambiente (VENV)

### 1. Criar o ambiente virtual
Abra o terminal na pasta do projeto e digite:
* **Windows/Linux/Mac**: `python3 -m venv .venv`

### 2. Ativar o ambiente
Isso fará com que o terminal "foque" apenas no seu projeto.
* **Windows**: `.\.venv\Scripts\activate`
* **Linux/Mac**: `source .venv/bin/activate`

> **Nota**: Quando ativado, o nome `(.venv)` aparecerá no início da linha do seu terminal.

### 3. Instalar as dependências
Com o ambiente ativo, instale as ferramentas necessárias:
* `pip install -r requirements.txt`

---

## Como Utilizar

1.  Os arquivos devem ter o mesmo nome. Ex: `sisu-rules.pdf` e `sisu-rules.csv`.
2.  O CSV deve possuir a coluna intitulada `rule`.
3.  Execute o programa:
    ```bash
    python3 main.py
    ```
4.  Resultados resumidos no terminal e os logs detalhados na pasta `outputs/`.

---

## Requisitos
* Python 3.10 ou superior
* Bibliotecas: `docling`, `pandas`

# Rule-Extraction-Validator
