import os
import pandas as pd


def get_absolute_path(relative_dir: str, filename: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_dir = os.path.abspath(os.path.join(script_dir, relative_dir))
    return os.path.join(abs_dir, filename)


def load_student_data(data_dir: str = "../data", filename: str = "studentInfo.csv") -> pd.DataFrame:
    file_path = get_absolute_path(data_dir, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[ERROR] Файл не знайдено: {file_path}")

    print(f"[INFO] Завантаження файлу: {file_path}")
    df = pd.read_csv(file_path)
    print(f"[INFO] Форма датафрейму: {df.shape}")
    print(f"[INFO] Пропущені значення:\n{df.isnull().sum()}")
    return df
