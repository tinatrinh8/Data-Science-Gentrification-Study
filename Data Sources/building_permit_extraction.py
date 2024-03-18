import pandas as pd
from sqlalchemy import create_engine, text

#connection to PostgreSQL database
engine = create_engine('postgresql+psycopg2://postgres:Bucnuoa!@localhost:5432/main')

# EXTRACTING BUILDING PERMITS
buildingPermits = pd.read_csv('clearedpermits2016.csv',low_memory=False)
buildingPermitsActive = pd.read_csv('building-permits-active-permits.csv', low_memory=False)
buildingPermits2017 = pd.read_csv('Cleared Building Permits since 2017.csv', low_memory=False)


#standardizing dataframes to prepare for merge
buildingPermitsActive.drop(['_id', 'REVISION_NUM'], axis=1, inplace=True)
buildingPermits.drop(['REVISION_NUM'], axis=1, inplace=True)
buildingPermits2017.drop(['_id', 'REVISION_NUM'], axis=1, inplace=True)

buildingPermitsActive['COMPLETED_DATE'] = pd.to_datetime(buildingPermitsActive['COMPLETED_DATE'])
buildingPermits['COMPLETED_DATE'] = pd.to_datetime(buildingPermits['COMPLETED_DATE'])
buildingPermits2017['COMPLETED_DATE'] = pd.to_datetime(buildingPermits2017['COMPLETED_DATE'])

#merge the datasets
combined_buildingPermits = pd.concat([buildingPermits, buildingPermitsActive, buildingPermits2017], ignore_index=True)

#dropping columns that are not needed
columns_to_drop = ['CURRENT_USE', 'PROPOSED_USE', 'DWELLING_UNITS_CREATED', 'DWELLING_UNITS_LOST']
start_col = 'ASSEMBLY'
end_col = 'BUILDER_NAME'

start_col_index = combined_buildingPermits.columns.get_loc(start_col)
end_col_index = combined_buildingPermits.columns.get_loc(end_col) + 1  # +1 to include 'BUILDER_NAME'

# extend the list with the range of columns
columns_to_drop.extend(combined_buildingPermits.columns[start_col_index:end_col_index])

# drop the columns
combined_buildingPermits.drop(columns=columns_to_drop, axis=1, inplace=True)


statuses_to_remove = [
    "Pending Cancellation",
    "Application Withdrawn",
    "Superseded",
    "Refused",
    "Abandoned",
    "Not Accepted",
    "VIOLATION"
]

combined_buildingPermits = combined_buildingPermits[~combined_buildingPermits['STATUS'].isin(statuses_to_remove)]

# dropping STRUCTURE_TYPES not useful to analysis
#print("STRUCTURE TYPES:")
#unique_structure_types = combined_buildingPermits['STRUCTURE_TYPE'].unique()

#print("WORK TYPES:")
#unique_work_types = combined_buildingPermits['WORK'].unique()

