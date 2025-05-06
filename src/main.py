from load_data import load_student_data
from analyze_data import compute_correlation_matrix
from visualize import plot_correlation_heatmap


def log_status(message):
    print(f"[STATUS] {message}")


def run_analysis():
    log_status("Аналіз кореляції на основі studentInfo.csv")
    df = load_student_data("../data")
    corr_matrix = compute_correlation_matrix(df)
    plot_correlation_heatmap(corr_matrix)
    log_status("Аналіз завершено!")


def main():
    run_analysis()


if __name__ == "__main__":
    main()
