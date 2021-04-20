print('Hello. Welcome to the Common Groundsffff Reccomendation App.\n')
print()

#the first part is just a dictionaries and lists used to get inputs

coffeeTypes = ['Drip Coffee', 'Latte', 'Mocha', 'Espresso']

dripCoffee = {
    'Americano': 'Simply Espresso and Water',
    'Drip Coffee': 'Like you would get from a coffee maker at home', 
    'Pour Over': 'Boiling water poured over coffee grounds for the freshest coffee.',
    'Cold Brew':'Drip coffee that has been steeping in cold coffee grounds for more time, making it a stronger brew.'
}

checkDrink = ['Americano', 'Drip Coffee', 'Pour Over', 'Cold Brew','Latte', 'Cappuccino', 'Standard Mocha', 'Chocolate Florentine', 'Espresso']

latte = {
    'Latte': 'Espresso and steamed milk', 
    'Cappuccino': 'Espresso and foamed milk'
}

mocha = {
    'Standard Mocha': 'Drip Coffee with Chocolate Syrup',
    'Chocolate Florentine': 'Cold Brew Coffee with Chocolate Syrup'
}

espresso = {
    'Espresso': 'Finely ground coffee with special beans and less water making it much more concentrated.'
}


milkOptions = ['Dairy', 'Non-Dairy', 'Black']

milk = ['1%', '2%', 'Whole' ]

nonDairy = ['Oat', 'Soy', 'Almond']

milkCheck = ['1%', '2%', 'Whole', 'Oat', 'Soy', 'Almond', 'no']

sweetener = [
    'Simple Syrup', 
    'Lavender', 
    'Caramel', 
    'Mint', 
    'Agave', 
    'Honey',
    'no flavoring'
]


#this is where we start the input process, the first one is for type of drink

typeOfCoffee = input('''
What kind of coffee sounds good to you today? The options are listed below.\n
Drip Coffee
Latte
Mocha
Espresso
\n''')

print()

#validates entry for drink type

while typeOfCoffee not in coffeeTypes:
    typeOfCoffee = input("It looks like you didn't enter a valid type of Coffee.\nPlease try and again.\nMake sure to use the same capitilization and spelling for you entry\n")

#this will return the options for the selected drink type



def coffeeSelection(typeOfCoffee):
    if typeOfCoffee == 'Drip Coffee':
        x = dripCoffee
    if typeOfCoffee == 'Latte':
        x = latte
    if typeOfCoffee == 'Mocha':
        x = mocha
    if typeOfCoffee == 'Espresso':
        x = espresso
    for key,val in x.items():
        print (key, ":", val)
    print()
    return 'Please review the options above and make a selection.'

print("You selected %s.\n\nYou'll find a list of choices and despriptions below." % (typeOfCoffee))

print()

print(coffeeSelection(typeOfCoffee))

print()
#this registers the actual drink they want

drinkChoice = input("Enter your choice here:\n")

while drinkChoice not in checkDrink:
    drinkChoice = input('It looks like you made an invalid entry.\nPlease try again.\n')

#This determines if they want dairy, non-dairy, or black

lactoseChoice = input('''
Would you like milk or a dairy-free alternative in your drink? 
If you prefer no milk, just enter 'Black'.
Please enter your choice from the options below.

Dairy
Non-Dairy
Black

''')

while lactoseChoice not in milkOptions:
    lactoseChoice = input("It looks like you didn't enter a valid choice.\nPlease make sure you use the same formatting as the options.\n")

def milkPicker(lactoseChoice):
    if lactoseChoice == 'Dairy':
        for x in range(len(milk)):
            print (milk[x])
    if lactoseChoice == 'Non-Dairy':
        for x in range(len(nonDairy)):
            print (nonDairy[x])
    if lactoseChoice == 'Black':
        print('No milk then, sounds good!')
    return ''

print()
print(milkPicker(lactoseChoice))
print()

milkChoice = ''

if lactoseChoice == 'Dairy' or lactoseChoice == 'Non-Dairy':
    milkChoice = input("Please select the milk you'd like in your coffee.\n")
if lactoseChoice == 'Black':
    milkChoice = 'no'


while milkChoice not in milkCheck:
    milkChoice = input('It looks like you did not enter you selection correctly.\nPlease use the same formatting as the option menu for you entry.')

syrup = input('''
Would you like a flavor added to your drink?\nYour options are listed below.\nIf you wouldn't like any, just enter "no flavoring".

Simple Syrup
Lavender Syrup 
Caramel 
Mint 
Agave
Honey 

''')

while syrup not in sweetener:
    syrup = input('It looks like you did not enter you selection correctly.\nPlease use the same formatting as the option menu for you entry.')

tired = input('Are you feeling tired?\n')

espressoAddIn = 'fuck'

def espressoOption(tired):
    
    global espressoAddIn
    
    if tired == 'Yes':
        espressoAddIn = input('You should add espresso to your drink\nPlease enter how many shots of espresso you want to add.\n')
    if tired == 'No':
        espressoAddIn = '0'
    return ''

print(espressoOption(tired))

summary = """
Please find your order below. 
You would like a %s with %s milk and %s. You also said you wanted %s shot(s) of espresso added.
Tell this order to your barista.
""" % (drinkChoice, milkChoice, syrup, espressoAddIn)

print(summary)

