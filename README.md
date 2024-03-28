# CSI4142---Project

Ensure that Python 3.6 or newer is installed on your machine.
Please install the following libraries with this command:
pip install pandas sqlalchemy requests Shapely


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