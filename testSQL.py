import pyodbc


connection = None
def create_cursor():

    driver = "ODBC Driver 17 for SQL Server"
    server = "EPPLKRAW0392\\SQLEXPRESS"
    database = "AdventureWorks2012"
    username = "testLogin"
    password = "11111"
    connectionString = ("DRIVER=" + driver + ";SERVER=" + server + ";DATABASE=" + database + ";UID=" + username + ";PWD=" + password)
    global connection
    if connection == None:
        connection = pyodbc.connect(connectionString)
        connection.autocommit = True
    return connection.cursor()



def test_person_address_count_columns():
    """ Check th number of columns in the Person.Address table."""

    cursor = create_cursor()
    cursor.execute("SELECT COUNT(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'Person' AND TABLE_NAME = 'Address'")
    columns_amount = cursor.fetchone()[0]
    expected_result = 9
    assert columns_amount == expected_result



def test_person_address_avg_StateProvinceID():
    """ Check the average value of the StateProvinceID column in the Person.Address table."""

    cursor = create_cursor()
    cursor.execute("SELECT AVG(StateProvinceID) AS AverageStateProvinceID FROM Person.Address")
    avg_value = cursor.fetchone()[0]
    expected_result = 49
    assert avg_value == expected_result

def test_production_document_min_ChangeNumber():
    """ Check the minimum value of the ChangeNumber column in the Production.Document table."""

    cursor = create_cursor()
    cursor.execute("SELECT MIN(ChangeNumber) AS MinChangeNumber FROM Production.Document")
    min_value = cursor.fetchone()[0]
    expected_result = 0
    assert min_value == expected_result



def test_production_document_max_len_FileName():
    """ Determines the maximum length of the FileName column in the Production.Document table."""

    cursor = create_cursor()
    cursor.execute("SELECT MAX(LEN(FileName)) AS MAXFileName FROM Production.Document")
    max_len_value = cursor.fetchone()[0]
    expected_result = 52
    assert max_len_value == expected_result

def test_production_UnitMeasure_count_null():
    """ Counts the number of NULL values in the Name column of the Production.UnitMeasure table."""

    cursor = create_cursor()
    cursor.execute("SELECT COUNT(Name) AS NullUnitMeasureCount FROM Production.UnitMeasure WHERE Name IS NULL")
    count_null = cursor.fetchone()[0]
    expected_result = 0
    assert count_null == expected_result

def test_production_document_min_len_name():
    """ Check the minimum length of values in the Name column of the Production.UnitMeasure table."""

    cursor = create_cursor()
    cursor.execute("SELECT MIN(LEN(Name)) AS MinName FROM Production.UnitMeasure")
    min_date = cursor.fetchone()[0]
    expected_result = 4
    assert min_date == expected_result