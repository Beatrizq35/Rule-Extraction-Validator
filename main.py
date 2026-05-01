import os
from core.extractor import PdfExtractor
from core.analyzer import MetricAnalyzer

# Configurações de caminhos
PATHS = {
    "pdfs": "./datasets",
    "gabaritos": "./ground-truth",
    "output": "./outputs",
    "extractions": "./extractions",
    "comparisons": "./comparisons"
}

def run_pipeline():
    # Inicializa os componentes
    extractor = PdfExtractor()
    analyzer = MetricAnalyzer()
    
    os.makedirs(PATHS["output"], exist_ok=True)
    os.makedirs(PATHS["extractions"], exist_ok=True)
    os.makedirs(PATHS["comparisons"], exist_ok=True)
    files = [f for f in os.listdir(PATHS["pdfs"]) if f.endswith(".pdf")]

    print(f"{'Documento':<25} | {'Recall':<8} | {'Status'}")
    print("-" * 50)

    for file_name in files:
        base_name = os.path.splitext(file_name)[0]
        pdf_path = os.path.join(PATHS["pdfs"], file_name)
        csv_path = os.path.join(PATHS["gabaritos"], f"{base_name}.csv")

        try:
            # 1. Extraction
            markdown_content = extractor.to_markdown(pdf_path)
            save_extraction(base_name, markdown_content)
            
            # 2. Loading Ground Truth
            rules = analyzer.load_ground_truth(csv_path)
            if rules is None:
                print(f"Gabarito ausente: {file_name}")
                continue

            # 3. Analysis
            recall, found, missing = analyzer.calculate_recall(rules, markdown_content)

            # 4. Feedback and Log
            print(f"{file_name[:25]:<25} | {recall:>7.1%} | {len(found)}/{len(rules)}")
            
            save_report(base_name, recall, missing)
            save_comparison(base_name, rules, found)

        except Exception as e:
            print(f"Erro em {file_name}: {e}")

def save_report(name, recall, missing):
    """Gera um pequeno arquivo de texto com o que faltou."""
    path = os.path.join(PATHS["output"], f"falhas_{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Resultado Revocação: {recall:.2%}\n")
        f.write("Regras NÃO encontradas:\n" + "\n".join([f"- {m}" for m in missing]))

def save_extraction(name, content):
    """Salva a extração completa em Markdown."""
    path = os.path.join(PATHS["extractions"], f"{name}_extracted.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def save_comparison(name, expected_rules, found_rules):
    """Salva a comparação com o gabarito em uma pasta separada."""
    path = os.path.join(PATHS["comparisons"], f"{name}_comparison.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("Regra | Status\n")
        f.write("--- | ---\n")
        for rule in expected_rules:
            status = "ENCONTRADA" if rule in found_rules else "NÃO ENCONTRADA"
            f.write(f"{rule} | {status}\n")

if __name__ == "__main__":
    run_pipeline()