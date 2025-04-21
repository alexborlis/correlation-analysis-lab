import os
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(corr_matrix, output_path="reports/correlation_matrix.png"):
    # Створити папку, якщо не існує
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"[INFO] Візуалізація кореляційної матриці, збереження в {output_path}")
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Кореляційна матриця")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
