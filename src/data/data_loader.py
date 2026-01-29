"""
Data loading utilities for Statcast data. 
"""
import pandas as pd 
from pybaseball import statcast 
from pathlib import Path 
from typing import Optional 
from tqdm import tqdm 
from src.utils.config import DATA_RAW # recall our utils 

def load_statcast_data(
        start_date: str ,
        end_date: str, 
        cache_path: Optional[Path] = None, 
        ) -> pd.DataFrame:
    """
    Loads Statcast pitch data for a given date range in a cleaned up and repeatable way. 
    
    Parameters
    ----------
    start_date: str 
        Start Date in YYYY-MM-DD format 
    end_date: str 
        End Date in YYYY-MM-DD format 
    cache_path: Path, optional 
        Path to cache the data. If exists, loads from the cache. 

    Returns 
    ----------
    pd.DataFrame 
        Statcast pitch data 
    """
    if cache_path is None: 
        cache_path = DATA_RAW / f"statcast_{start_date}_{end_date}.parquet" # FAST 

    # loading from the cache if it exists as mentioned earlier 
    if cache_path.exists():
        print(f"Loading data from cache: {cache_path}")
        return pd.read_parquet(cache_path)

    # downloading from statcast 
    print(f"Downloading Statcast data from {start_date} to {end_date}...here comes the pitch...")
    data = statcast(start_dt=start_date , end_dt=end_date)

    if data is None or len(data) == 0:
        raise ValueError("No data returned from Statcast")
    
    print(f"Downloaded {len(data):,} pitches. The pitcher winds and deals!") # fun way to share this

    # caching for future use 
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_parquet(cache_path , index=False)
    print(f"Cached data to: {cache_path}")

    return data 

# now expanding this and doing this for multiple seasons
def load_multiple_seasons(
        start_year: int, 
        end_year: int, 
        cache: bool = True,
        ) -> pd.DataFrame:
    """
    Loads multiple seasons of Statcast data. 

    Parameters
    ----------
    start_year: int 
        Starting year (inclusive)
    end_year: int 
        Ending year (inclusive)
    cache: bool 
        Whether to use and/or create cache files 

    Returns 
    ----------
    pd.DataFrame
        Has our combined, multi-season Statcast data 
    """
    all_data = []
    
    for year in tqdm(range(start_year, end_year + 1), desc="Loading seasons"):
        start_date = f"{year}-03-01"
        end_date = f"{year}-11-30" # baseball season 

        cache_path = DATA_RAW / f"statcast_{year}.parquet" if cache else None # checking if we cached data 
        data = load_statcast_data(start_date , end_date , cache_path) # using our own work 
        all_data.append(data)

    combined = pd.concat(all_data , ignore_index=True) # can probably just stack on top of each other 
    print(f"\nTotal pitches across all seasons: {len(combined):,}\n That's a lot of mud!")

    return combined





