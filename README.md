# Project README

## Setting Up and Testing the PostgreSQL Database

Follow these steps to set up and test the PostgreSQL database:

1. **Ensure PostgreSQL is Running**  
    Make sure you have a PostgreSQL server installed, running, and accessible. Verify that you can connect to it using your preferred database client.

2. **Set Up the `.env` File for Database Credentials**  
    The project uses a `.env` file to store database credentials securely.  
    - Create a `.env` file in the root directory of the project if it doesn't already exist.  
    - Add the following variables to the `.env` file, replacing the placeholders with your actual database credentials:  
      ```
      DB_HOST=your_database_host
      DB_PORT=your_database_port
      DB_NAME=your_database_name
      DB_USER=your_database_user
      DB_PASSWORD=your_database_password
      ```  
    - Ensure the `.env` file is included in your `.gitignore` file to prevent it from being committed to version control.  
    - The `initialize_database.py` script and `test_database.ipynb` notebook will automatically load these credentials using the `python-dotenv` library.

3. **Initialize the Database**  
    Use the `initialize_database.py` script to set up the database schema and populate it with any necessary initial data:  
    - Ensure you have Python installed and the required dependencies. Install dependencies using:  
      ```bash
      pip install -r requirements.txt
      ```  
    - Run the `initialize_database.py` script:  
      ```bash
      python initialize_database.py
      ```

4. **Test the Database with the Python Notebook**  
    Use the provided Python notebook to test the database:  
    - Open the notebook in your preferred environment (e.g., Jupyter Notebook):  
      ```bash
      jupyter notebook test_database.ipynb
      ```  
    - Follow the instructions in the notebook to connect to the database and run test queries.  
    - Verify that the database is functioning as expected by observing the outputs of the test cells.

## Notes

- Ensure your PostgreSQL server is running and accessible before running the script or notebook.
- For troubleshooting, check the logs or error messages for more details.
