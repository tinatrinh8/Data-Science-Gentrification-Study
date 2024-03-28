# CSI4142---Project

Ensure that Python 3.6 or newer is installed on your machine.
Please install the following libraries with this command:
pip install pandas numpy sqlalchemy

For Windows:
To work with the project's database, PostgreSQL must be installed on your machine. This will also include the pg_dump tool, which is necessary for database backup and restoration tasks.
Make sure that the path to PostgreSQL's bin directory is added to your system's PATH environment variable.
For macOS:
Open the terminal and run: brew install postgresql

Verify pg_dump installation:
open the terminal and run: pg_dump --version

Opening the database:
Launch pgAdmin, which should have come included with the PostgreSQL installation.
In the left sidebar, navigate to the "Servers" section and expand it. You should see "PostgreSQL 16". If prompted, enter your password to connect to the server.
ight-click on "Databases," then select "Create" > "Database...".
In the "Database" field, enter main as the name of your new database.
Click "Save" to create the database.
Navigate to the newly created main database, right-click on it, and choose "Restore".
In the "Restore Database" window, you'll need to specify the source file to restore from. Click the "..." button next to the "Filename" field to browse for the file.
Navigate to the project folder where the database.backup file is located, select it, and click "Open".
Once the file is selected, click "Restore" to begin the restoration process.