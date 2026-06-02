import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df["provider_id"] = df["provider_id"].fillna("MISSING_PROVIDER")
    df["claim_date"] = pd.to_datetime(df["claim_date"])
    return df

def detect_anomalies(df):
    threshold = df["claim_amount"].mean() + 3 * df["claim_amount"].std()
    anomalies = df[df["claim_amount"] > threshold].copy()
    anomalies["anomaly_reason"] = "High claim amount"
    return anomalies

def provider_kpis(df):
    return (
        df.groupby("provider_id")
        .agg(
            total_claims=("claim_id", "count"),
            total_claim_amount=("claim_amount", "sum"),
            average_claim_amount=("claim_amount", "mean"),
            rejected_claims=("submission_status", lambda x: (x == "Rejected").sum()),
            approved_claims=("submission_status", lambda x: (x == "Approved").sum())
        )
        .reset_index()
        .sort_values("total_claim_amount", ascending=False)
    )

def main():
    df = load_data("data/sample_claims.csv")
    df = clean_data(df)

    anomalies = detect_anomalies(df)
    kpis = provider_kpis(df)

    df.to_csv("cleaned_claims.csv", index=False)
    anomalies.to_csv("anomaly_claims.csv", index=False)
    kpis.to_csv("provider_kpi_summary.csv", index=False)

    print("Healthcare Claims Analytics Completed")
    print(f"Total Claims: {len(df)}")
    print(f"Missing Provider Claims: {(df['provider_id'] == 'MISSING_PROVIDER').sum()}")
    print(f"Anomalies Detected: {len(anomalies)}")
    print(f"Total Claim Amount: ${df['claim_amount'].sum():,.2f}")

if __name__ == "__main__":
    main()
