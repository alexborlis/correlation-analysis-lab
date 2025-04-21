import os
import pandas as pd

def load_student_data(data_dir: str = "../data") -> pd.DataFrame:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_data_dir = os.path.abspath(os.path.join(script_dir, data_dir))

    file = "studentInfo.csv"
    file_path = os.path.join(abs_data_dir, file)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[ERROR] Файл не знайдено: {file_path}")

    print(f"[INFO] Завантаження файлу: {file_path}")
    df = pd.read_csv(file_path)
    print(f"[INFO] Форма датафрейму: {df.shape}")
    print(f"[INFO] Пропущені значення:\n{df.isnull().sum()}")
    return df

