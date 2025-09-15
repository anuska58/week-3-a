# EXERCISE 1: Fibonacci
def fib(n):
    """Return the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(f"fib(10): {fib(10)}")
print(f"fib(20): {fib(20)}")
print(f"fib(5): {fib(5)}")


# EXERCISE 2: Binary Conversion
def to_binary(n):
    """Return the binary representation of a non-negative integer n."""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)


print(f"to_binary(2): {to_binary(2)}")
print(f"to_binary(12): {to_binary(12)}")
print(f"to_binary(0): {to_binary(0)}")
print(f"bin(2): {bin(2)}")
print(f"bin(12): {bin(12)}")
print(f"bin(0): {bin(0)}")


# EXERCISE 3: Data Analysis
import pandas as pd

URL = (
    "https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv"
)
df_bellevue = pd.read_csv(URL)

print("\nBellevue Data Sample:")
print(df_bellevue.head())


def task_i():
    """
    Return a list of all column names, sorted by missing values
    (least missing first, most missing last).
    """
    df = df_bellevue.copy()
    if "gender" in df.columns:
        df["gender"] = (
            df["gender"]
            .str.lower()
            .str.strip()
            .replace(
                {
                    "m": "man",
                    "w": "woman",
                    "?": None,
                    "h": None,
                    "g": None,
                    "": None,
                }
            )
        )
        print("Cleaned Gender Values:", df["gender"].unique())
    missing_values = df.isnull().sum()
    sorted_cols = missing_values.sort_values(ascending=True).index.tolist()
    return sorted_cols


print("\nTask 1:", task_i())


def task_ii():
    """
    Return a DataFrame with 'year' and 'total_admissions'.
    Extracts year from the 'date_in' column.
    """
    df = df_bellevue.copy()
    df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
    if df["date_in"].isnull().any():
        print("There are missing values in the 'date_in' column and converted to NaN.")
    df["year"] = df["date_in"].dt.year
    result = df.groupby("year").size().reset_index(name="total_admissions")
    return result


print("\nTask 2:\n", task_ii())


def task_iii():
    """
    Return a Series with gender as index and average age as values.
    """
    df = df_bellevue.copy()
    df["gender"] = (
        df["gender"]
        .str.lower()
        .str.strip()
        .replace(
            {
                "m": "man",
                "w": "woman",
                "?": None,
                "h": None,
                "g": None,
                "": None,
            }
        )
    )
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    result = df.groupby("gender")["age"].mean()
    return result


print("\nTask 3:\n", task_iii())


def task_4():
    """
    Return a list of the 5 most common professions (most common first).
    """
    df = df_bellevue.copy()
    if "profession" not in df.columns:
        print("No 'profession' column found in dataset.")
        return []
    df["profession"] = df["profession"].astype(str).str.strip().str.lower()
    if df["profession"].isna().any() or (df["profession"] == "").any():
        print("Some 'profession' values are missing or blank.")
    top5 = df["profession"].value_counts().head(5).index.tolist()
    return top5


print("\nTask 4:", task_4())
