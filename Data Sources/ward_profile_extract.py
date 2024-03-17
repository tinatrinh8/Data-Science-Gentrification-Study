
import pandas as pd
from sqlalchemy import create_engine

#connection to PostgreSQL database 
engine = create_engine('postgresql+psycopg2://postgres:Bucnuoa!@localhost:5432/main')
#postgresql+psycopg2://<username>:<password>@<host>:<port>/<database>  with username being default 'postgres'

# WARD DIMENSION
WardDimension = pd.read_csv('WardNameNumbers.csv', encoding='ISO-8859-1', low_memory=False)

# rename columns
WardDimension.rename(columns={'Ward Number': 'Ward_ID'}, inplace=True)
WardDimension.rename(columns={'Ward Name': 'Ward_Name'}, inplace=True)

# change data types
WardDimension['Ward_ID'] = 'Ward ' + WardDimension['Ward_ID'].astype(str)
WardDimension['Ward_Name'] = WardDimension['Ward_Name'].astype(str)

# output final ward dimension
#WardDimension.to_csv('WardDimension.csv', encoding='ISO-8859-1', index=False)

# load dataframe to database
WardDimension.to_sql('WardDimension', engine, if_exists='replace', index=False)

# EDUCATION DIMENSION
education_data2016 = pd.read_csv('WardProfile2016.csv', skiprows=range(833), nrows=16, header=0, encoding='ISO-8859-1', low_memory=False)
education_data2021 = pd.read_csv('WardProfile2021.csv', skiprows=range(978), nrows=17, header=0, encoding='ISO-8859-1', low_memory=False)

# rename 'Education' column to 'Education_Level' before melting
education_data2016.rename(columns={'Education': 'Education_Level'}, inplace=True)
education_data2021.rename(columns={'Education': 'Education_Level'}, inplace=True)

# Filter out rows where 'Education_Level' column is not NA (i.e., not empty)
education_data2016 = education_data2016[education_data2016['Education_Level'].notna()]
education_data2021 = education_data2021[education_data2021['Education_Level'].notna()]

# remove all spaces in education_level column
education_data2016['Education_Level'] = education_data2016['Education_Level'].str.strip()
education_data2021['Education_Level'] = education_data2021['Education_Level'].str.strip()

# Melt the DataFrame to get 'Ward_ID', 'Education_Level', and 'Population' columns
education_data2016 = pd.melt(education_data2016, id_vars=['Education_Level'], var_name='Ward_ID', value_name='Population')
education_data2016['Year'] = 2016
education_data2021 = pd.melt(education_data2021, id_vars=['Education_Level'], var_name='Ward_ID', value_name='Population')
education_data2021['Year'] = 2021

#merge the datasets
EducationDimension = pd.concat([education_data2016, education_data2021], ignore_index=True)

# change data types
EducationDimension['Population'] = EducationDimension['Population'].astype(int)
EducationDimension['Ward_ID'] = EducationDimension['Ward_ID'].astype(str)
EducationDimension['Education_Level'] = EducationDimension['Education_Level'].astype(str)

# output final education dimension
#EducationDimension.to_csv('EducationDimension.csv', encoding='ISO-8859-1', index=False)

# load dataframe to database
EducationDimension.to_sql('EducationDimension', engine, if_exists='replace', index=False)

# AGE DIMENSION
age_data2016 = pd.read_csv('WardProfile2016.csv', skiprows=range(0), nrows=21, header=0, encoding='ISO-8859-1', low_memory=False)
age_data2021 = pd.read_csv('WardProfile2021.csv', skiprows=range(0), nrows=21, header=0, encoding='ISO-8859-1', low_memory=False)

age_data2016.rename(columns={'Population': 'Age_Range'}, inplace=True)
age_data2021.rename(columns={'Population': 'Age_Range'}, inplace=True)

# Filter out rows where 'Age' column is not NA (i.e., not empty)
age_data2016 = age_data2016[age_data2016['Age_Range'].notna()]
age_data2021 = age_data2021[age_data2021['Age_Range'].notna()]

# remove spaces
age_data2016['Age_Range'] = age_data2016['Age_Range'].str.strip()
age_data2021['Age_Range'] = age_data2021['Age_Range'].str.strip()

