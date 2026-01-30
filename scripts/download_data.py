---
"""
Script to download statcast data. 
"""

import argparse 
from src.data.data_loader import load_multiple_seasons 
from src.utils.config import DATA_RAW

def main():
    """
    Downloads statcast data for given or specified years. 
    """
    parser = argparse.ArgumentParser(description="Download Statcast data")
    parser.add_argument(
            "--start-year",
            type=int,
            default=2024,
            help="Starting year (default: 2024)",
            )
    parser.add_argument(
            "--end-year",
            type=int,
            default=2025,
            help="Ending year (default: 2025)",
            )
    args = parser.parse_args()

    print(f"Downloading Statcast data for {args.start_year}-{args.end_year}")
    data = load_multiple_seasons(args.start_year, args.end_year)

    # saving the combined dataset 
    output_path = (
            DATA_RAW / f"statcast_{args.start_year}_{args.end_year}_combined.parquet"
            )
    data.to_parquet(output_path , index=False)
    print(f"\nSaved combined dataset to: {output_path}")
    print(f"Shape: {data.shape}")
    print(f"Columns: {list(data.columns[:10])}...")

# adding the standard to catch edge cases perhaps in the future 
if __name__ == "__main__":
    main()

