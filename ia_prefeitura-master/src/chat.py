from .analise import PrefeituraAnalise

class ChatPrefeitura:
    def __init__(self, caminho_csv):
        self.ia = PrefeituraAnalise(caminho_csv)

    def responder(self, texto):
        text = texto.lower()
        # regras simples de intenção
        if 'gasto' in text and 'saúde' in text or ('gasto' in text and 'saude' in text):
            # tenta extrair ano no texto
            import re
            m = re.search(r'(\d{4})', text)
            if m:
                ano = int(m.group(1))
            else:
                return 'Por favor, informe o ano (por exemplo: 2020).'
            val = self.ia.gasto_por_ano(ano, 'gastos_saude')
            if val is None:
                return f'Nenhum dado encontrado para {ano}.'
            return f'Gasto com saúde em {ano}: {int(val):,}'.replace(',', '.')
        if 'média' in text and 'educa' in text:
            media = self.ia.media_gastos('gastos_educacao')
            return f'Média de gastos com educação: {media:,.2f}'.replace(',', '.')
        if 'resumo' in text or 'estatística' in text or 'resumo geral' in text:
            resumo = self.ia.resumo_geral()
            lines = []
            for k,v in resumo.items():
                lines.append(f"{k}: média={v['media']:.2f}, soma={v['soma']:.0f}")
            return '\n'.join(lines) if lines else 'Nenhuma estatística disponível.'
        return 'Desculpe, não entendi. Pergunte sobre gastos (saúde/educação) ou peça resumo geral.'

if __name__ == '__main__':
    chat = ChatPrefeitura('../data/dados.csv')
    print('Chat IA Prefeitura (digite sair para encerrar)')
    while True:
        q = input('Você: ')
        if q.strip().lower() in ('sair','exit','quit'):
            break
        print('IA:', chat.responder(q))
