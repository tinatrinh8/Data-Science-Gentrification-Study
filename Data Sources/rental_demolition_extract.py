import pandas as pd
from sqlalchemy import create_engine, text

#connection to PostgreSQL database
engine = create_engine('postgresql+psycopg2://postgres:Bucnuoa!@localhost:5432/main')

# EXTRACTING DEMOLITION RENTAL UNITS DATA
demolition = pd.read_csv('Rental Demolition and Replacement.csv',low_memory=False)

# changing date types
demolition['City Council Approval Date'] = pd.to_datetime(demolition['City Council Approval Date'])

# changing string types
demolition['IBMS Address'] = demolition['IBMS Address'].astype(str)
demolition['Address of Existing Rental Building'] = demolition['Address of Existing Rental Building'].astype(str)
demolition['RH File Number'] = demolition['RH File Number'].astype(str)
demolition['Type'] = demolition['Type'].astype(str)

# changing int types
demolition['Total Rental Homes for Demolition'] = pd.to_numeric(demolition['Total Rental Homes for Demolition'], errors='coerce').astype('Int64')
demolition['Affordable Rental Homes for Demolition'] = pd.to_numeric(demolition['Affordable Rental Homes for Demolition'], errors='coerce').astype('Int64')
demolition['Mid-Range Rental Homes for Demolition'] = pd.to_numeric(demolition['Mid-Range Rental Homes for Demolition'], errors='coerce').astype('Int64')
demolition['High-End Rental Homes for Demolition'] = pd.to_numeric(demolition['High-End Rental Homes for Demolition'], errors='coerce').astype('Int64')
demolition['Total Rental Homes Replaced'] = pd.to_numeric(demolition['Total Rental Homes Replaced'], errors='coerce').astype('Int64')
demolition['Affordable Rental Homes Replaced'] = pd.to_numeric(demolition['Affordable Rental Homes Replaced'], errors='coerce').astype('Int64')
demolition['Mid-Range Rental Homes Replaced'] = pd.to_numeric(demolition['Mid-Range Rental Homes Replaced'], errors='coerce').astype('Int64')
demolition['High-End Rental Homes Replaced'] = pd.to_numeric(demolition['High-End Rental Homes Replaced'], errors='coerce').astype('Int64')

# dropping columns
demolition.drop(['_id', 'Link to Staff Report', '(Post 2018) Ward', 'Link to Staff Report'], axis=1, inplace=True)

# output final education dimension
#demolition.to_csv('DemolitionDimension.csv', encoding='ISO-8859-1', index=False)

# load dataframe to database
demolition.to_sql('DemolitionDimension', engine, if_exists='replace', index=False)