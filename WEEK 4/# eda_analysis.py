# eda_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
sns.set(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (12, 8)

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("✅ Data loaded. Shape:", df.shape)
    return df

def overview(df):
    print("\n--- Data Overview ---")
    print(df.head())
    print("\nInfo:")
    print(df.info())
    print("\nStatistics (numerical):")
    print(df.describe().T)

def missing_values(df):
    missing = df.isnull().sum()
    pct = (missing / len(df) * 100).round(2)
    missing_df = pd.DataFrame({'missing_count': missing, 'percent': pct})
    print("\n--- Missing Values ---")
    print(missing_df[missing_df.missing_count > 0])
    # Heatmap
    plt.figure(figsize=(10,6))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing data heatmap")
    plt.show()

def plot_distributions(df, num_cols):
    for col in num_cols:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True, bins=30)
        plt.title(f"Histogram & KDE – {col}")
        plt.show()

def detect_outliers(df, num_cols):
    for col in num_cols:
        plt.figure()
        sns.boxplot(x=df[col])
        plt.title(f"Box plot – {col}")
        plt.show()
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
        count = df[(df[col] < lower) | (df[col] > upper)].shape[0]
        print(f"{col}: {count} outliers (IQR method)")
        
def correlation_heatmap(df, num_cols):
    corr = df[num_cols].corr()
    plt.figure(figsize=(12,8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix Heatmap")
    plt.show()

def pairwise_relationships(df, cols):
    sns.pairplot(df[cols].dropna(), corner=True, diag_kind='kde')
    plt.suptitle("Pairwise relationships", y=1.02)
    plt.show()

def main():
    df = load_data("titanic_dataset.csv")
    overview(df)
    missing_values(df)
    
    # Identify numeric columns
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    print("\nNumeric columns:", num_cols)
    
    plot_distributions(df, num_cols)
    detect_outliers(df, num_cols)
    correlation_heatmap(df, num_cols)
    
    if len(num_cols) >= 3:
        sample_cols = num_cols[:5]  # Limit to first 5 for clarity
        pairwise_relationships(df, sample_cols)

if __name__ == "__main__":
    main()
