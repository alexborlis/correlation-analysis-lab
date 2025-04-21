import pandas as pd

def compute_correlation_matrix(df):
    print("[INFO] Обробка категоріальних змінних")
    df_encoded = pd.get_dummies(df, drop_first=True)

    print(f"[INFO] Перетворений датафрейм: {df_encoded.shape}")
    corr_matrix = df_encoded.corr()
    return corr_matrix