# Melt the DataFrame to get 'Ward_ID', 'Age', and 'Population' columns
age_data2016 = pd.melt(age_data2016, id_vars=['Age_Range'], var_name='Ward_ID', value_name='Population')
age_data2016['Year'] = 2016
age_data2021 = pd.melt(age_data2021, id_vars=['Age_Range'], var_name='Ward_ID', value_name='Population')
age_data2021['Year'] = 2021

#merge the datasets
AgeDimension = pd.concat([age_data2016, age_data2021], ignore_index=True)

# change data types
AgeDimension['Population'] = AgeDimension['Population'].astype(int)
AgeDimension['Ward_ID'] = AgeDimension['Ward_ID'].astype(str)
AgeDimension['Age_Range'] = AgeDimension['Age_Range'].astype(str)

# output final age dimension
#AgeDimension.to_csv('AgeDimension.csv', encoding='ISO-8859-1', index=False)

# load dataframe to database
AgeDimension.to_sql('AgeDimension', engine, if_exists='replace', index=False)

# EMPLOYMENT DIMENSION
employment_data2016 = pd.read_csv('WardProfile2016.csv', skiprows=range(1163), nrows=12, header=0, encoding='ISO-8859-1', low_memory=False)
employment_data2021 = pd.read_csv('WardProfile2021.csv', skiprows=range(1297), nrows=12, header=0, encoding='ISO-8859-1', low_memory=False)

# Filter out rows where 'Employment' column is not NA (i.e., not empty)
employment_data2016 = employment_data2016[employment_data2016['Employment'].notna()]
employment_data2021 = employment_data2021[employment_data2021['Employment'].notna()]

# Removing the numbers and spaces before each employment type
employment_data2016['Employment'] = employment_data2016['Employment'].str.strip()
employment_data2021['Employment'] = employment_data2021['Employment'].str.strip()
employment_data2016['Employment'] = employment_data2016['Employment'].str.replace(r"^\s*\d+\s+", "", regex=True)
employment_data2021['Employment'] = employment_data2021['Employment'].str.replace(r"^\s*\d+\s+", "", regex=True)

# Melt the DataFrame to get 'Ward_ID', 'Employment', and 'Population' columns
employment_data2016 = pd.melt(employment_data2016, id_vars=['Employment'], var_name='Ward_ID', value_name='Population')
employment_data2016['Year'] = 2016
employment_data2021 = pd.melt(employment_data2021, id_vars=['Employment'], var_name='Ward_ID', value_name='Population')
employment_data2021['Year'] = 2021

#merge the datasets
EmploymentDimension = pd.concat([employment_data2016, employment_data2021], ignore_index=True)

# change data types
EmploymentDimension['Population'] = EmploymentDimension['Population'].astype(int)
EmploymentDimension['Ward_ID'] = EmploymentDimension['Ward_ID'].astype(str)
EmploymentDimension['Employment'] = EmploymentDimension['Employment'].astype(str)


# output final education dimension
#EmploymentDimension.to_csv('EmploymentDimension.csv', encoding='ISO-8859-1', index=False)

# load dataframe to database
EmploymentDimension.to_sql('EmploymentDimension', engine, if_exists='replace', index=False)

# INDUSTRY DIMENSION
industry_data2016 = pd.read_csv('WardProfile2016.csv', skiprows=range(1176), nrows=22, header=0, encoding='ISO-8859-1', low_memory=False)
industry_data2021 = pd.read_csv('WardProfile2021.csv', skiprows=range(1310), nrows=22, header=0, encoding='ISO-8859-1', low_memory=False)

# Filter out rows where 'Industry' column is not NA (i.e., not empty)
industry_data2016 = industry_data2016[industry_data2016['Industry'].notna()]
industry_data2021 = industry_data2021[industry_data2021['Industry'].notna()]

# Removing the numbers and spaces before each industry type
industry_data2016['Industry'] = industry_data2016['Industry'].str.strip()
industry_data2021['Industry'] = industry_data2021['Industry'].str.strip()
industry_data2016['Industry'] = industry_data2016['Industry'].str.replace(r"^\s*\d+(-\d+)?\s+", "", regex=True)
industry_data2021['Industry'] = industry_data2021['Industry'].str.replace(r"^\s*\d+(-\d+)?\s+", "", regex=True)

