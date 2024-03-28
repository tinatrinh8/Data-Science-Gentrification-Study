# CSI4142: Toronto Ward Gentrification Study

Ensure that Python 3.6 or newer is installed on your machine.
Please install the following libraries with this command:
pip install pandas sqlalchemy requests Shapely json folium geopandas


For Windows:
To work with the project's database, PostgreSQL must be installed on your machine. Visit the official PostgreSQL download page and download the Windows installer for PostgreSQL.
For macOS:
Open the terminal and run "brew install postgresql" or download the macOS installer from the official PostgreSQL download page.

Restoring the database:
Launch pgAdmin, which should have come included with the PostgreSQL installation.
In the left sidebar, navigate to the "Servers" section and expand it. You should see "PostgreSQL 16". If prompted, enter your password to connect to the server.
Right-click on "Databases," then select "Create" > "Database...".
In the "Database" field, enter "main" as the name of the database.
Click "Save" to create the database.
Navigate to the newly created main database, right-click on it, and choose "Restore".
In the "Restore Database" window, you'll need to specify the source file to restore from. Click the "..." button next to the "Filename" field to browse for the file.
Navigate to the project folder where the database.backup file is located, select it, and click "Open".
Once the file is selected, click "Restore" to begin the restoration process.

For the geospatial analysis:
This part of the assignment uses the Mapbox API to make geocoding requests. As such, you need to sign up on Mapbox and generate a personal API key to run the program. 

Once the API key is generated, you simply paste to replace the "YOUR API KEY" string in the mapbox_key.json file. From there, you can begin running the geospatial Jupyer Notebook to see the full analysis by pressing Run All in your respective IDE
