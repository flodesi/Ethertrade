# from web3 import Web3
# import json
#
# ganache_url = 'http://127.0.0.1:7545'
# web3 = Web3(Web3.HTTPProvider(ganache_url))
#
# abi = json.loads('[{"name": "TokenPurchase", "inputs": [{"type": "address", "name": "buyer", "indexed": true}, {"type": "uint256", "name": "eth_sold", "indexed": true}, {"type": "uint256", "name": "tokens_bought", "indexed": true}], "anonymous": false, "type": "event"}, {"name": "EthPurchase", "inputs": [{"type": "address", "name": "buyer", "indexed": true}, {"type": "uint256", "name": "tokens_sold", "indexed": true}, {"type": "uint256", "name": "eth_bought", "indexed": true}], "anonymous": false, "type": "event"}, {"name": "AddLiquidity", "inputs": [{"type": "address", "name": "provider", "indexed": true}, {"type": "uint256", "name": "eth_amount", "indexed": true}, {"type": "uint256", "name": "token_amount", "indexed": true}], "anonymous": false, "type": "event"}, {"name": "RemoveLiquidity", "inputs": [{"type": "address", "name": "provider", "indexed": true}, {"type": "uint256", "name": "eth_amount", "indexed": true}, {"type": "uint256", "name": "token_amount", "indexed": true}], "anonymous": false, "type": "event"}, {"name": "Transfer", "inputs": [{"type": "address", "name": "_from", "indexed": true}, {"type": "address", "name": "_to", "indexed": true}, {"type": "uint256", "name": "_value", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "Approval", "inputs": [{"type": "address", "name": "_owner", "indexed": true}, {"type": "address", "name": "_spender", "indexed": true}, {"type": "uint256", "name": "_value", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "setup", "outputs": [], "inputs": [{"type": "address", "name": "token_addr"}], "constant": false, "payable": false, "type": "function", "gas": 175875}, {"name": "addLiquidity", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "min_liquidity"}, {"type": "uint256", "name": "max_tokens"}, {"type": "uint256", "name": "deadline"}], "constant": false, "payable": true, "type": "function", "gas": 82616}, {"name": "removeLiquidity", "outputs": [{"type": "uint256", "name": "out"}, {"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "amount"}, {"type": "uint256", "name": "min_eth"}, {"type": "uint256", "name": "min_tokens"}, {"type": "uint256", "name": "deadline"}], "constant": false, "payable": false, "type": "function", "gas": 116814}, {"name": "__default__", "outputs": [], "inputs": [], "constant": false, "payable": true, "type": "function"}, {"name": "ethToTokenSwapInput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "min_tokens"}, {"type": "uint256", "name": "deadline"}], "constant": false, "payable": true, "type": "function", "gas": 12757}, {"name": "ethToTokenTransferInput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "min_tokens"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "recipient"}], "constant": false, "payable": true, "type": "function", "gas": 12965}, {"name": "ethToTokenSwapOutput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_bought"}, {"type": "uint256", "name": "deadline"}], "constant": false, "payable": true, "type": "function", "gas": 50463}, {"name": "ethToTokenTransferOutput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_bought"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "recipient"}], "constant": false, "payable": true, "type": "function", "gas": 50671}, {"name": "tokenToEthSwapInput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_sold"}, {"type": "uint256", "name": "min_eth"}, {"type": "uint256", "name": "deadline"}], "constant": false, "payable": false, "type": "function", "gas": 47503}, {"name": "tokenToEthTransferInput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_sold"}, {"type": "uint256", "name": "min_eth"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "recipient"}], "constant": false, "payable": false, "type": "function", "gas": 47712}, {"name": "tokenToEthSwapOutput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "eth_bought"}, {"type": "uint256", "name": "max_tokens"}, {"type": "uint256", "name": "deadline"}], "constant": false, "payable": false, "type": "function", "gas": 50175}, {"name": "tokenToEthTransferOutput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "eth_bought"}, {"type": "uint256", "name": "max_tokens"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "recipient"}], "constant": false, "payable": false, "type": "function", "gas": 50384}, {"name": "tokenToTokenSwapInput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_sold"}, {"type": "uint256", "name": "min_tokens_bought"}, {"type": "uint256", "name": "min_eth_bought"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "token_addr"}], "constant": false, "payable": false, "type": "function", "gas": 51007}, {"name": "tokenToTokenTransferInput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_sold"}, {"type": "uint256", "name": "min_tokens_bought"}, {"type": "uint256", "name": "min_eth_bought"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "recipient"}, {"type": "address", "name": "token_addr"}], "constant": false, "payable": false, "type": "function", "gas": 51098}, {"name": "tokenToTokenSwapOutput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_bought"}, {"type": "uint256", "name": "max_tokens_sold"}, {"type": "uint256", "name": "max_eth_sold"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "token_addr"}], "constant": false, "payable": false, "type": "function", "gas": 54928}, {"name": "tokenToTokenTransferOutput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_bought"}, {"type": "uint256", "name": "max_tokens_sold"}, {"type": "uint256", "name": "max_eth_sold"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "recipient"}, {"type": "address", "name": "token_addr"}], "constant": false, "payable": false, "type": "function", "gas": 55019}, {"name": "tokenToExchangeSwapInput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_sold"}, {"type": "uint256", "name": "min_tokens_bought"}, {"type": "uint256", "name": "min_eth_bought"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "exchange_addr"}], "constant": false, "payable": false, "type": "function", "gas": 49342}, {"name": "tokenToExchangeTransferInput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_sold"}, {"type": "uint256", "name": "min_tokens_bought"}, {"type": "uint256", "name": "min_eth_bought"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "recipient"}, {"type": "address", "name": "exchange_addr"}], "constant": false, "payable": false, "type": "function", "gas": 49532}, {"name": "tokenToExchangeSwapOutput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_bought"}, {"type": "uint256", "name": "max_tokens_sold"}, {"type": "uint256", "name": "max_eth_sold"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "exchange_addr"}], "constant": false, "payable": false, "type": "function", "gas": 53233}, {"name": "tokenToExchangeTransferOutput", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_bought"}, {"type": "uint256", "name": "max_tokens_sold"}, {"type": "uint256", "name": "max_eth_sold"}, {"type": "uint256", "name": "deadline"}, {"type": "address", "name": "recipient"}, {"type": "address", "name": "exchange_addr"}], "constant": false, "payable": false, "type": "function", "gas": 53423}, {"name": "getEthToTokenInputPrice", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "eth_sold"}], "constant": true, "payable": false, "type": "function", "gas": 5542}, {"name": "getEthToTokenOutputPrice", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_bought"}], "constant": true, "payable": false, "type": "function", "gas": 6872}, {"name": "getTokenToEthInputPrice", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "tokens_sold"}], "constant": true, "payable": false, "type": "function", "gas": 5637}, {"name": "getTokenToEthOutputPrice", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "uint256", "name": "eth_bought"}], "constant": true, "payable": false, "type": "function", "gas": 6897}, {"name": "tokenAddress", "outputs": [{"type": "address", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 1413}, {"name": "factoryAddress", "outputs": [{"type": "address", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 1443}, {"name": "balanceOf", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "address", "name": "_owner"}], "constant": true, "payable": false, "type": "function", "gas": 1645}, {"name": "transfer", "outputs": [{"type": "bool", "name": "out"}], "inputs": [{"type": "address", "name": "_to"}, {"type": "uint256", "name": "_value"}], "constant": false, "payable": false, "type": "function", "gas": 75034}, {"name": "transferFrom", "outputs": [{"type": "bool", "name": "out"}], "inputs": [{"type": "address", "name": "_from"}, {"type": "address", "name": "_to"}, {"type": "uint256", "name": "_value"}], "constant": false, "payable": false, "type": "function", "gas": 110907}, {"name": "approve", "outputs": [{"type": "bool", "name": "out"}], "inputs": [{"type": "address", "name": "_spender"}, {"type": "uint256", "name": "_value"}], "constant": false, "payable": false, "type": "function", "gas": 38769}, {"name": "allowance", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [{"type": "address", "name": "_owner"}, {"type": "address", "name": "_spender"}], "constant": true, "payable": false, "type": "function", "gas": 1925}, {"name": "name", "outputs": [{"type": "bytes32", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 1623}, {"name": "symbol", "outputs": [{"type": "bytes32", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 1653}, {"name": "decimals", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 1683}, {"name": "totalSupply", "outputs": [{"type": "uint256", "name": "out"}], "inputs": [], "constant": true, "payable": false, "type": "function", "gas": 1713}]')
# address = '0x6b175474e89094c44da98b954eedeac495271d0f'
#
# contract =  web3.eth.contract(address=address, abi=abi)
#
# print(contract)

