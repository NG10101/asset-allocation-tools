from tkinter import *
import psycopg2
import matplotlib.pyplot as plt

DB_NAME = "*****"
DB_USER = "*****"
DB_PASS = "*****"
DB_HOST = "*****"
DB_PORT = "*****"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)

def input_output():
    global Client_Name
    global Client_Age
    global Client_Fund
    global raw_age
    global int_age
    Client_Name = entry_1.get()
    raw_age = (entry_2.get())
    int_age = int(raw_age)
    if int_age < 18:
            w1label_1 = Label(main_window, text="You're too young to invest in a pension scheme!")
            w1label_1.grid()  

    elif int_age > 65: 
            w1label_2 = Label(main_window, text="You have reached the retirement age now, Relax!") 
            w1label_2.grid()

    elif int_age == range(18, 36):
        int_age = 35
    elif int_age == range(55, 101):
        int_age = 55
    Client_Age = str(int_age)
    Client_Fund = optionvar.get()
    print(Client_Name, Client_Age, Client_Fund)

    cursor = conn.cursor()
    x = cursor.execute("SELECT asset_equity, asset_bond, asset_treasury from allocations where age = " + Client_Age + " and fund = " + "'" + Client_Fund + "'")
    result = cursor.fetchone()
    print(result)

    labels = 'Equity', 'Corporate Bond', 'Treasury'
    sizes = result

    
    fig1, ax1 = plt.subplots()
    fig1.suptitle('Hi '+ Client_Name.capitalize() + " asset allocation as per your risk appetite is as per below pie chart", fontsize=10)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

main_window = Tk()

main_window.title('Asset Allocation Calculator') 


label_1 = Label(main_window, text="What is your Name?") 

label_2 = Label(main_window, text="What is your Age?")

label_3 = Label(main_window, text="What is your Risk Appetite?")

entry_1 = Entry(main_window)

entry_2 = Entry(main_window)

OPTIONS = [
    "Aggressive",
    "Moderate",
    "Conservative"
]

optionvar = StringVar(main_window)
optionvar.set("Please Select")
entry_3 = OptionMenu(main_window, optionvar, *OPTIONS)

label_1.grid(row=0, sticky=W)
entry_1.grid(row=0, column=1)
label_2.grid(row=1, sticky=W)
entry_2.grid(row=1, column=1)
label_3.grid(row=2, sticky=W)
entry_3.grid(row=2, column=1)
submit_button = Button(main_window, text='Submit', command=input_output)
submit_button.grid(row=5, columnspan=2)
Pack()

mainloop()
