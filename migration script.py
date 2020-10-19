import psycopg2
import xlrd
import os

DB_NAME = "********"
DB_USER = "********"
DB_PASS = "********"
DB_HOST = "salt.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
print("database connected successfully!")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE allocations
(
Age INT NOT NULL,
Asset_Equity INT NOT NULL,
Asset_Bond INT NOT NULL,
Asset_Treasury INT NOT NULL, 
Fund TEXT NOT NULL)

 """)

conn.commit()
print("Table created successfully")


# Open the workbook and define the worksheet
os.chdir(r"C:\Users\NG\Documents")
print("Directory Changed.")
book = xlrd.open_workbook("data for DB.xlsx")
sheet = book.sheet_by_name("Sheet2")
print("Opened Excel Sheet.")

query = """
INSERT INTO allocations (
    Age,
    Asset_Equity,
    Asset_Bond,
    Asset_Treasury,
    Fund) VALUES (%s, %s, %s, %s, %s)"""

# grab existing row count in the database for validation later
cursor.execute("SELECT count(*) FROM allocations")
before_import = cursor.fetchone()

for r in range(1, sheet.nrows):
    Age = sheet.cell(r,0).value
    Asset_Equity = sheet.cell(r,1).value
    Asset_Bond = sheet.cell(r,2).value
    Asset_Treasury = sheet.cell(r,3).value
    Fund = sheet.cell(r,4).value

    # Assign values from each row
    values = (Age, Asset_Equity, Asset_Bond, Asset_Treasury, Fund)

    # Execute sql Query
    cursor.execute(query, values)

# Commit the transaction
conn.commit()

# If you want to check if all rows are imported
x = cursor.execute("SELECT count(*) FROM allocations")
result = cursor.fetchone()

print(x)

conn.close()