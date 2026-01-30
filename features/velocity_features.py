def transaction_velocity(df):
    df = df.copy()

    df["prev_time"] = df.groupby("user_id")["Time"].shift(1)
    df["time_since_last_tx"] = df["Time"] - df["prev_time"]
    df["time_since_last_tx"].fillna(999999)

    return df