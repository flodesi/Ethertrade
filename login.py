from tkinter import *
import csv
import data_handling as dh


def login():
    global window2
    window2 = Toplevel(window)
    window2.title("Login")
    window2.geometry("300x250")
    Label(window2, text = "Kindly enter login details below:").pack()
    Label(window2, text = "").pack()

    global entered_username
    global entered_password

    entered_username = StringVar()
    entered_password = StringVar()

    # global username_entry1
    # global password_entry1

    Label(window2, text = "Username * ").pack()
    entered_username = Entry(window2, textvariable = entered_username)
    entered_username.pack()
    Label(window2, text = "").pack()
    Label(window2, text = "Password * ").pack()
    entered_password = Entry(window2, textvariable = entered_password)
    entered_password.pack()
    Label(window2, text = "").pack()
    Button(window2, text = "Login", width = 10, height = 1, command = login_verification).pack()


def login_verification():
    username1 = entered_username.get()
    password1 = entered_password.get()

    login_credentials = {}
    with open("login.csv", "rt") as rf:
        reader = csv.reader(rf, delimiter= ',')
        for row in reader:
            login_credentials[row[0]] = row[1]

    if username1 in login_credentials:
        if login_credentials[username1] == password1:
            correct_login()
        else:
            password_incorrect()
    else:
        unp_not_found()

def correct_login():
    login_sitting()


def password_incorrect():
    global window4
    window4 = Toplevel(window)
    window4.title("user_information")
    window4.geometry("300x250")
    Label(window4, text = "Password Incorrect.").pack()
    Button(window4, text = "O.K.", width = 10, height = 1, command = close2).pack()

def unp_not_found():
    global window5
    window5 = Toplevel(window)
    window5.title("user_information")
    window5.geometry("300x250")
    Label(window5, text = "Username and Password not found.").pack()
    Button(window5, text = "O.K.", width = 10, height = 1, command = close3).pack()

def close2():
    window4.destroy()

def close3():
    window5.destroy()

def login_sitting():
    window8 = Toplevel(window)
    window8.title("User Information")
    window8.geometry("300x250")
    Label(window8, text = "Dashboard").pack()
    Button(window8, text = "Create Contract", command = initialize_contract).pack()
    Button(window8, text = "View Contracts", command = view_contracts).pack()



def initialize_contract():

    global buyer_name
    buyer_name = StringVar()
    global total_amount
    total_amount = StringVar()
    global date
    date = StringVar()

    global window9
    window9 = Toplevel(window)
    window9.title("User Information")
    window9.geometry("300x250")
    Label(window9, text = "Dashboard").pack()

    Label(window9, text = "Buyer Name").pack()
    Entry(window9, textvariable = buyer_name).pack()
    Label(window9, text = "Total Amount").pack()
    Entry(window9, textvariable = total_amount).pack()
    Label(window9, text = "Date").pack()
    Entry(window9, textvariable = date).pack()
    Button(window9, text = "Create", command = create_contract).pack()

def create_contract():

    customer_contactlist = []
    contract_idlist = []
    with open("customer_contracts.csv", "rt") as rf:
        reader = csv.reader(rf, delimiter= ',')
        for row in reader:
            customer_contactlist.append(row)
            contract_idlist.append(int(row[0]))

        new_id = max(contract_idlist) + 1
        s_name = entered_username.get()
        customer_contactlist.append([new_id, buyer_name.get(), s_name, total_amount.get(), total_amount.get(), date.get(), "incomplete", "", ""])
    rf.close()

    with open("customer_contracts.csv", "w", newline='') as wf:
        writer = csv.writer(wf)
        writer.writerows(customer_contactlist)
    wf.close()

    Label(window9, text = "Contract Created", fg = "green" ,font = ("calibri", 11)).pack()

