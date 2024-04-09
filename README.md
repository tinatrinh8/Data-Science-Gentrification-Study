# CSI4142: Toronto Ward Gentrification Study 🥭🌠🕰️🍄🎨

## 🪄 Phase 2: Physical Design and Data Staging 🪄

### 🚴🏻‍♀️ Overview
This project is a part of the coursework for CSI4142 at the University of Ottawa. In our research, our focus is on analyzing gentrification across different Toronto neighborhoods by examining contributing factors and finding correlations. The study involves analyzing data related to Age, Education, Demolition, Ward, Income, Household, Building Permit, Ethnocultural, Employment, Shelter, and Industry to determine their relationship with high and low gentrification levels.

### 🥨 Team Members
- Serena Iyoha - 300187757
- Shannon Noah - 300163898
- Tina Trinh - 300175427

### 🎋 Data Staging Steps (ETL Process)
- **Extraction**: Data extracted from CSVs.
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

### ⛸️ PostgreSQL Installation Instructions
**Windows:**
- Navigate to the official [PostgreSQL download page](https://www.postgresql.org/download/windows/).
- Select the Windows installer for PostgreSQL.
- Execute the downloaded installer and follow the prompts to install PostgreSQL and pgAdmin.

**macOS:**
- Open the terminal.
- Run `brew install postgresql` if you have Homebrew installed, or download the installer from the official [PostgreSQL download page for macOS](https://www.postgresql.org/download/macosx/).

### 🥑 Restoring the Database
- Launch pgAdmin, included with your PostgreSQL installation.
- In the sidebar, find "Servers" and expand it to reveal "PostgreSQL 16".
- Connect to the server using your password when prompted.
- Right-click "Databases" and select "Create" > "Database...".
- Name the database "main" and save it.
- Right-click on the new "main" database and select "Restore".
- In the dialog, use the file browser to select the `database.backup` file from the project folder.
- Confirm the selection and initiate the restoration process by clicking "Restore".

### 🧥 Geospatial Analysis Preparation
- Sign up at [Mapbox](https://www.mapbox.com/) and generate an API key.
- In the `mapbox_key.json` file within the project, replace "YOUR API KEY" with the key you obtained.
- Open the geospatial analysis Jupyter Notebook.
- Execute all cells in the notebook to run the analysis.

**Note:** Ensure to update any placeholder text with actual data and file paths specific to your setup.
