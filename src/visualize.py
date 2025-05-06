import os
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(corr_matrix, show=True, save_path=None):
    print("[INFO] Побудова теплової карти")
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Кореляційна матриця")
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
        print(f"[INFO] Збережено до: {save_path}")

    if show:
        plt.show()

    plt.close()
