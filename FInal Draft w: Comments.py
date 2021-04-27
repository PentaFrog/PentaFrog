import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk() 

typeOfCoffee = 'oops'
drinkChoice = ''
drinkCost = 0.0
milkChoice = ''
syrupChoice = ''
espressoShot = ''

class Common_Grounds:
   #opening page
    def __init__(self):
        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)
        
        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif')
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text='CG Coffee Ordering App', bg='#e6ccb3')
        titleLabel.grid(row=0, column=4)

        descriptionLabel = tk.Label(canvas, text='Please select the type of drink you would like to be described', bg='#e6ccb3')
        descriptionLabel.grid(row=1,column=4)

        dcButton = tk.Button(canvas, text = 'Drip Coffee', bg='#bf8040', command=self.dripCoffeeFun)
        dcButton.grid(row=4, column=4)


        latteButton = tk.Button(canvas, text = 'Latte', bg='#bf8040', command=self.latteFun)
        latteButton.grid(row=5, column=4)

        mochaButton = tk.Button(canvas, text='Mocha', bg='#bf8040', command=self.mochaFun)
        mochaButton.grid(row=6, column=4)

        espressoButton = tk.Button(canvas, text='Espresso', bg='#bf8040', command=self.espressoFun)
        espressoButton.grid(row=7, column=4)
#drip coffee options
    def dripCoffeeFun(self):
        global typeOfCoffee
        
        typeOfCoffee = 'Drip Coffee'

        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif') 
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text='Please review the descriptions below and select a drink using the buttons.', bg='#e6ccb3', padx=0.1, pady=0, height=2)
        titleLabel.grid(row=0, column=4, rowspan=1)

        dripChoice = tk.Button(canvas, text='Drip Coffee', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.dripcoffee)
        dripChoice.grid(row=1, column=4)

        dripChoiceLabel = tk.Label(canvas, text="Just regular coffee like you'd get from a machine", bg='#e6ccb3', padx=0.1, pady=0, height=1)
        dripChoiceLabel.grid(row=2, column=4)

        americanoChoice = tk.Button(canvas, text='Americano', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.americano)
        americanoChoice.grid(row=3, column=4)

        americanoLabel = tk.Label(canvas, text="Espresso and Hot Water", bg='#e6ccb3', padx=0.1, pady=0, height=1)
        americanoLabel.grid(row=4, column=4)

        pourOverChoice = tk.Button(canvas, text="Pour Over", bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.pourover)
        pourOverChoice.grid(row=5, column=4)

        pourOverLabel = tk.Label(canvas, text="Boiling water poured over coffee grounds for a fresher cup.", bg='#e6ccb3', padx=0.1, pady=0, height=1)
        pourOverLabel.grid(row=6, column=4)

        coldbrewChoice = tk.Button(canvas, text="Cold Brew", bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.coldbrew)
        coldbrewChoice.grid(row=7, column=4)

        coldbrewLabel = tk.Label(canvas, text="Like drip coffee but it has steeped longer and at a colder temperature making it stronger.", bg='#e6ccb3', padx=0.1, pady=0, height=1)
        coldbrewLabel.grid(row=8, column=4)

        forward = tk.Button(canvas, text='Next', bg='#e6ccb3', command=self.milk)
        forward.grid(row=9, column=4)

#latte options
    def latteFun(self):
        global typeOfCoffee

        typeOfCoffee = 'Latte'

        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif')
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text='Please review the descriptions below and select a drink using the buttons.', bg='#e6ccb3', padx=0.1, pady=0, height=2)
        titleLabel.grid(row=0, column=4, rowspan=1)

        latteChoice = tk.Button(canvas, text='Latte', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.latte)
        latteChoice.grid(row=1, column=4)

        latteLabel = tk.Label(canvas, text="Espresso and Steamed Milk", bg='#e6ccb3', padx=0.1, pady=0, height=1)
        latteLabel.grid(row=2, column=4)

        cappuccinoChoice = tk.Button(canvas, text='Cappuccino', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.cappuccino)
        cappuccinoChoice.grid(row=3, column=4)

        cappuccinoLabel = tk.Label(canvas, text="Espresso and Foamed Milk", bg='#e6ccb3', padx=0.1, pady=0, height=1)
        cappuccinoLabel.grid(row=4, column=4)

        forward = tk.Button(canvas, text='Next', bg='#e6ccb3', command=self.milk)
        forward.grid(row=9, column=4)

