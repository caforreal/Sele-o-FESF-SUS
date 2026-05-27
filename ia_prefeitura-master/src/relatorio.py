from .analise import PrefeituraAnalise
import matplotlib.pyplot as plt
from pathlib import Path

class Relatorio:
    def __init__(self, caminho_csv):
        self.ia = PrefeituraAnalise(caminho_csv)

    def gerar_grafico_gastos(self, saida_png='gastos.png'):
        df = self.ia.df
        if 'ano' in df.columns and 'gastos_saude' in df.columns:
            df_sorted = df.sort_values('ano')
            plt.figure(figsize=(8,4))
            plt.plot(df_sorted['ano'], df_sorted['gastos_saude'], marker='o')
            plt.title('Gastos com Saúde por Ano')
            plt.xlabel('Ano')
            plt.ylabel('Gastos com Saúde')
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(saida_png)
            plt.close()
            return Path(saida_png).resolve()
        else:
            raise ValueError('Colunas esperadas não encontradas no CSV.')
