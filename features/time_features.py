def time_features(df):
    df = df.copy()

    df["hour"] = (df["Time"] / 3600) % 24
    df["is_night"] = df["hour"].between(0, 5).astype(int)

    return df