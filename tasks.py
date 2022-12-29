import webbrowser
import sys
import websites
import os
from datetime import date
import calendar
import openpyxl
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
import datetime



def daily_tasks():

    monday_tasks = '''

    Today is Monday, you need to:

        • 

    '''
    tuesday_tasks = '''

    Today is Tuesday, you need to:

        • 

    '''
    wednesday_tasks = '''

    Today is Wednesday, you need to:

        • 

    '''
    thursday_tasks = '''

    Today is Thursday, you need to:

        • 

    '''
    friday_tasks = '''

    Today is Friday, you need to:

        • 

    '''

    current_day = date.today()
    day_of_the_month = datetime.datetime.now()
    todays_day = day_of_the_month.day

    print(f"\nToday is the {todays_day}")

    weekday_name = calendar.day_name[current_day.weekday()]

    if weekday_name == 'Monday':
        print(monday_tasks)
    if weekday_name == 'Tuesday':
        print(tuesday_tasks)
    if weekday_name == 'Wednesday':
        print(wednesday_tasks)
    if weekday_name == 'Thursday':
        print(thursday_tasks)
    if weekday_name == 'Friday':
        print(friday_tasks)
    else:
        pass

def welcome_menu():

        welcome_message = input("\n\n ** Good Day Sir or Madam, Would Youm Like To See The Menu? Press 'Enter' Please ** \n\n")

        menu = ('''

            Welcome, How May I Assist You Today?

            1) Overview of Job Duties
                2) SAP
                3) Scheduling
                4) Transportation / Procurement
                5) Finance
                6) Reporting
                7) Purchase Order's (PO)
                8) Internal Docs / ICRS
                9) Production
                10) FTZ
                    11) Fahrenheit to Celsius
                    12) Celsius to Fahrenheit
                    13) Production Planning
                    14) Rail Business
                    15) X Business
                    16) Reminders
                    17) Truck Business

        ''')

        if welcome_message == "":
            print(menu)
        else:
            welcome_menu()


        selected_input = input("Please Enter Your Desired Destination! (Enter Number) Enter 'quit()' to Exit   \n")

        if selected_input == "1":
            print_job_duties()
        if selected_input == "2":
            SAP()
        if selected_input == "3":
            scheduling()
        if selected_input == "4":
            t_o_p()
        if selected_input == "5":
            finance()
        if selected_input == "6":
            reporting()
        if selected_input == "7":
            p_o()
        if selected_input == "8":
            internal()
        if selected_input == "9":
            production()
        if selected_input == "10":
            ftz()
        if selected_input == "11":
            f_to_c()
        if selected_input == "12":
            c_to_f()
        if selected_input == "13":
            production_plan()
        if selected_input == "14":
            rail_business()
        if selected_input == "15":
            x_business()
        if selected_input == "16":
            reminders()
        if selected_input == "17":
            truck_business()
        if selected_input == "quit()":
            quit()
        else:
            print("\n ****ERROR**** Please select a number from the below menu!!!!\n")
            welcome_menu()



# **************************************************************************************************************

def print_job_duties():

    print(
        '''\n
            

        ''')

    welcome_menu()

# **************************************************************************************************************


def SAP():

    text = input('''

    *************************************************************************

    Job Duties:

        - Materials Posting (Deliveries)

    *************************************************************************

    SAP Login:

    Login: 
    Password: 


    To Open the SAP Handbook 
    
    Please Press ENTER!!!!

    ''')

    if text == '':
        os.system('start SAP_Handbook_SCM.docx')
        print("*********SUCCESS*********")
    else:
        print('Please press ENTER!!!!!')
        SAP()
    
    welcome_menu()

    


# **************************************************************************************************************

def scheduling():

    print('''

    *************************************************************************

    Job Duties:

        - Train / Truck 

    *************************************************************************

    → 


    ''')

    welcome_menu()



# **************************************************************************************************************

def t_o_p():

    print('''

    *************************************************************************

    Job Duties:

        - 


    *************************************************************************
    
    
    ''')

    welcome_menu()




# **************************************************************************************************************

def finance():

    print('''

    *************************************************************************

    Job Duties:

        - 


    *************************************************************************

    
    
    ''')

    welcome_menu()




# **************************************************************************************************************

def reporting():

    print('''

    *************************************************************************

    Job Duties:

        - 



    *************************************************************************


    
    
    
    
    ''')

    welcome_menu()




# **************************************************************************************************************

def p_o():

    print('''

    *************************************************************************

    Job Duties:

        - 


    *************************************************************************


    
    
    
    
    ''')

    welcome_menu()




# **************************************************************************************************************

def internal():

    print('''

    *************************************************************************

    Job Duties:

        

        
    *************************************************************************


    
    
    
    
    ''')

    welcome_menu()




# **************************************************************************************************************

def production():

    print('''

    *************************************************************************

    Job Duties:

        - 

        
    *************************************************************************


    
    
    
    
    ''')

    welcome_menu()




# **************************************************************************************************************

def ftz():

    print('''

    *************************************************************************

    Job Duties:

        - 

        
    *************************************************************************


    
    
    
    
    ''')

    welcome_menu()




# **************************************************************************************************************

def rail_business():

    print('''

    → 

    
    ''')

    visit_webpage = input("Would you like to visit this webpage? (Y/N) \n")

    if visit_webpage == "Y":
        webbrowser.open(websites.up) #create new file where you house websites you access
        return
    if visit_webpage == "N":
        welcome_menu()
    else:
        print("Please enter 'Y' or 'N' !!\n")
        rail_business()
    
    welcome_menu()


# **************************************************************************************************************

def x_business():

    print('''

    → 

    
    ''')

    visit_webpage = input("Would you like to visit this webpage? (Y/N) \n")

    if visit_webpage == "Y":
        webbrowser.open(websites.pocc) #create new file where you house websites you access
        welcome_menu()
    if visit_webpage == "N":
        welcome_menu()
    else:
        print("Please enter 'Y' or 'N' !!")
        pocc_business()
    
    welcome_menu()


# **************************************************************************************************************

def truck_business():

    print('''

    → 

    
    ''')

    visit_webpage = input("Would you like to visit this webpage? (Y/N) \n")

    if visit_webpage == "Y":
        webbrowser.open(websites.SDI)
        welcome_menu()
    if visit_webpage == "N":
        welcome_menu()
    else:
        print("Please enter 'Y' or 'N' !!")
        truck_business()
    
    welcome_menu()

# **************************************************************************************************************

def f_to_c():

    fah = input("Please indiciate the Fahrenheit you would like to convert to Celsius? \n")

    fah = int(fah)

    celsius = round(((((fah-32)*5))/9),2)

    print(f"\n{fah} Fahrenheit is {celsius} Celsius")

    welcome_menu()


# **************************************************************************************************************

def c_to_f():

    cels = input("Please indiciate the Celsius you would like to convert to Fahrenheit? \n")

    cels = int(cels)

    fahrenheit = round(((((cels * 9)/5)+32)),2)

    print(f"\n{cels} Celsius is {fahrenheit} Fahrenheit")

    welcome_menu()



# **************************************************************************************************************



# **************************************************************************************************************

daily_tasks()
welcome_menu()