def view_contracts():
    global name
    name = entered_username.get()
    all_contracts = []
    with open("customer_contracts.csv", "rt") as rf:
        reader = csv.reader(rf, delimiter= ',')
        for row in reader:
            if row[1] == name or row[2] == name:
                all_contracts.append(row)

    window10 = Toplevel(window)
    window10.title("Current Contracts")
    window10.geometry("500x500")
    Label(window10, text = "Current Contracts are as follows:").pack()
    for element in all_contracts:
        Label(window10, text = element).pack()

    Button(window10, text = "Edit Contract", command = edit_contract).pack()


    # listBox.insert(END, "Contract ID | Buyer Name      \t\t | Seller Name      \t\t | Total Amount      \t\t | Seller Name      \t\t | Balamce Amount      \t\t | Date      \t\t | Status      \t\t | Tracking Number      \t\t | Carrier\n")
    # listBox.insert(END,"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # listBox.insert(END,"\n")

    # for i in range(len(all_contracts)):
    #     listBox.insert(END,(all_contracts[i][0]))
    #     listBox.insert(END,"\t |")

    #     listBox.insert(END,all_contracts[i][1])
    #     listBox.insert(END,"\t \t|")

    #     listBox.insert(END,all_contracts[i][2])
    #     listBox.insert(END,"\t \t|")

    #     listBox.insert(END,all_contracts[i][3])
    #     listBox.insert(END,"\t \t|")

    #     listBox.insert(END,all_contracts[i][4])
    #     listBox.insert(END,"\t \t|")

    #     listBox.insert(END,all_contracts[i][5])
    #     listBox.insert(END,"\t \t|")

    #     listBox.insert(END,all_contracts[i][6])
    #     listBox.insert(END,"\t \t|")

    #     listBox.insert(END,all_contracts[i][7])
    #     listBox.insert(END,"\t \t|")

    #     listBox.insert(END,all_contracts[i][8])
    #     listBox.insert(END,"\n")

    #     scores = Tk()
    #     label = Label(scores, text="High Scores", font = ("Arial",30)).grid(row = 0, columnspan = 3)
    #     listBox= Text(scores,width = 40)
    #     listBox.grid(row = 1,column= 0, columnspan = 2)
    #     showScores = Button(scores, text = "Show scores",width = 15, command = show).grid(row = 4, column = 0)
    #     closeButton = Button(scores, text = "Close",width = 15, command = exit).grid(row = 4, column = 1)

    #     scores.mainloop()


def edit_contract():

    global cntrt_id
    cntrt_id = StringVar()

    window11 = Toplevel(window)
    window11.title("Edit Contract")
    window11.geometry("500x100")
    Label(window11, text = "Please enter the Contract ID of the contract you wish to edit:").pack()
    Entry(window11, textvariable = cntrt_id).pack()
    Button(window11, text = "Edit", command = update_contract).pack()

def update_contract():
    name = entered_username.get()
    all_contracts_lst = []
    with open("customer_contracts.csv", "rt") as rf:
        reader = csv.reader(rf, delimiter= ',')
        for row in reader:
            if row[0] == cntrt_id.get():
                if row[1] == name:  # buyer
                    global amount
                    amount = StringVar()

                    window12 = Toplevel(window)
                    window12.title("Add Funds to Contracts")
                    window12.geometry("500x500")
                    Label(window12, text = "Amount:").pack()
                    Entry(window12, textvariable = amount).pack()
                    Button(window12, text = "Update Contract", command = update_buyer).pack()

                elif row[2] == name: # seller
                    global trk_no
                    trk_no = StringVar()
                    global carr
                    carr = StringVar()

                    window13 = Toplevel(window)
                    window13.title("Current Contracts")
                    window13.geometry("500x100")
                    Label(window13, text = "trk_no:").pack()
                    Entry(window13, textvariable = trk_no).pack()
                    Label(window13, text = "carr:").pack()
                    Entry(window13, textvariable = carr).pack()
                    Button(window13, text = "Update Contract", command = update_seller).pack()

def update_buyer():
    dhand = dh.data_handling()
    dhand.add_funds_to_contract(cntrt_id.get(), amount.get())

def update_seller():
    dhand = dh.data_handling()
    dhand.add_tracking(cntrt_id.get(), trk_no.get(), carr.get())








def register():
    global window1
    window1 = Toplevel(window)
    window1.title("Register")
    window1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(window1, text = "Kindly enter details below:").pack()
    Label(window1, text = "").pack()
    Label(window1, text = "Username * ").pack()
    username_entry = Entry(window1, textvariable = username)
    username_entry.pack()

    Label(window1, text = "Password * ").pack()
    password_entry =  Entry(window1, textvariable = password, show = "*")
    password_entry.pack()
    Label(window1, text = "").pack()
    Button(window1, text = "Register", width = 10, height = 1, command = register_user).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    user_wallet_key_lst = []
    with open("users.csv", "rt") as rf:
        reader = csv.reader(rf, delimiter= ',')
        for row in reader:
            user_wallet_key_lst.append(row)

    wallet_address = user_wallet_key_lst[0][0]
    private_key = user_wallet_key_lst[0][1]

    rf.close()

    with open("users.csv", "w", newline='') as wf:
        writer = csv.writer(wf)
        writer.writerows(user_wallet_key_lst)
    wf.close()


    file=open('login.txt', "r")
    if file.readline() == "":
        file.close()
        file=open('login.txt', "a")
        file.write(username_info + "," + password_info + "," + wallet_address + "," + private_key)
        file.close()
    else:
        file.close()
        file=open('login.txt', "a")
        file.write("\n" + username_info + "," + password_info + "," + wallet_address + "," + private_key)
        file.close()



    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(window1, text = "Registration Complete", fg = "green" ,font = ("calibri", 11)).pack()



def main_window():
    global window
    window = Tk()
    window.geometry("300x250")
    window.title("Ethertrade")
    Label(text = "Ethertrade", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register",height = "2", width = "30", command = register).pack()

    window.mainloop()

main_window()