#mocha options
    def mochaFun(self):
        global typeOfCoffee

        typeOfCoffee = 'Mocha'

        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif')
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text='Please review the descriptions below and select a drink using the buttons.', bg='#e6ccb3', padx=0.1, pady=0, height=2)
        titleLabel.grid(row=0, column=4, rowspan=1)

        mochaChoice = tk.Button(canvas, text='Mocha', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.mocha)
        mochaChoice.grid(row=1, column=4)

        mochaLabel = tk.Label(canvas, text="Drip Coffee with Chocolate Syrup", bg='#e6ccb3', padx=0.1, pady=0, height=1)
        mochaLabel.grid(row=2, column=4)

        chocflorChoice = tk.Button(canvas, text='Chocolate Florentine', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.chocflor)
        chocflorChoice.grid(row=3, column=4)

        chocflorLabel = tk.Label(canvas, text="Cold Brew Coffee with Chocolate Syrup", bg='#e6ccb3', padx=0.1, pady=0, height=1)
        chocflorLabel.grid(row=4, column=4)

        forward = tk.Button(canvas, text='Next', bg='#e6ccb3', command=self.milk)
        forward.grid(row=9, column=4)
#espresso options
    def espressoFun(self):
        global typeOfCoffee

        typeOfCoffee = 'Espresso'

        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=10, row=0, rowspan=10)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=9, row=0, rowspan=9)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif')
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text='Please Select the type of milk you would like in your coffee, if any.', bg='#e6ccb3', padx=0.1, pady=0, height=2)
        titleLabel.grid(row=0, column=4, rowspan=1)

        espressoChoice = tk.Button(canvas, text='Espresso', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.espresso)
        espressoChoice.grid(row=1, column=4)

        espressoLabel = tk.Label(canvas, text='finely ground coffee with special beans and less water. A much more concentrated form of coffee', bg='#e6ccb3', padx=0.1, pady=0, height=2)
        espressoLabel.grid(row=2, column=4)

        forward = tk.Button(canvas, text='Next', bg='#e6ccb3', command=self.milk)
        forward.grid(row=9, column=4)
#entries for each option which will be added to the summary page
    def americano(self):
        global drinkChoice
        drinkChoice = 'Americano'
        global drinkCost
        drinkCost += 3.99
    def dripcoffee(self):
        global drinkChoice
        drinkChoice = 'Drip Coffee'
        global drinkCost
        drinkCost += 3.99
    def pourover(self):
        global drinkChoice
        drinkChoice = 'Pour Over'
        global drinkCost
        drinkCost += 3.99
    def coldbrew(self):
        global drinkChoice
        drinkChoice = 'Cold Brew'
        global drinkCost
        drinkCost += 3.99
    def latte(self):
        global drinkChoice
        drinkChoice = 'Latte'
        global drinkCost
        drinkCost += 2.99
    def cappuccino(self):
        global drinkChoice
        drinkChoice = 'Cappuccino'
        global drinkCost
        drinkCost += 3.99
    def mocha(self):
        global drinkChoice
        drinkChoice = 'Mocha'
        global drinkCost
        drinkCost += 4.99
    def chocflor(self):
        global drinkChoice
        drinkChoice = 'Chocolate Florentine'
        global drinkCost
        drinkCost += 3.99
    def espresso(self):
        global drinkChoice
        drinkChoice = 'Espresso'
        global drinkCost
        drinkCost += 1.99
    #milk option page
    def milk(self):
        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        titleLabel = tk.Label(canvas, text='Please Select the type of milk you would like in your coffee, if any.', bg='#e6ccb3', padx=0.1, pady=0, height=2)
        titleLabel.grid(row=0, column=4, rowspan=1)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif') 
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        dairyChoice = tk.Button(canvas, text='Dairy', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.dairy)
        dairyChoice.grid(row=1, column=4)

        nondairyChoice = tk.Button(canvas, text='Non-Dairy', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.nondairy)
        nondairyChoice.grid(row=2, column=4)

        nomilkChoice = tk.Button(canvas, text='No Milk', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.black)
        nomilkChoice.grid(row=3, column=4)

        forward = tk.Button(canvas, text='Next', bg='#e6ccb3', command=self.syrups)
        forward.grid(row=9, column=4)
    #dairy options
    def dairy(self):
        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif') 
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text='Please Select the type of milk you would like in your coffee.', bg='#e6ccb3', padx=0.1, pady=0, height=2)
        titleLabel.grid(row=0, column=4, rowspan=1)

        oneChoice = tk.Button(canvas, text='1% Milk', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.onepercent)
        oneChoice.grid(row=1, column=4)

        twoChoice = tk.Button(canvas, text='2% Milk', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.twopercent)
        twoChoice.grid(row=2, column=4)

        wholeChoice = tk.Button(canvas, text='Whole Milk', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.whole)
        wholeChoice.grid(row=3, column=4)

        forward = tk.Button(canvas, text='Next', bg='#e6ccb3', command=self.syrups)
        forward.grid(row=9, column=4)