# Melt the DataFrame to get 'Ward_ID', 'Industry', and 'Population' columns
industry_data2016 = pd.melt(industry_data2016, id_vars=['Industry'], var_name='Ward_ID', value_name='Population')
industry_data2016['Year'] = 2016
industry_data2021 = pd.melt(industry_data2021, id_vars=['Industry'], var_name='Ward_ID', value_name='Population')
industry_data2021['Year'] = 2021

#merge the datasets
IndustryDimension = pd.concat([industry_data2016, industry_data2021], ignore_index=True)

# change data types
IndustryDimension['Population'] = IndustryDimension['Population'].astype(int)
IndustryDimension['Ward_ID'] = IndustryDimension['Ward_ID'].astype(str)
IndustryDimension['Industry'] = IndustryDimension['Industry'].astype(str)

# output final education dimension
#IndustryDimension.to_csv('IndustryDimension.csv', encoding='ISO-8859-1', index=False)

# load dataframe to database
IndustryDimension.to_sql('IndustryDimension', engine, if_exists='replace', index=False)

# INCOME DIMENSION
income_data2016 = pd.read_csv('WardProfile2016.csv', skiprows=range(1252), nrows=17, header=0, encoding='ISO-8859-1', low_memory=False)
income_data2021 = pd.read_csv('WardProfile2021.csv', skiprows=range(1389), nrows=17, header=0, encoding='ISO-8859-1', low_memory=False)

# Filter out rows where 'Income' column is not NA (i.e., not empty)
income_data2016 = income_data2016[income_data2016['Income'].notna()]
income_data2021 = income_data2021[income_data2021['Income'].notna()]

# change value of one of income ranges
income_data2016.loc[income_data2016['Income'].str.contains('Total - Total income groups'), 'Income'] = 'Total Income Groups'
income_data2021.loc[income_data2021['Income'].str.contains('Total - Total Income groups'), 'Income'] = 'Total Income Groups'

# Removing the spaces before each income
income_data2016['Income'] = income_data2016['Income'].str.strip()
income_data2021['Income'] = income_data2021['Income'].str.strip()

# Melt the DataFrame to get 'Ward_ID', 'Income', and 'Population' columns
income_data2016['Year'] = 2016
income_data2021['Year'] = 2021
income_data2016 = pd.melt(income_data2016, id_vars=['Income', 'Year'], var_name='Ward_ID', value_name='Population')
income_data2021 = pd.melt(income_data2021, id_vars=['Income', 'Year'], var_name='Ward_ID', value_name='Population')
columns_order = [col for col in income_data2016.columns if col != 'Year'] + ['Year']
income_data2016 = income_data2016[columns_order]
income_data2021 = income_data2021[columns_order]

#merge the datasets
IncomeDimension = pd.concat([income_data2016, income_data2021], ignore_index=True)

# change data types
IncomeDimension['Population'] = IncomeDimension['Population'].astype(int)
IncomeDimension['Ward_ID'] = IncomeDimension['Ward_ID'].astype(str)
IncomeDimension['Income'] = IncomeDimension['Income'].astype(str)

# output final income dimension
#IncomeDimension.to_csv('IncomeDimension.csv', encoding='ISO-8859-1', index=False)

# load dataframe to database
IncomeDimension.to_sql('IncomeDimension', engine, if_exists='replace', index=False)

# ETHNOCULTURAL DIMENSION
ethnicity_data2016 = pd.read_csv('WardProfile2016.csv', skiprows=range(851), nrows=280, header=0, encoding='ISO-8859-1', low_memory=False)
ethnicity_data2021 = pd.read_csv('WardProfile2021.csv', skiprows=range(1013), nrows=252, header=0, encoding='ISO-8859-1', low_memory=False)

# Filter out rows where 'Ethnocultural' column is not NA (i.e., not empty)
ethnicity_data2016 = ethnicity_data2016[ethnicity_data2016['Ethnoculture'].notna()]
ethnicity_data2021 = ethnicity_data2021[ethnicity_data2021['Ethnoculture'].notna()]

# change value of one of income ranges
ethnicity_data2016.loc[ethnicity_data2016['Ethnoculture'].str.contains('Total - Ethnic origin'), 'Ethnoculture'] = 'Total Ethnic Origin'
ethnicity_data2021.loc[ethnicity_data2021['Ethnoculture'].str.contains('Total - Ethnic origin'), 'Ethnoculture'] = 'Total Ethnic Origin'

