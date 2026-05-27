from pathlib import Path
from src.chat import ChatPrefeitura

def main():
    # Resolve caminho do CSV relativo ao projeto
    base = Path(__file__).resolve().parent.parent
    caminho = base / 'data' / 'dados.csv'
    chat = ChatPrefeitura(str(caminho))

    print('=== Chat IA Prefeitura ===')
    print("Digite 'sair' para encerrar.")
    while True:
        q = input('Você: ')
        if q.strip().lower() in ('sair','exit','quit'):
            break
        print('IA:', chat.responder(q))

if __name__ == '__main__':
    main()
