# Toronto Ward Gentrification Study 🥭🌠🕰️🍄🎨

## 🪄 Phase 2: Physical Design and Data Staging 🪄

### 🚴🏻‍♀️ Overview
In our research, our focus is on analyzing gentrification across different Toronto neighborhoods by examining contributing factors and finding correlations. The study involves analyzing data related to Age, Education, Demolition, Ward, Income, Household, Building Permit, Ethnocultural, Employment, Shelter, and Industry to determine their relationship with high and low gentrification levels.

### 🥨 Team Members
- Serena Iyoha
- Shannon Noah
- Tina Trinh 

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

## 🧝🏻‍♀️ Phase 4: Data Mining 🧝🏻‍♀️

### 🍨 Overview
In Phase 4, we apply data mining techniques to analyze gentrification trends across Toronto neighborhoods. Our focus is to draw correlations from demographic and urban data variables. This is found in 'Phase4' file.

### 🛤️  Data Summarization and Preprocessing
- Visualizations (scatter plots, boxplots, histograms) provide a preliminary understanding of our data.
- Preprocessing tasks include imputation for missing values, one-hot encoding for categorical variables, normalization of numerical attributes, and diligent feature selection to streamline our dataset.

### 🛁  Outlier Detection (Bonus)
- Employing the one-class SVM algorithm, we pinpoint global outliers and interpret their significance within our dataset.
