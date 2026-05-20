# vendor-sales-performance.
An end-to-end data pipeline and SQL analysis project evaluating vendor sales performance and delivery trends.

### Day 1: Establishing the Data Foundation 🧱

**Objective:** Ingest large raw CSV datasets into a structured relational database to enable efficient SQL querying and analysis down the line.

**What I did today:**
* Wrote a production-ready Python script to automate the extraction and loading of vendor inventory, sales, and purchase data.
* Set up a local **SQLite** database using **SQLAlchemy**.
* Implemented a data chunking mechanism using **Pandas** to bypass memory limitations when reading massive files.
* Built dynamic logic to replace tables on the first chunk and append subsequent data chunks seamlessly.