# STRUCTURE TYPE
print("number of rows:", len(combined_buildingPermits))
not_included = [
    'Office', 'SFD: P/D/F/E/R Drains', 'Industrial Warehouse/Hazardous Building', 
    'Electromagnetic Locks', 'HVAC Alt. add on Sys. or Ductwork Alt.', 'Nursing Home Facility',
    'Home for the Aged', 'Retaining Wall', 'SFD Garages', 'Piping(all other bldgs):Outside Water..',
    'P/D/F/E/R Drains: all other buildings', 'Parking Garage Repairs (all other)', 'Grandstand',
    'Residential Porches', 'Residential Decks', 'Repair Garage', 'Converted House', 'Industrial - Shell',
    'Laundromat', 'Third Party', 'Storage Room', 'Convent/Monastery', 'Police Station with Detention',
    'Manufacturing - MMPF', 'Undertaking Premises',
    'Self-Service Storage Building', 'Triplex/Semi-Detached', 'Courtroom', 'Distillery', 
    'Dry Cleaning/Laundry Plant', 'Printing Plant', 'Dry Cleaning Depot',
    'Police Station with No Detention', 'Live/Work Unit', 'Unknown', 'Group D & E', 'SFD Access. Structures',
    'Fire Alarms', 'Standpipes', 'Piping(SF) Water Serv., Sanitary/Storm', 'Fireplaces',
    'HVAC Alt. Boiler/Furn Rplmt. or A/C', 'Exterior Storage Tank', 'Canopy w/o enclosure', 'Sprinklers',
    'Underpinning', 'Spray Painting Operation', 'Group F (< 230 m2)', 'Piping(SF):Repair/Rplmt/Add. Pool Drain',
    'HVAC: Special Ventilation System', 'Basements - Finishing - in Dwellings/TH', 'Mixed Comm/Inst./Res',
    'SFD/TH HVAC', 'Balcony Repairs', 'Repairs/Re-cladding Walls, Re-roofing', 'Temporary Buildings',
    'Trailers', 'Parking Garage Repairs (slab)', 'Sales Pavilions', 'Mixed Industrial Use',
    'SFD/TH Heat. Vent. only', 'Commercial/Institutional Use', 'Industrial/Institutional Use', 'Tent',
    'Mixed Assembly Use', 'Window Replacements (except SFD)', 'Communication Tower', 'SFD/TH Boiler/Furn. Replac.',
    'Residential Carports', 'Group F (> 230m2)', 'Portable Classroom',
    'Re-roofing with structural work', 'Multiple-Use Building', 'Mixed Institutional', 'Fire Doors Retrofit', 'Piping(all other bldgs):Inside San/Storm', 'Exhibition Hall(With Sales)', 'Exhibition Hall(Without Sales)', 'Mixed Inst/Res', 'Other School',
    'House', 'Mixed Comm/Inst/Ind/Res', 'Air Supported Stuctures', 'Home Office', 'Mixed Ind/Comm/Res',
    'Industrial Chemical Plant', 'Municipal Shelter', 'Penthouse/Mechanical Room', 'Lecture Hall', 'Subdivision', 'Public Health', 'ZR - Licensing LPR Notice',
    'HAP Folder', "ZR - Examiner's Notice", 'Tree Declaration Form', 'Municipal Road Damage Deposit Form',
    'Demolition Permit Application Checklist',
    'Parks Levy Appraisal Request', 'Registration and Discharge of Unsafe Order', 'ZR Folder - Planning Source',
    'MGO Memo To', 'Search Titles', 'HP Property DM Folder', 'Sump Pump Program', 'Supermarket',
    'Laneway / Rear Yard Suite', 'Toronto Fire Notifications', 'Laneway / Rear Yard Suites',
    'Television Studio(with audience)', 'HVAC for other Group C', 'Backflow Prevention Devices',
    'Manholes, Catch Basin, Interceptors, Smp', 'SFD/TH A/C Unit Addition', 'Tent (permits for certified)',
    'Balcony Guards'
]

combined_buildingPermits = combined_buildingPermits[~combined_buildingPermits['STRUCTURE_TYPE'].isin(not_included)]

no_work_types = [
    'Install/Alter Plumbing - only',
    'Partial Permit - Shoring',
    'Install/Alter HVAC - only',
    'Building Permit Related(PS)',
    'Other Proposal',
    'Fixtures/Roof Drains: Other',
    'Multiple Projects',
    'Fixtures/Roof Drains: SFD',
    'Communication Tower',
    'Building Permit Related(MS)',
    'Partial Permit - Foundation',
    'Electromagnetic Locks',
    'Alter: Add on /Ductwork',
    'Other(BA)',
    'HVAC: Parking Garages',
    'Canopy',
    'Other(SR)',
    'Fire Damage',
    'Walk-Out Stair',
    'HVAC: Groups A & B',
    'Piping: SFD/Semi',
    'Fire Alarm',
    'Air Conditioning: SFD/Semi/TH',
    'Garage Repair/Reconstruction',
    'Piping: Other Buildings',
    'Sprinklers',
    'Manholes/Catch Basins/Sumps/Interceptors',
    'Underpinning',
    'HVAC: Groups D & E',
    'Partial Permit - Structural Framing',
    'Certified Tents',
    'Other(DS)',
    'Building Permit Related (DR)',
    'Heat/Ventilation: SFD/Semi/TH',
    'Canopy w/o Enclosure',
    'Sales Pavilions',
    'Interior Demolition',
    'Site Service',
    'Septic System: Sewage System',
    'Other(PS)',
    'Boiler/Furnace: SFD/Semi/TH',
    'Other(FS)',
    'Other(MS)',
    'Inside and Outside Drains',
    'Other Temporary Tents',
    'Building Permit Related(FS)',
    'Other(TS)',
    'Alter: Boiler/Furnace/AC Replacement',
    'Shoring',
    'Backflow Prevention Devices (Water only)',
    'Temporary Structures',
    'HVAC: SFD/Semi/TH',
    'Retaining Wall',
    'HVAC: Other Group C Buildings',
    'Emergency Lighting',
    'Solar Domestic Hot Water (Res)',
    'Sign Building Permit Related',
    'Crane Runway',
    'Alternative Solution',
    'Solar Collector',
    'Standpipes',
    'Party Wall Admin Permits',
    'Back Water Valve (Sewer only)',
    'HVAC: Group F > 230 Sq M',
    'Pool Fence Enclosure',
    'Fire Doors Retrofit',
    'Exterior Tank & Support',
    'Fireplace/Wood Stoves',
    'Trailers',
    'HVAC: Group F up to 230 Sq M',
    'Material Evaluation',
    'Unknown',
    'HVAC',
    'Install/Alter Plumbing & HVAC only',
    'Accessory Structure',
    'Partial Permit - Other',
    'Addition',
    'Satellite Dish',
    'Pedestrian Bridge',
    'Holding Tank: Sewage System',
    'HVAC: Laboratories',
    'Ceilings (Add or Replace)',
    'Other'
]

