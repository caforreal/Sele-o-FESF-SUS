from .data_loader import load_csv
import numpy as np

class PrefeituraAnalise:
    def __init__(self, caminho_csv):
        self.df = load_csv(caminho_csv)

    def gasto_por_ano(self, ano, categoria):
        d = self.df
        if 'ano' in d.columns:
            row = d.loc[d['ano'] == int(ano)]
            if not row.empty and categoria in d.columns:
                val = row.iloc[0][categoria]
                return int(val) if not np.isnan(val) else None
        return None

    def media_gastos(self, categoria):
        if categoria in self.df.columns:
            vals = self.df[categoria].dropna().astype(float)
            if len(vals) == 0:
                return 0
            return float(vals.mean())
        return 0

    def resumo_geral(self):
        """Retorna um dicionário com algumas estatísticas básicas."""
        resumo = {}
        for col in self.df.columns:
            if np.issubdtype(self.df[col].dtype, np.number):
                resumo[col] = {
                    'media': float(self.df[col].mean()),
                    'soma': float(self.df[col].sum()),
                    'min': float(self.df[col].min()),
                    'max': float(self.df[col].max())
                }
        return resumo
