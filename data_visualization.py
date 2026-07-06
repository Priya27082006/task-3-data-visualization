import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Create folder for graphs
# -----------------------------
os.makedirs("visualizations", exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("books_dataset.csv")

print("\nDataset Loaded Successfully\n")

print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

# -----------------------------
# Data Cleaning
# -----------------------------
df = df.drop_duplicates()

df = df.dropna()

# Convert numeric columns
if "Price" in df.columns:
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

if "Rating" in df.columns:
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

df = df.dropna()

sns.set_style("whitegrid")

# =====================================================
# 1 Genre Wise Books
# =====================================================

if "Genre" in df.columns:

    plt.figure(figsize=(10,6))

    genre_counts = df["Genre"].value_counts()

    sns.barplot(
        x=genre_counts.index,
        y=genre_counts.values
    )

    plt.title("Books by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("visualizations/sales_by_genre.png")

    plt.show()

# =====================================================
# 2 Top Authors
# =====================================================

if "Author" in df.columns:

    plt.figure(figsize=(10,6))

    top_authors = df["Author"].value_counts().head(10)

    sns.barplot(
        x=top_authors.values,
        y=top_authors.index
    )

    plt.title("Top 10 Authors")

    plt.xlabel("Books")

    plt.ylabel("Author")

    plt.tight_layout()

    plt.savefig("visualizations/top_authors.png")

    plt.show()

# =====================================================
# 3 Rating Distribution
# =====================================================

if "Rating" in df.columns:

    plt.figure(figsize=(8,5))

    sns.histplot(df["Rating"], bins=10, kde=True)

    plt.title("Rating Distribution")

    plt.tight_layout()

    plt.savefig("visualizations/rating_distribution.png")

    plt.show()

# =====================================================
# 4 Price Distribution
# =====================================================

if "Price" in df.columns:

    plt.figure(figsize=(8,5))

    sns.histplot(df["Price"], bins=15, kde=True)

    plt.title("Price Distribution")

    plt.tight_layout()

    plt.savefig("visualizations/price_distribution.png")

    plt.show()

# =====================================================
# 5 Scatter Plot
# =====================================================

if "Price" in df.columns and "Rating" in df.columns:

    plt.figure(figsize=(8,6))

    sns.scatterplot(
        data=df,
        x="Price",
        y="Rating"
    )

    plt.title("Price vs Rating")

    plt.tight_layout()

    plt.savefig("visualizations/rating_vs_price.png")

    plt.show()

# =====================================================
# 6 Correlation Heatmap
# =====================================================

numeric_df = df.select_dtypes(include="number")

if len(numeric_df.columns) > 1:

    plt.figure(figsize=(8,6))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("visualizations/correlation_heatmap.png")

    plt.show()

print("\n--------------- DATA STORY ----------------")

if "Genre" in df.columns:
    print("Most Common Genre :", df["Genre"].mode()[0])

if "Author" in df.columns:
    print("Author with Most Books :", df["Author"].mode()[0])

if "Price" in df.columns:
    print("Average Price :", round(df["Price"].mean(), 2))
    print("Highest Price :", df["Price"].max())
    print("Lowest Price :", df["Price"].min())

if "Rating" in df.columns:
    print("Average Rating :", round(df["Rating"].mean(), 2))
    print("Highest Rating :", df["Rating"].max())
    print("Lowest Rating :", df["Rating"].min())

print("\nKey Insights:")
print("- Popular genres can help publishers understand reader preferences.")
print("- Top authors indicate which writers attract the most audience.")
print("- Price and rating comparison helps evaluate whether expensive books receive better ratings.")
print("- Correlation heatmap highlights relationships among numerical variables.")

print("\nVisualizations created successfully.")
print("All charts are saved inside the 'visualizations' folder.")