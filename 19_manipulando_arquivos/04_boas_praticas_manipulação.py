from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "Llorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"erro ao abrir o arquivo {exc}")

#try:
#    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#        arquivo.write("Aprendendo a manipular arquivos utilizando python.")
#except IOError as exc:
#    print(f"Erro ao abrir o arquivo {exc}")

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
        print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
     print(exc)