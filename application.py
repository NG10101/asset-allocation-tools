import psycopg2

DB_NAME = "*****"
DB_USER = "*****"
DB_PASS = "*****"
DB_HOST = "salt.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)

print("Hi what's your name")

name = input()
print('Hi ' + name.capitalize() + '!') 

while True:
	try:
		age = int(float(input("What's your age?")))
		break
	except:
		print("Please type your age in numbers!")

if age < 18:
    print("You're too young to invest in a pension scheme!")
elif age > 65:
    print("You have reached the retirement age now, Relax!")
elif age > 18:
    age == 35
elif age > 55:
    age == 55