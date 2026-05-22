# vendor-sales-performance.
An end-to-end data pipeline and SQL analysis project evaluating vendor sales performance and delivery trends.

### Day 1: Establishing the Data Foundation 🧱

**Objective:** Ingest large raw CSV datasets into a structured relational database to enable efficient SQL querying and analysis down the line.

**What I did today:**
* Wrote a production-ready Python script to automate the extraction and loading of vendor inventory, sales, and purchase data.
* Set up a local **SQLite** database using **SQLAlchemy**.
* Implemented a data chunking mechanism using **Pandas** to bypass memory limitations when reading massive files.
* Built dynamic logic to replace tables on the first chunk and append subsequent data chunks seamlessly.

## Day 2: Advanced SQL Joins & Data Consolidation 🔗

*Objective:* Consolidate fragmented inventory, purchase, sales, and freight data into a single master summary table to prepare for analysis and visualization.

*What I did today:*
- Queried and explored raw data from SQLite tables (`purchases`, `sales`, `vendor_invoice`, etc.) using Pandas.
- Filtered and aggregated purchase and sales data for specific vendors to understand table structures.
- Wrote a complex SQL query using Common Table Expressions (CTEs) and `LEFT JOIN`s to merge purchase metrics, sales metrics, and freight costs.
- Generated a master `vendor_sales_summary` table containing total purchase quantities/dollars, total sales quantities/dollars, and freight costs per vendor and brand.
- Saved the consolidated master table back into the `inventory.db` SQLite database for future downstream analysis.

## Day 3: Feature Engineering & Database Updates ⚙️

*Objective:* Transform raw financial data into actionable business metrics and permanently update the project's SQLite database.

*What I did today:*
- Engineered key retail performance features (`GrossProfit`, `ProfitMargin`, `StockTurnover`, and `SalestoPurchaseRatio`) using Pandas.
- Exported the enriched dataframe back into the local `inventory.db` SQLite database.
- Utilized the Pandas `.to_sql()` method with `if_exists='replace'` to safely overwrite the legacy `vendor_sales_summary` table without data loss.
- Managed and debugged Jupyter Notebook cell execution states to prevent data overwriting and resolved SQLite `OperationalError` constraints.
