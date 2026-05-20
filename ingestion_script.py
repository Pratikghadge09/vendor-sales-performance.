import pandas as pd
import os
from sqlalchemy import create_engine
import logging

# Setup Logging
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

os.makedirs("db", exist_ok=True)
engine = create_engine("sqlite:///db/inventory.db")

# MODIFIED: Added 'mode' parameter so we can switch between 'replace' and 'append'
def ingest_db(df, table_name, engine, mode):
    try:
        df.to_sql(table_name, con=engine, if_exists=mode, index=False, chunksize=1000)
        logging.info(f"Successfully ingested a chunk into {table_name} (Mode: {mode})")
    except Exception as e:
        logging.error(f"Error ingesting chunk into {table_name}: {e}")
        raise e

def load_raw_data():
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            file_path = os.path.join('data', file)
            table_name = file.replace('.csv', '')
            print(f"Processing: {file}")
            
            # CRITICAL FIX: Read the CSV in chunks (e.g., 50,000 rows at a time)
            # This prevents the MemoryError during the read phase.
            csv_reader = pd.read_csv(file_path, chunksize=50000)
            
            for i, chunk in enumerate(csv_reader):
                # Logic: 'replace' the table only for the very first chunk.
                # 'append' for all subsequent chunks.
                if i == 0:
                    mode = 'replace'
                else:
                    mode = 'append'
                
                print(f"  -> Ingesting batch {i+1} with mode '{mode}'...")
                ingest_db(chunk, table_name, engine, mode)
                
            print(f"Completed: {file}")

# Run the ingestion
if __name__ == "__main__":
    load_raw_data()
