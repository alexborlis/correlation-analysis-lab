import pandas as pd


def encode_categorical(df):
    print("[INFO] Обробка категоріальних змінних")
    df_encoded = pd.get_dummies(df, drop_first=True)
    print(f"[INFO] Перетворений датафрейм: {df_encoded.shape}")
    return df_encoded


def compute_correlation_matrix(df):
    encoded_df = encode_categorical(df)
    return encoded_df.corr()
