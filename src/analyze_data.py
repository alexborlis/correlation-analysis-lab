def compute_correlation_matrix(df):
    print("[INFO] Вибір числових колонок для побудови кореляційної матриці")
    numeric_df = df.select_dtypes(include='number')
    print(f"[INFO] Обрано {numeric_df.shape[1]} числових колонок")
    corr_matrix = numeric_df.corr()
    return corr_matrix
