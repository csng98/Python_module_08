import importlib.metadata
import sys


def check_dependencies() -> bool:
    required_packages = ["pandas", "numpy", "matplotlib"]
    all_ok = True

    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    for pkg in required_packages:
        try:
            version = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({version}) - Ready")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {pkg} is not installed!")
            all_ok = False

    return all_ok


def run_matrix_analysis() -> None:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    raw_data = np.random.normal(loc=0.0, scale=1.0, size=(1000, 2))
    df = pd.DataFrame(raw_data, columns=["Sentinels", "Zion_Signals"])

    plt.figure(figsize=(8, 5))
    plt.hist(df["Sentinels"], bins=30, alpha=0.5, label="Sentinel Activity")
    plt.hist(df["Zion_Signals"], bins=30, alpha=0.5, label="Zion Broadcasts")
    plt.title("Matrix Data Stream Analysis")
    plt.xlabel("Signal Frequency")
    plt.ylabel("Data Density")
    plt.legend()

    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def print_instructions() -> None:
    print("\n" + "!" * 40)
    print("DEPENDENCIES MISSING")
    print("!" * 40)
    print("To install with pip:\n  pip install -r requirements.txt")
    print("\nTo install with Poetry:\n  poetry install")


if __name__ == "__main__":
    if check_dependencies():
        try:
            run_matrix_analysis()
        except Exception as e:
            print(f"Data stream corruption averted! Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print_instructions()
