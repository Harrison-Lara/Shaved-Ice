########################################################################
##
## CS 101
## Program # 2
## Name: Harrison Lara
## Email: hrlwwd@mail.umkc.edu
##
## PROBLEM :
##    In this assignment we will simulate owning a Shave Ice stand for the user.
## The simulation will  take place over 10 days. On each day the weather will 
## be randomly created and user will decide how many shave ices to prepare 
## in advance of the day's customers. Make too many and get too few customers
## will lose money. Make too few of them and you may sell everything you make,
## but  lose out on potential sales.  The number of customers will be greater 
## on hot days and lower on  cool days or days when it is raining.
##
## ALGORITHM:
##   1.	Greet the user ‘Welcome to the Shaved Ice Ten Day Simulator’
##   2.	Set the bank account to $5 for Day 1
##   3.	Set cost of each cone to .50
##   4.	Tell the user what day it is and how much money they have in the bank ($5)
##   5.	Tell the user what the weather is per day (clear or rainy) and the temperature
##      import random  
##      random.randint()
##      if value <=10: 
##      print(" Rainy ")  
##      else:  
##      print("Clear")
##
##      random.randint( 70, 110)
##
##   6.	Ask the user to input price per cone > = .50 (repeat step 6 if not over .50)
##   7.	Ask the user how many cones they want to make for day (0, 1, 2, 3, …)
##   8.	Prompt must enter a value >=0, enter value again
##   9.	Prompt user you don’t have enough money to make this many cones. Enter new value (repeat step 7)
##  10.	Determine the number of customers that came per day with the formula: 
##      maxcustomers = (temperature -70) * 0.5 / cup price (round down)
##      if it is raining, divide the max customers by 2 (round down)
##  11.	Calculate the number of cones sold according to number of max customers 
##  12.	Prompt user ‘you sold # cones today and cost a total of $#.##’
##  13.	Calculate the amount of profit or loss with the (amount sold * price) – cost 
##  14.	Prompt user ‘you have a profit or loss of (-)$0.00
##  15.	If bank account hits $0.00, end simulation and jump to Step 19
##  16.	If not Step 15, loop back to Step 4 until Step 15 occurs.
##  17.	For each new day, state the day and amount of profit in bank. 
##  18.	Calculate new bank amount by taking previous day bank amount and adding profit/ loss to it. 
##  19.	At the end of day 10 or Step 15 occurs, prompt user ‘End of simulation, do you want to play again? Yes or no’
##  20.	If not a valid response, you must choose ‘Yes or No’ 
##  21.	Repeat Step 19 
##  22.	If Yes is chosen, go back to Step 1, if No, prompt user ‘Thank you for playing the ‘Shaved Ice Ten Day Simulator”
##  23.	End Program
## 
## ERROR HANDLING:
##          Space or symbols in place of a number for input.
##
## OTHER COMMENTS:
##                None
##
########################################################################

#Greeting
print('Welcome to the Shaved Ice Ten Day Simulator') #greet user
print (' ')#line break

#Set users conditions
account = 5 #$5 in bank
cone_cost = .5 #set cost per cone
day = 1 #start at day 1
end = 0 #variable for end of day inputs
import random #random numbers for later on
simulating = True #creating overall loop
while simulating == True:#while this holds True, keep loop going
    
#Inform User
    start_day = print('Day',day,', you have $',account,'in your wallet')  #Tell user what day and how much you have
    temperature = random.randint(70, 110)  #calculate the temperature
    weather = random.randint(0,100)   #calculate the weather
    if weather <=10:
        weather = 'rainy'
    else:
        weather= 'nice and sunny'
    print('Theres a lovely temperature of',temperature,'degrees outside and it is', weather) #tell user what the weather and temperature is like

#User Input
    cone_price = float(input('Hey bro, how much is one of those colorful cones?')) #ask user how much each cone will be
    while cone_price <.5:
        print('You must enter a price of at least .50 cents') #invalid input
        cone_price = float(input('Ah good try, but really man what will be the price per cone?')) #asking for input again
        
    amount = int(input('Ok, lets get this baby rockin, how many cones are we making today boss?')) #ask user how many cones to make
    while amount < 0:
        amount= int(input('Trickster I see, how many cones should we be making for the day?')) #invalid input
    while amount * .5 >= account:
        print('Sorry bro, your wallet is looking a little low for that many') #asking for new input
        amount = int(input('How many cones do you want to make today?'))

#Calculations
    customers = (temperature - 70)*0.5/cone_price #calculating amount of max consumers
    if weather is 'rainy':
        rainy_customers= customers/2 #if it rains, divide the max consumers by two
    else:
         customers= customers #if not rainy, max consumers stays the same
         
    cost = amount*.5 #set cost per cone
    print(' ') #line break
    if customers > amount:
        print('Nice bruh! You sold', amount,'cones and it cost you $',cost) #tell user how many cones were sold and the cost based on condition
    elif customers < amount:
        print('Nice bruh! You sold', customers,'cones and it cost you $',cost)
    else:
        print('Nice bruh! You sold', amount,'cones and it cost you $',cost)

#End of day
    profit_loss = (amount*cone_price)-cost #calculate profit/loss made this day based on condition
    if profit_loss > 0:
        account = profit_loss + account
        print('With a profit/loss of $',profit_loss)
    elif profit_loss < 0:
        account = profit_loss - account
        print('With a profit/loss of $',profit_loss)
    else:
        account =  0 + account
        print('With a profit/loss of $',profit_loss)
    
    day+=1 #transistion to next day, day 1 to day 2 to day 3...
    print(' ')#line break
    
#end simulation or start over 
    if account <= 0 or day >=11:#end day if you have $0 or day ten is finished
        print('Bro! You made some serious bank. You made a total of $',account) #tell user amount they made after ten days
        while True:
            end= input('End of Simulation. Do you wish to play again, yes or no?') #end simulation and ask user if they want to restart the game or end it
            if end.lower()== 'yes':
                account= account+ 5
                break #restart the game
            elif end.lower()=='no':
                print('Have a great day!') #thanks for playing and end simulation 
                exit()
            else:
                print ('Try again')
                continue #invalid input, ask again
