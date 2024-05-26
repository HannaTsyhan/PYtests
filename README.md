Database Tests for AdventureWorks2012

This repository contains a set of tests written in Python to validate various aspects of the AdventureWorks2012 database using pyodbc for database connectivity and pytest for testing.
Table of Contents

    Prerequisites
    Setup
    Test Descriptions
    Running the Tests

Prerequisites

Before running these tests, ensure you have the following installed:

    Python 3.7 or higher
    pyodbc
    pytest

You can install the necessary Python packages using pip:

sh

    pip install pyodbc pytest

Setup

Database Connection Configuration:
The database connection details are specified in the create_cursor function. Make sure to update the connection details if your setup is different.

    python

    driver = "ODBC Driver 17 for SQL Server"
    server = "EPPLKRAW0392\\SQLEXPRESS"
    database = "AdventureWorks2012"
    username = "testLogin"
    password = "11111"

Database:
Ensure that the AdventureWorks2012 database is restored and available on the specified SQL Server instance.

To generate a report:
pytest testSQL.py --html=report.html
Test report will be stored  as report.html