# from tkinter import *
# import csv
#
# contracts = []
# with open('customer_contracts.csv', 'rt') as rf:
#      reader = csv.reader(rf, delimiter=',')
#      test = True
#      for row in reader:
#          if test:
#              test = False
#              continue
#          row[0] = int(row[0])
#          row[3] = float(row[3])
#          row[4] = float(row[4])
#          print(row)
#          contracts.append(row)

# from tkinter import *
# from tkinter.ttk import *
# import csv
#
# class App(Frame):
#
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.CreateUI()
#         self.LoadTable()
#         self.grid(sticky = (N,S,W,E))
#         parent.grid_rowconfigure(0, weight = 1)
#         parent.grid_columnconfigure(0, weight = 1)
#
#     def CreateUI(self):
#         tv = Treeview(self)
#         tv['columns'] = ('buyer', 'seller', 'total', 'balance', 'date', 'status', 'tracking','carrier')
#         tv.heading("#0", text='Contract ID', anchor='w')
#         tv.column("#0", anchor="w")
#         # tv.heading('contract', text='Contract ID')
#         # tv.column('contract', anchor='center', width=100)
#         tv.heading('buyer', text='Buyer Name')
#         tv.column('buyer', anchor='center', width=100)
#         tv.heading('seller', text='Seller Name')
#         tv.column('seller', anchor='center', width=100)
#         tv.heading('total', text='Total Amount')
#         tv.column('total', anchor='center', width=100)
#         tv.heading('balance', text='Balance Owing')
#         tv.column('balance', anchor='center', width=100)
#         tv.heading('date', text='Date')
#         tv.column('date', anchor='center', width=100)
#         tv.heading('status', text='Status')
#         tv.column('status', anchor='center', width=100)
#         tv.heading('tracking', text='Tracking Number')
#         tv.column('tracking', anchor='center', width=100)
#         tv.heading('carrier', text='Carrier')
#         tv.column('carrier', anchor='center', width=100)
#         tv.grid(sticky = (N,S,W,E))
#         self.treeview = tv
#         self.grid_rowconfigure(0, weight = 1)
#         self.grid_columnconfigure(0, weight = 1)
#         button = Button(root, text='Stop', width=25, command='')
#         button.pack()
#
#     def LoadTable(self):
#         contracts = []
#         with open('customer_contracts.csv', 'rt') as rf:
#              reader = csv.reader(rf, delimiter=',')
#              test = True
#              for row in reader:
#                  if test:
#                      test = False
#                      continue
#                  row[0] = int(row[0])
#                  row[3] = float(row[3])
#                  row[4] = float(row[4])
#                  print(row)
#                  contracts.append(row)
#         rf.close()
#         for item in contracts:
#             self.treeview.insert('', 'end', text=item[0], values=(item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8]))
#
# root = Tk()
# App(root)
# root.mainloop()