combined_buildingPermits = combined_buildingPermits[~combined_buildingPermits['WORK'].isin(no_work_types)]

#print("number of rows:", len(combined_buildingPermits))

# changing date types
combined_buildingPermits['ISSUED_DATE'] = pd.to_datetime(combined_buildingPermits['ISSUED_DATE'])
combined_buildingPermits['APPLICATION_DATE'] = pd.to_datetime(combined_buildingPermits['APPLICATION_DATE'])

# changing int types
combined_buildingPermits['EST_CONST_COST'] = combined_buildingPermits['EST_CONST_COST'].str.replace(',', '')  # Remove commas
combined_buildingPermits['EST_CONST_COST'] = pd.to_numeric(combined_buildingPermits['EST_CONST_COST'], errors='coerce')
combined_buildingPermits['EST_CONST_COST'] = combined_buildingPermits['EST_CONST_COST'].fillna(0).astype(int)
combined_buildingPermits['GEO_ID'] = pd.to_numeric(combined_buildingPermits['GEO_ID'], errors='coerce').astype('Int64')

# changing string types
combined_buildingPermits['PERMIT_NUM'] = combined_buildingPermits['PERMIT_NUM'].astype(str)
combined_buildingPermits['PERMIT_TYPE'] = combined_buildingPermits['PERMIT_TYPE'].astype(str)
combined_buildingPermits['WORK'] = combined_buildingPermits['WORK'].astype(str)
combined_buildingPermits['STREET_NAME'] = combined_buildingPermits['STREET_NAME'].astype(str)
combined_buildingPermits['STREET_TYPE'] = combined_buildingPermits['STREET_TYPE'].astype(str)
combined_buildingPermits['STREET_NUM'] = combined_buildingPermits['STREET_NUM'].astype(str)
combined_buildingPermits['STREET_DIRECTION'] = combined_buildingPermits['STREET_DIRECTION'].astype(str)
combined_buildingPermits['POSTAL'] = combined_buildingPermits['POSTAL'].astype(str)
combined_buildingPermits['WARD_GRID'] = combined_buildingPermits['WARD_GRID'].astype(str)
combined_buildingPermits['DESCRIPTION'] = combined_buildingPermits['DESCRIPTION'].astype(str)
combined_buildingPermits['STATUS'] = combined_buildingPermits['STATUS'].astype(str)

# change format of column names
combined_buildingPermits.columns = ['_'.join(word.capitalize() for word in col.split('_')) for col in combined_buildingPermits.columns]

# Check the new column names
print(combined_buildingPermits.columns)
# output final building permit dimension
#combined_buildingPermits.to_csv('BuildingPermitDimension.csv', index=False)


with engine.connect() as conn:
    # load dataframe to database
    combined_buildingPermits.to_sql('BuildingPermitDimension', engine, if_exists='replace', index=False)
    
    # Then add the surrogate key column
    conn.execute(text("""
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT FROM information_schema.columns 
                WHERE table_schema = 'public' 
                AND table_name   = 'BuildingPermitDimension' 
                AND column_name  = 'Permit_Key'
            ) THEN
                ALTER TABLE public."BuildingPermitDimension"
                ADD COLUMN Permit_Key serial PRIMARY KEY;
            END IF;
        END
        $$;
    """))
    conn.execute(text("SELECT setval('Permit_Key', (SELECT MAX(Permit_Key) FROM public.\"BuildingPermitDimension\"));"))

#print("number of rows:", len(combined_b]

# Calculate the number of duplicate PERMIT_NUM values in the filtered DataFrame
#number_of_closed_duplicates = closed_permits['PERMIT_NUM'].duplicated().sum()

#print(f"Number of duplicated PERMIT_NUM values with STATUS 'Closed': {number_of_closed_duplicates}")

#closer look into duplicate entries for permit number
#duplicates_df = combined_buildingPermits[combined_buildingPermits.duplicated('PERMIT_NUM', keep=False)]
#duplicates_df.to_csv('duplicates.csv', index=False)

# Close the engine connection when done
engine.dispose()
