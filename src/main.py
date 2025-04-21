from load_data import load_student_data
from analyze_data import compute_correlation_matrix
from visualize import plot_correlation_heatmap

def main():
    print("[START] Аналіз кореляції на основі studentVle.csv")

    df = load_student_data("../data")
    corr_matrix = compute_correlation_matrix(df)
    plot_correlation_heatmap(corr_matrix)

    print("[DONE] Аналіз завершено!")

if __name__ == "__main__":
    main()