# import tkinter, configparser, random, os, tkinter.messagebox, tkinter.simpledialog
#
# window = tkinter.Tk()
#
# window.title("Minesweeper")
#
# #prepare default values
#
# rows = 10
# cols = 10
# mines = 10
#
# field = []
# buttons = []
#
# colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']
#
# gameover = False
# customsizes = []
#
#
# def createMenu():
#     menubar = tkinter.Menu(window)
#     menusize = tkinter.Menu(window, tearoff=0)
#     menusize.add_command(label="small (10x10 with 10 mines)", command=lambda: setSize(10, 10, 10))
#     menusize.add_command(label="medium (20x20 with 40 mines)", command=lambda: setSize(20, 20, 40))
#     menusize.add_command(label="big (35x35 with 120 mines)", command=lambda: setSize(35, 35, 120))
#     menusize.add_command(label="custom", command=setCustomSize)
#     menusize.add_separator()
#     for x in range(0, len(customsizes)):
#         menusize.add_command(label=str(customsizes[x][0])+"x"+str(customsizes[x][1])+" with "+str(customsizes[x][2])+" mines", command=lambda customsizes=customsizes: setSize(customsizes[x][0], customsizes[x][1], customsizes[x][2]))
#     menubar.add_cascade(label="size", menu=menusize)
#     menubar.add_command(label="exit", command=lambda: window.destroy())
#     window.config(menu=menubar)
#
#
# def setCustomSize():
#     global customsizes
#     r = tkinter.simpledialog.askinteger("Custom size", "Enter amount of rows")
#     c = tkinter.simpledialog.askinteger("Custom size", "Enter amount of columns")
#     m = tkinter.simpledialog.askinteger("Custom size", "Enter amount of mines")
#     while m > r*c:
#         m = tkinter.simpledialog.askinteger("Custom size", "Maximum mines for this dimension is: " + str(r*c) + "\nEnter amount of mines")
#     customsizes.insert(0, (r,c,m))
#     customsizes = customsizes[0:5]
#     setSize(r,c,m)
#     createMenu()
#
# def setSize(r,c,m):
#     global rows, cols, mines
#     rows = r
#     cols = c
#     mines = m
#     saveConfig()
#     restartGame()
#
# def saveConfig():
#     global rows, cols, mines
#     #configuration
#     config = configparser.SafeConfigParser()
#     config.add_section("game")
#     config.set("game", "rows", str(rows))
#     config.set("game", "cols", str(cols))
#     config.set("game", "mines", str(mines))
#     config.add_section("sizes")
#     config.set("sizes", "amount", str(min(5,len(customsizes))))
#     for x in range(0,min(5,len(customsizes))):
#         config.set("sizes", "row"+str(x), str(customsizes[x][0]))
#         config.set("sizes", "cols"+str(x), str(customsizes[x][1]))
#         config.set("sizes", "mines"+str(x), str(customsizes[x][2]))
#
#     with open("config.ini", "w") as file:
#         config.write(file)
#
# def loadConfig():
#     global rows, cols, mines, customsizes
#     config = configparser.SafeConfigParser()
#     config.read("config.ini")
#     rows = config.getint("game", "rows")
#     cols = config.getint("game", "cols")
#     mines = config.getint("game", "mines")
#     amountofsizes = config.getint("sizes", "amount")
#     for x in range(0, amountofsizes):
#         customsizes.append((config.getint("sizes", "row"+str(x)), config.getint("sizes", "cols"+str(x)), config.getint("sizes", "mines"+str(x))))
#
# def prepareGame():
#     global rows, cols, mines, field
#     field = []
#     for x in range(0, rows):
#         field.append([])
#         for y in range(0, cols):
#             #add button and init value for game
#             field[x].append(0)
#     #generate mines
#     for _ in range(0, mines):
#         x = random.randint(0, rows-1)
#         y = random.randint(0, cols-1)
#         #prevent spawning mine on top of each other
#         while field[x][y] == -1:
#             x = random.randint(0, rows-1)
#             y = random.randint(0, cols-1)
#         field[x][y] = -1
#         if x != 0:
#             if y != 0:
#                 if field[x-1][y-1] != -1:
#                     field[x-1][y-1] = int(field[x-1][y-1]) + 1
#             if field[x-1][y] != -1:
#                 field[x-1][y] = int(field[x-1][y]) + 1
#             if y != cols-1:
#                 if field[x-1][y+1] != -1:
#                     field[x-1][y+1] = int(field[x-1][y+1]) + 1
#         if y != 0:
#             if field[x][y-1] != -1:
#                 field[x][y-1] = int(field[x][y-1]) + 1
#         if y != cols-1:
#             if field[x][y+1] != -1:
#                 field[x][y+1] = int(field[x][y+1]) + 1
#         if x != rows-1:
#             if y != 0:
#                 if field[x+1][y-1] != -1:
#                     field[x+1][y-1] = int(field[x+1][y-1]) + 1
#             if field[x+1][y] != -1:
#                 field[x+1][y] = int(field[x+1][y]) + 1
#             if y != cols-1:
#                 if field[x+1][y+1] != -1:
#                     field[x+1][y+1] = int(field[x+1][y+1]) + 1
#
# def prepareWindow():
#     global rows, cols, buttons
#     tkinter.Button(window, text="Restart", command=restartGame).grid(row=0, column=0, columnspan=cols, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
#     buttons = []
#     for x in range(0, rows):
#         buttons.append([])
#         for y in range(0, cols):
#             b = tkinter.Button(window, text=" ", width=2, command=lambda x=x,y=y: clickOn(x,y))
#             b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
#             b.grid(row=x+1, column=y, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
#             buttons[x].append(b)
#
# def restartGame():
#     global gameover
#     gameover = False
#     #destroy all - prevent memory leak
#     for x in window.winfo_children():
#         if type(x) != tkinter.Menu:
#             x.destroy()
#     prepareWindow()
#     prepareGame()
#
# def clickOn(x,y):
#     global field, buttons, colors, gameover, rows, cols
#     if gameover:
#         return
#     buttons[x][y]["text"] = str(field[x][y])
#     if field[x][y] == -1:
#         buttons[x][y]["text"] = "*"
#         buttons[x][y].config(background='red', disabledforeground='black')
#         gameover = True
#         tkinter.messagebox.showinfo("Game Over", "You have lost.")
#         #now show all other mines
#         for _x in range(0, rows):
#             for _y in range(cols):
#                 if field[_x][_y] == -1:
#                     buttons[_x][_y]["text"] = "*"
#     else:
#         buttons[x][y].config(disabledforeground=colors[field[x][y]])
#     if field[x][y] == 0:
#         buttons[x][y]["text"] = " "
#         #now repeat for all buttons nearby which are 0... kek
#         autoClickOn(x,y)
#     buttons[x][y]['state'] = 'disabled'
#     buttons[x][y].config(relief=tkinter.SUNKEN)
#     checkWin()
#
# def autoClickOn(x,y):
#     global field, buttons, colors, rows, cols
#     if buttons[x][y]["state"] == "disabled":
#         return
#     if field[x][y] != 0:
#         buttons[x][y]["text"] = str(field[x][y])
#     else:
#         buttons[x][y]["text"] = " "
#     buttons[x][y].config(disabledforeground=colors[field[x][y]])
#     buttons[x][y].config(relief=tkinter.SUNKEN)
#     buttons[x][y]['state'] = 'disabled'
#     if field[x][y] == 0:
#         if x != 0 and y != 0:
#             autoClickOn(x-1,y-1)
#         if x != 0:
#             autoClickOn(x-1,y)
#         if x != 0 and y != cols-1:
#             autoClickOn(x-1,y+1)
#         if y != 0:
#             autoClickOn(x,y-1)
#         if y != cols-1:
#             autoClickOn(x,y+1)
#         if x != rows-1 and y != 0:
#             autoClickOn(x+1,y-1)
#         if x != rows-1:
#             autoClickOn(x+1,y)
#         if x != rows-1 and y != cols-1:
#             autoClickOn(x+1,y+1)
#
# def onRightClick(x,y):
#     global buttons
#     if gameover:
#         return
#     if buttons[x][y]["text"] == "?":
#         buttons[x][y]["text"] = " "
#         buttons[x][y]["state"] = "normal"
#     elif buttons[x][y]["text"] == " " and buttons[x][y]["state"] == "normal":
#         buttons[x][y]["text"] = "?"
#         buttons[x][y]["state"] = "disabled"
#
# def checkWin():
#     global buttons, field, rows, cols
#     win = True
#     for x in range(0, rows):
#         for y in range(0, cols):
#             if field[x][y] != -1 and buttons[x][y]["state"] == "normal":
#                 win = False
#     if win:
#         tkinter.messagebox.showinfo("Gave Over", "You have won.")
#
# if os.path.exists("config.ini"):
#     loadConfig()
# else:
#     saveConfig()
#
# createMenu()
#
# prepareWindow()
# prepareGame()
# window.mainloop()
