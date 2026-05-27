import pandas as pd
from pathlib import Path

def load_csv(caminho):
    """Carrega CSV de forma robusta com pandas e normaliza colunas numéricas."""
    path = Path(caminho)
    if not path.exists():
        # tenta caminho relativo ao arquivo atual (quando executado via python -m src.main)
        base = Path(__file__).resolve().parent.parent
        candidate = base / caminho
        if candidate.exists():
            path = candidate
        else:
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}") from None
    df = pd.read_csv(path)
    # tenta converter colunas numéricas automaticamente
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='ignore')
        except Exception:
            pass
    return df
