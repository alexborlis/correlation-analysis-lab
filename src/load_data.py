import os
import pandas as pd

def load_student_data(data_dir: str = "../data") -> pd.DataFrame:
    script_dir = os.path.dirname(os.path.abspath(__file__))  # src/
    abs_data_dir = os.path.abspath(os.path.join(script_dir, data_dir))

    if not os.path.isdir(abs_data_dir):
        raise NotADirectoryError(f"[ERROR] Не вдалося знайти папку: {abs_data_dir}")

    csv_files = [f for f in os.listdir(abs_data_dir) if f.endswith(".csv")]
    if not csv_files:
        raise FileNotFoundError(f"[ERROR] У папці {abs_data_dir} не знайдено CSV-файлів.")

    selected_file = os.path.join(abs_data_dir, csv_files[0])
    print(f"[INFO] Знайдено файл: {selected_file}")

    df = pd.read_csv(selected_file)
    print(f"[INFO] Форма датафрейму: {df.shape}")
    print(f"[INFO] Пропущені значення:\n{df.isnull().sum()}")
    return df
