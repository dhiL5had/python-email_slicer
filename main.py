import os
os.system("clear||cls")
def start():
    print('''
    --- Email Slicer ---

    *enter q/e to exit the program
    *enter cls/clear to clear the terminal

    ''')
    user_email= input("Enter your email : ")

    while user_email.lower() in ["e","q","exit","quit"]:
        print("\nProgram exited.\n")
        quit()

    while user_email in ["cls", "clear"]:
        os.system("clear||cls")
        start()

    (username, domain)= user_email.split("@")
    (domain, extension)= domain.split(".")

    print(f'''\n
    -- Output ---
    
    Username :  {username}
    Domain :  {domain}
    Extension :  {extension}
    ''')
    

while True:
    start()