# Removing the spaces before each ethnicity
ethnicity_data2016['Ethnoculture'] = ethnicity_data2016['Ethnoculture'].str.strip()
ethnicity_data2021['Ethnoculture'] = ethnicity_data2021['Ethnoculture'].str.strip()

# Melt the DataFrame to get 'Ward_ID', 'Ethnocultural', and 'Population' columns
ethnicity_data2016['Year'] = 2016
ethnicity_data2021['Year'] = 2021
ethnicity_data2016 = pd.melt(ethnicity_data2016, id_vars=['Ethnoculture', 'Year'], var_name='Ward_ID', value_name='Population')
ethnicity_data2021 = pd.melt(ethnicity_data2021, id_vars=['Ethnoculture', 'Year'], var_name='Ward_ID', value_name='Population')
columns_order = [col for col in ethnicity_data2016.columns if col != 'Year'] + ['Year']
ethnicity_data2016 = ethnicity_data2016[columns_order]
ethnicity_data2021 = ethnicity_data2021[columns_order]

#merge the datasets
EthnoculturalDimension = pd.concat([ethnicity_data2016, ethnicity_data2021], ignore_index=True)

# change data types
EthnoculturalDimension['Population'] = EthnoculturalDimension['Population'].astype(int)
EthnoculturalDimension['Ward_ID'] = EthnoculturalDimension['Ward_ID'].astype(str)
EthnoculturalDimension['Ethnoculture'] = EthnoculturalDimension['Ethnoculture'].astype(str)

# output final ethnicity dimension
#EthnoculturalDimension.to_csv('EthnoculturalDimension.csv', encoding='ISO-8859-1', index=False)
  
# load dataframe to database
EthnoculturalDimension.to_sql('EthnoculturalDimension', engine, if_exists='replace', index=False)

# HOUSEHOLD DIMENSION    
household_data2016 = pd.read_csv('WardProfile2016.csv', skiprows=range(98), nrows=9, header=0, encoding='ISO-8859-1', low_memory=False)
household_data2021 = pd.read_csv('WardProfile2021.csv', skiprows=range(108), nrows=9, header=0, encoding='ISO-8859-1', low_memory=False)

# Filter out rows where 'Household' column is not NA (i.e., not empty)
household_data2016 = household_data2016[household_data2016['Household'].notna()]
household_data2021 = household_data2021[household_data2021['Household'].notna()]

# change value of one of income ranges
household_data2016.loc[household_data2016['Household'].str.contains('Total - Private households by household'), 'Household'] = 'Total Household'
household_data2021.loc[household_data2021['Household'].str.contains('Total - Private households by household'), 'Household'] = 'Total Household'


# Removing the spaces before each household type
household_data2016['Household'] = household_data2016['Household'].str.strip()
household_data2021['Household'] = household_data2021['Household'].str.strip()

# Melt the DataFrame to get 'Ward_ID', 'Household', and 'Population' columns
household_data2016['Year'] = 2016
household_data2021['Year'] = 2021
household_data2016 = pd.melt(household_data2016, id_vars=['Household', 'Year'], var_name='Ward_ID', value_name='Population')
household_data2021 = pd.melt(household_data2021, id_vars=['Household', 'Year'], var_name='Ward_ID', value_name='Population')
columns_order = [col for col in household_data2016.columns if col != 'Year'] + ['Year']
household_data2016 = household_data2016[columns_order]
household_data2021 = household_data2021[columns_order]

# Merge the datasets
HouseholdDimension = pd.concat([household_data2016, household_data2021], ignore_index=True)


# change data types
HouseholdDimension['Ward_ID'] = HouseholdDimension['Ward_ID'].astype(str)
HouseholdDimension['Household'] = HouseholdDimension['Household'].astype(str)

# rename column
HouseholdDimension.rename(columns={'Household': 'Household_Description'}, inplace=True)

# output final ethnicity dimension
#HouseholdDimension.to_csv('HouseholdDimension.csv', encoding='ISO-8859-1', index=False)

# load dataframe to database
HouseholdDimension.to_sql('HouseholdDimension', engine, if_exists='replace', index=False)

# Close the engine connection when done
engine.dispose()