#non dairy options
    def nondairy(self):
        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif') 
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text='Please Select the type of milk you would like in your coffee.', bg='#e6ccb3', padx=0.1, pady=0, height=2)
        titleLabel.grid(row=0, column=4, rowspan=1)

        oatChoice = tk.Button(canvas, text='Oat Milk', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.oat)
        oatChoice.grid(row=1, column=4)

        almondChoice = tk.Button(canvas, text='Almond Milk', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.almond)
        almondChoice.grid(row=2, column=4)

        soyChoice = tk.Button(canvas, text='Soy Milk', bg='#e6ccb3', padx=0.1, pady=0, height=2, command=self.soy)
        soyChoice.grid(row=3, column=4)

        forward = tk.Button(canvas, text='Next', bg='#e6ccb3', command=self.syrups)
        forward.grid(row=9, column=4)
#list of options that will be added to summary
    def black(self):
        global milkChoice
        milkChoice = 'no'
    def onepercent(self):
        global milkChoice
        milkChoice = '1%'
    def twopercent(self):
        global milkChoice
        milkChoice = '2%'
    def whole(self):
        global milkChoice
        milkChoice = 'Whole'
    def oat(self):
        global milkChoice
        milkChoice = 'Oat'
    def almond(self):
        global milkChoice
        milkChoice = 'Almond'
    def soy(self):
        global milkChoice
        milkChoice = 'Soy'
#page for selecting syrups
    def syrups(self):

        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif')
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text="Please select the type of syrup you'd like in your drink, if any.", bg='#bf8040')
        titleLabel.grid(row=0, column=4)

        simpleButton = tk.Button(canvas, text = 'Simple Syrup', bg='#bf8040', command=self.simple)
        simpleButton.grid(row=1, column=4)

        lavenderButton = tk.Button(canvas, text = 'Lavender Syrup', bg='#bf8040', command=self.lavender)
        lavenderButton.grid(row=2, column=4)

        caramelButton = tk.Button(canvas, text='Caramel', bg='#bf8040', command=self.caramel)
        caramelButton.grid(row=3, column=4)

        mintButton = tk.Button(canvas, text='Mint', bg='#bf8040', command=self.mint)
        mintButton.grid(row=4, column=4)

        agaveButton = tk.Button(canvas, text='Agave', bg='#bf8040', command=self.agave)
        agaveButton.grid(row=5, column=4)

        honeyButton = tk.Button(canvas, text='Honey', bg='#bf8040', command=self.honey)
        honeyButton.grid(row=6, column=4)

        noneButton = tk.Button(canvas, text='No Syrup', bg='#bf8040', command=self.none)
        noneButton.grid(row=7, column=4)

        forward = tk.Button(canvas, text='Next', bg='#e6ccb3', command=self.espresso)
        forward.grid(row=9, column=4)
