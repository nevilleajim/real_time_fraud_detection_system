def rolling_transaction_count(df, window=10):
    df = df.copy()

    df["tx_count_rolling"] = (
        df.groupby("user_id")["Amount"]
        .rolling(window)
        .count()
        .reset_index(level=0, drop=True)
    )

    df["tx_count_rolling"].fillna(1)

    return df