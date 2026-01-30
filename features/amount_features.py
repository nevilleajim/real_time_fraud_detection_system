import pandas as pd

def amount_deviation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates amount deviation features per user.
    """
    df = df.copy()

    user_stats = df.groupby("user_id")["Amount"].agg(
        user_mean_amount="mean",
        user_std_amount="std"
    )

    df = df.join(user_stats, on="user_id")

    df["amount_zscore"] = (
        (df["Amount"] - df["user_mean_amount"]) / (df["user_std_amount"] + 1e-6)
    )

    return df