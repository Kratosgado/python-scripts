"""
This is a class that stores weapons in and allows users to add or remove weapons from it.
It can be used in games or even apps

class inventory:
    add
    remove
    display
    save
    load

class main:
    instancing the  inventory class and calling it to run
"""

#import os and json
#will be used to save and load files
import os
import json

#create the inventory class
class inventory:
    #create a dictionary named weapon that will store the weapons
    weapons = {}

    #create a constructor that loads the inventory on startup
    def __init__(self) -> None:
        self.load()

    #create addition function
    def add(self, wp, amt):
        qty = 0
        #check if the weapon is in the inventory and add the amount
        if wp in self.weapons:
            qty = self.weapons[wp]
            qty += amt
        else:
            qty = amt
        self.weapons[wp] = qty
        print(f'You added {amt} to {wp} \n {wp} is now {qty} ')
        
    #create the function to remove weapons
    '''
    there's a bug here in the rem() function , can you fix it? 
    figure the bug out by running the code and trying possible inputs with the 
    rem() function and fix it. thank you
    '''
    def rem(self, wp, amt):
        if wp in self.weapons:
            qty = self.weapons[wp]
            qty -= amt
            self.weapons[wp] = qty
            print(f'You removed {amt} from {wp} \n You now have {qty} of {wp} left ')
        else:
            print(f'You don\'t have {wp} in your inventory')

    #function to display weapons that has been stored in the inventory
    def list(self):
        #loop through the weapons list and print them
        for k,v in self.weapons.items():
            print(f'{k} = {v} ')
    
    #function to save changes made to inventory
    def save(self):
        print('saving file...')
        #open an inventory file in write mode and use json to save it
        with open('inventory.txt', 'w') as filename:
            #json's dump method writes self.weapons to inventory.txt
            json.dump(self.weapons,  filename)
        print('file saved')

    #function to load the inventory
    def load(self):
        print('loading...')
        filename = 'inventory.txt'
        #check if filename exists and open it
        if os.path.exists(filename):
            with open(filename) as file:
                #json's load method loads and opens the inventory.txt
                json.load(file)
            
            print('file loaded')
        #if there's no file to load,  run this
        else:
            print('Sorry!!! \n There is no file to load')

#main class that will instance the inventory class and control our code
class main:
    #instancing the class
    invent = inventory()
    #use a while loop to prevent a sudden crash when the user enters a wrong command
    while True:
        #recieve command
        cmd = input('Enter command: add, rem, list, save, load, exit: ')

        #check command  and run corresponding inventory function
        if cmd == 'add' or cmd == 'rem':
            wp = input('name of weapon: ')
            amt = int(input('amount: '))

            if cmd == 'add':
                invent.add(wp, amt)
            
            if cmd == 'rem':
                invent.rem(wp, amt)

        if cmd == 'list':
            invent.list()
        
        if cmd == 'save':
            invent.save()

        if cmd == 'load':
            invent.load()
        
        if cmd == 'exit':
            invent.save()
            break

#run the main class
if __name__ == "__main__":
    main()