#the vairous syrup options that wil be added to the summary
    def simple(self):
        global syrupChoice
        syrupChoice = 'Simple'
    def lavender(self):
        global syrupChoice
        syrupChoice = 'Lavender'
    def caramel(self):
        global syrupChoice
        syrupChoice = 'Caramel'
    def mint(self):
        global syrupChoice
        syrupChoice = 'Mint'
    def agave(self):
        global syrupChoice
        syrupChoice = 'Agave'
    def honey(self):
        global syrupChocie
        syrupChoice = 'Honey'
    def none(self):
        global syrupChoice
        syrupChoice = 'no'
#espresso add in page
    def espresso(self):
        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif') 
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text="Are you feeling tired?", bg='#bf8040')
        titleLabel.grid(row=0, column=4)

        yesButton = tk.Button(canvas, text = 'Yes', bg='#bf8040', command=self.yes)
        yesButton.grid(row=1, column=4)

        noButton = tk.Button(canvas, text = 'No', bg='#bf8040', command=self.no)
        noButton.grid(row=2, column=4)

        forwardButton = tk.Button(canvas, text='Next', bg='#bf8040', command=self.summary)
        forwardButton.grid(row=5, column=4)
#the page that will run if the client selects yes
    def yes(self):
        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif') 
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)

        titleLabel = tk.Label(canvas, text="We reccomend you add some espresso for extra energy.", bg='#e6ccb3')
        titleLabel.grid(row=0, column=4)

        self.shotCount = tk.StringVar()
        shotCounter = tk.Entry(canvas, text = 'Enter how shots you would like below.', bg='#e6ccb3', textvariable = self.shotCount)
        shotCounter.grid(row=3, column=4)

        shotLabel = tk.Label(canvas, text="Enter how many shots you would like in the box above.", bg='#e6ccb3')
        shotLabel.grid(row=4, column=4)

        enter = tk.Button(canvas, text="Enter", bg='#bf8040', command=self.espressoShotValue)
        enter.grid(row=5, column=4)

        nextButton = tk.Button(canvas, text="Next", bg='#bf8040')
        nextButton.configure(command=self.summary)
        nextButton.grid(row=6, column=4)
#gets the amount of shots added in
    def espressoShotValue(self):
        global espressoShot
        espressoShot = self.shotCount.get()

        global drinkCost
        drinkCost += 0.49
#puts the espresso count to 0
    def no(self):
        global espressoShot
        espressoShot = '0'
#summary page with data validation check
    def summary(self):
        
        

        canvas = tk.Canvas(root, height=700, width=800, bg='#bf8040')
        canvas.grid(column=2, columnspan=15, row=0, rowspan=15)

        frame = tk.Frame(canvas, height=700, width=800, bg='#bf8040')
        frame.grid(column=2, columnspan=15, row=0, rowspan=15)

        self.photo = tk.PhotoImage(file=r'/Users/janickolay/Desktop/Spring 2021/INSC 30833/Common Grounds/CG Logo.gif') 
        tk.Label(canvas, image=self.photo, height=50, width=50, anchor='center').grid(row = 0, column = 3)
       
        if drinkChoice == '' or syrupChoice == '' or milkChoice == '':
            titleLabel = tk.Label(canvas, text=('It looks like you forgot select all options. Please close and reopen the app to get a complete reccomendation.'), bg='#e6ccb3')
            titleLabel.grid(row=0, column=4)
        
        else:
            titleLabel = tk.Label(canvas, text=("""You're drink recomendation is as follows. You would like a %s with %s milk and %s syrup.""" % (drinkChoice, milkChoice, syrupChoice)), bg='#e6ccb3')
            titleLabel.grid(row=0, column=4)

            titleLabeltwo = tk.Label(canvas, text=("""You also said you wanted %s shot(s) of espresso added.""" % (espressoShot)), bg='#e6ccb3')
            titleLabeltwo.grid(row=1, column=4)

            titleLabelthree = tk.Label(canvas, text=("""Your order will cost $%.2f""" % (drinkCost)), bg='#e6ccb3')
            titleLabelthree.grid(row=2, column=4)

Common_Grounds()

root.mainloop()