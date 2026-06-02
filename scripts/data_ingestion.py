from pathlib import Path
import pandas as pd

try:
    DATA_DIR = Path("./data/raw")

    files = sorted(DATA_DIR.glob("*.csv"))

    print("=" * 80)
    print("DATA INGESTION REPORT")
    print("=" * 80)

    for file in files:

        print(f"\n\nFILE: {file.name}")
        print("-" * 80)

        try:

            df = pd.read_csv(file)

            print("\nShape:")
            print(df.shape)

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

        except Exception as e:

            print(f"ERROR READING {file.name}")
            print(e)

    print("\n\nDone.")

except Exception as e:
    print("Error occured while executing the file")
    print(e)
    