from pathlib import Path
from urllib.request import urlretrieve

BASE_URL = "https://d37ci6vzurychx.cloudfront.net"
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

FILES = {
    "yellow_tripdata_2025-10.parquet": f"{BASE_URL}/trip-data/yellow_tripdata_2025-10.parquet",
    "taxi_zone_lookup.csv": f"{BASE_URL}/misc/taxi_zone_lookup.csv",
}

for name, url in FILES.items():
    target = RAW_DIR / name
    if target.exists():
        print(f"Already have {name}")
        continue
    print(f"Downloading {name} ...")
    urlretrieve(url, target)
    print("Done")