# CSI4142: Toronto Ward Gentrification Study 🥭🌠🕰️🍄🎨

## 🪄 Phase 2: Physical Design and Data Staging 🪄

### 🚴🏻‍♀️ Overview
This project is a part of the coursework for CSI4142 at the University of Ottawa. In our research, our focus is on analyzing gentrification across different Toronto neighborhoods by examining contributing factors and finding correlations. The study involves analyzing data related to Age, Education, Ward, Income, Household, Building Permit, Ethnocultural, Employment, Shelter, and Industry to determine their relationship with high and low gentrification levels.

### 🥨 Team Members
- Serena Iyoha - 300187757
- Shannon Noah - 300163898
- Tina Trinh - 300175427

### 🎋 Data Staging Steps (ETL Process)
- **Extraction**: Data extracted in formats like CSV, XML, or JSON.
- **Transformation**: Includes data cleaning, conversion, integration, discretization, and feature engineering.
- **Loading**: Involves generating surrogate keys and loading the integrated/final dataset into a data mart.

### 🐌 Prerequisites
- Ensure Python 3.6 or newer is installed.
- PostgreSQL must be installed for database management.
- For geospatial analysis, a Mapbox API key is required.

### 👒 Required Libraries
Install the following libraries using pip:

```bash
pip install pandas sqlalchemy requests Shapely json folium geopandas
```

### 📙 PostgreSQL Installation
- **Windows**: Download and install from the [official PostgreSQL download page](https://www.postgresql.org/download/windows/).
- **macOS**: Use Homebrew with `brew install postgresql`, or download from the [official page](https://www.postgresql.org/download/macosx/).

### 🛩️ Database Setup
1. Launch pgAdmin and connect to PostgreSQL.
2. Create a new database named "main".
3. Restore the database using the `database.backup` file from the project folder.

### 🌍 Geospatial Analysis Setup
1. Sign up on Mapbox and generate a personal API key.
2. Replace "YOUR API KEY" in the `mapbox_key.json` file with your generated API key.

### 🥃 Project Structure
```plaintext
.
├── Data (CSV,JSON)         # Raw data and processed data
├── Data Sources               
│   ├── WardProfile.ipynb   # Jupyter notebooks for analysis
│   ├── BuildingPermit.ipynb
│   ├── geospatial_analysis.ipynb
│   └── geocoding.py        # Source code
├── mapbox_key.json         # Mapbox API key configuration
├── queries       
│   └── database.backup     # Database backup file
└── README.md
```

