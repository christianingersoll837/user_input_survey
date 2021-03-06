print()
print("                        IS THE LOTTERY FOR YOU")
# Welcome to the Is The Lottery For Me assesment survey
print()
print("That's the question we are going to pose to you over the course of this survey.")
print()

dream = input("Have you ever wondered what you would do with a massive lottery jackpot\ny/n?:")
if dream == 'y':
    print(f"That's definitely something we've all thought about.")
else:
    print(f"                                 WoW!\nYou must already be in the top 5% of the population that holds 95% of the world's wealth.\nIt's not that often that we see someone who's never imagined a lottery windfall.\nHowever, technically because you have already started taking this survey,\nyou can no longer say you've never wondered.")
print()
dollar = int(input("So, tell us how much would the jackpot have to be in order for it to be considered life changing money\n(PLEASE USE INTEGERS FOR YOUR INPUT)?\n$"))
if dollar > 100000000:
    print(f"OK, now we both know that ${dollar} is alot of money.\nFor the sake of this survey let's use $100,000,000 as our benchmark for a windfall jackpot.")
else:
    print(f"Let's start thinking big and use $100000000 as our benchmark for a windfall jackpot.")
print()
dollar = 100000000
print(f"Now that we know that ${dollar} is what we will fantasize about in this survey,\nlet's figure out how big of a hit we will take on taxes.")
print()
state_tax = input("Only certain states take taxes from lottery winners.\nSo what state do you live in?\n(PLEASE MAKE SURE YOU SPELL THE STATE CORRECTLY):")
state_tax_upper = state_tax.upper()
if state_tax_upper == 'NEW YORK':
    print(f"We know that {state_tax_upper} state takes the most out in taxes from lottery winnings.\n{state_tax_upper} has a tax rate of 8.82% on lottery jackpot winnings.")
elif state_tax_upper == 'MARYLAND':
    print(f"We know that {state_tax_upper} state takes the second most out in taxes from lottery winnings.\n{state_tax_upper} has a tax rate of 8.75% on lottery jackpot winnings.")
elif state_tax_upper == 'OREGON':
    print(f"We know that {state_tax_upper} state is tied for third\nas the state that takes the third most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 8.00% on lottery jackpot winnings.")
elif state_tax_upper == 'NEW JERSEY':
    print(f"We know that {state_tax_upper} state is tied for third\nas the state that takes the third most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 8.00% on lottery jackpot winnings.")
elif state_tax_upper == 'WISCONSIN':
    print(f"We know that {state_tax_upper} state has the fourth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 7.65% on lottery jackpot winnings.")
elif state_tax_upper == 'MINNESOTA':
    print(f"We know that {state_tax_upper} state has the fifth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 7.25% on lottery jackpot winnings.")
elif state_tax_upper == 'SOUTH CAROLINA':
    print(f"We know that {state_tax_upper} state is tied for sixth\nas the state that takes the sixth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 7.00% on lottery jackpot winnings.")
elif state_tax_upper == 'ARKANSAS':
    print(f"We know that {state_tax_upper} state is tied for sixth\nas the state that takes the sixth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 7.00% on lottery jackpot winnings.")
elif state_tax_upper == 'CONNECTICUT':
    print(f"We know that {state_tax_upper} state has the seventh highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 6.99% on lottery jackpot winnings.")
elif state_tax_upper == 'IDAHO':
    print(f"We know that {state_tax_upper} state has the eighth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 6.92% on lottery jackpot winnings.")
elif state_tax_upper == 'MONTANA':
    print(f"We know that {state_tax_upper} state has the ninth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 6.90% on lottery jackpot winnings.")
elif state_tax_upper == 'WEST VIRGINIA':
    print(f"We know that {state_tax_upper} state has the tenth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 6.50% on lottery jackpot winnings.")
elif state_tax_upper == 'VERMONT':
    print(f"We know that {state_tax_upper} state is tied for eleventh\nas the state that takes the eleventh most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 6.00% on lottery jackpot winnings.")
elif state_tax_upper == 'NEW MEXICO':
    print(f"We know that {state_tax_upper} state is tied for eleventh\nas the state that takes the eleventh most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 6.00% on lottery jackpot winnings.")
elif state_tax_upper == 'RHODE ISLAND':
    print(f"We know that {state_tax_upper} state has the twelfth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 5.99% on lottery jackpot winnings.")
elif state_tax_upper == 'GEORGIA':
    print(f"We know that {state_tax_upper} state has the thirteenth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 5.75% on lottery jackpot winnings.")
elif state_tax_upper == 'NORTH CAROLINA':
    print(f"We know that {state_tax_upper} state has the fourteenth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 5.50% on lottery jackpot winnings.")
elif state_tax_upper == 'NEBRASKA':
    print(f"We know that {state_tax_upper} state is tied for fifteenth\nas the state that takes the fifteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 5.00% on lottery jackpot winnings.")
elif state_tax_upper ==  'MASSACHUSETTS':
    print(f"We know that {state_tax_upper} state is tied for fifteenth\nas the state that takes the fifteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 5.00% on lottery jackpot winnings.")
elif state_tax_upper == 'MAINE':
    print(f"We know that {state_tax_upper} state is tied for fifteenth\nas the state that takes the fifteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 5.00% on lottery jackpot winnings.")
elif state_tax_upper == 'LOUISIANA':
    print(f"We know that {state_tax_upper} state is tied for fifteenth\nas the state that takes the fifteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 5.00% on lottery jackpot winnings.")
elif state_tax_upper == 'KENTUCKY':
     print(f"We know that {state_tax_upper} state is tied for fifteenth\nas the state that takes the fifteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 5.00% on lottery jackpot winnings.")
elif state_tax_upper == 'KANSAS':
    print(f"We know that {state_tax_upper} state is tied for fifteenth\nas the state that takes the fifteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 5.00% on lottery jackpot winnings.")
elif state_tax_upper == 'IOWA':
    print(f"We know that {state_tax_upper} state is tied for fifteenth\nas the state that takes the fifteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 5.00% on lottery jackpot winnings.")
elif state_tax_upper == 'ARIZONA':
    print(f"We know that {state_tax_upper} state is tied for fifteenth\nas the state that takes the fifteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 5.00% on lottery jackpot winnings.")
elif state_tax_upper == 'ILLINOIS':
    print(f"We know that {state_tax_upper} state has the sixteenth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 4.95% on lottery jackpot winnings.")
elif state_tax_upper == 'MICHIGAN':
    print(f"We know that {state_tax_upper} state has the seventeenth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 4.25% on lottery jackpot winnings.")
elif state_tax_upper == 'VIRGINIA':
    print(f"We know that {state_tax_upper} state is tied for eighteenth\nas the state that takes the eighteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 4.00% on lottery jackpot winnings.")
elif state_tax_upper == 'OKLAHOMA':
    print(f"We know that {state_tax_upper} state is tied for eighteenth\nas the state that takes the eighteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 4.00% on lottery jackpot winnings.")
elif state_tax_upper == 'OHIO':
    print(f"We know that {state_tax_upper} state is tied for eighteenth\nas the state that takes the eighteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 4.00% on lottery jackpot winnings.")
elif state_tax_upper == 'MISSOURI':
    print(f"We know that {state_tax_upper} state is tied for eighteenth\nas the state that takes the eighteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 4.00% on lottery jackpot winnings.")
elif state_tax_upper == 'COLORADO':
    print(f"We know that {state_tax_upper} state is tied for eighteenth\nas the state that takes the eighteenth most out in taxes from lottery winnings.\n{state_tax_upper} state has a tax rate of 4.00% on lottery jackpot winnings.")
elif state_tax_upper == 'INDIANA':
     print(f"We know that {state_tax_upper} state has the nineteenth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 3.23% on lottery jackpot winnings.")
elif state_tax_upper == 'PENNSYLVANIA':
     print(f"We know that {state_tax_upper} state has the twentieth highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 3.07% on lottery jackpot winnings.")
elif state_tax_upper == 'NORTH DAKOTA':
     print(f"We know that {state_tax_upper} state has the twentyfirst highest tax rate on lottery winnings.\n{state_tax_upper} state has a tax rate of 2.90% on lottery jackpot winnings.")
else:
    print(f"We know that {state_tax_upper} state has no tax on lottery winnings")
print()
print("Ok, now we know your state tax rates")
fed_tax_rate = input("Do you know what the federal tax rate is on lottery jackpot winnings\ny/n:")
if fed_tax_rate == 'y':
    print("Great, you know the federal tax rate on lottery winnings is 24%.")
elif fed_tax_rate == 'n':
    print("You would never believe it but the Federal tax rate on lottery winnings is 24%.") 
print()
state_taxes = input("Based on the current tax rates on lottery winnings in your state.\nWhat is the tax rate in your state\n(MAKE SURE YOU INPUT THE FLOAT FOR YOUR STATE ONLY): ")
 
federal_taxes = input("Now just to make sure we are following along,\nwhat is the federal tax rate for lottery jackpot winnings: ")

sum = int(state_taxes) + int(federal_taxes) 
  
# Display the sum 
# will print value in float 
print("The total taxes to be taken out are roughly {0}% state and {1}% federal for a total of\njust about {2}% in taxes " .format(state_taxes, federal_taxes, sum))

total_taxes = 1000000000//(sum)
print(f"The total tax withholdings are ${total_taxes}")

after_taxes = 100000000-total_taxes
print(f"The grand total winnings after taxes are ${after_taxes}")
first_purchase = input(f"Here we are with our ${after_taxes}.\nWould you make any major purchases immediatley?y/n:")
if first_purchase == 'y':
    big_buy = input("How much do you think you would spend on that first major purchase\n(MAKE SURE TO INPUT AN INTEGER AMOUNT).$")
    
    purchase_first = input(f"Now that we are going to spend ${big_buy}.\nTell us, what did you just buy?")
    budget_for_life = input(f"So you bought a {purchase_first} and it cost ${big_buy}.\nNow we can safely say you should start a budget.\nTell us how much money would you set aside every year to maintain a comfortable lifestyle?\n(DONT FORGET TO USE INTEGERS)$")
    print(f"Based on this survey we think you will be a great lottery jackpot winner.\nGo get your tickets and good luck Tiger!")


elif first_purchase =='n':
    invest_first = input(f"Great to hear, that is the smartest move!\nHowever, if you're of this mindset the next question is,\nwould you try to grow your money and invest.y/n:")
    if invest_first =='y':
        interest_return = input(f"The average rate of inflation is 2.99%.\nWhat kind of 'Return On Your' investments would you need to make, or more specifically.\nHow much money do you need to earn on your investments every year on your\n${after_taxes} to live comfortably?\n(MAKE SURE YOU USE INTEGERS)$")
        life_savings = input(f"Yes, making ${interest_return} every year sounds like a great idea!\nSome insurance annuities can earn as much as 8-12% interest per annum.\nTherefore an insurance annuity can earn you up to $1,200,000 per year on every\n$10,000,000 invested.\nWould you invest in an insurance annuity?y/n:")
        if life_savings == 'y':
            print(f"Perfect!!!\nAccording to this survey the odds that you would be a great lottery jackpot winner are high.\nYou should probably go out and buy your tickets now,\nyou would be an amazing investor.")
        elif life_savings =='n':
            print("You won't be fooled....\n!!!!SCAMMERS BEWARE!!!!\nThank you for your time taking this survey.\nThe lottery doesnt sound like its for you" )    
    
    
    elif invest_first =='n':
        invest_loop = input(f"Ah ha! You want to budget your ${after_taxes}.This is enough to last all of your life.\nSo if we aren't going to make any major purchases and aren't going invest in anything.\nWhat would your yearly budget be in order to make your money last your lifetime? $")
        looped_invest = input(f"Yep, ${invest_loop} is plenty of money to go around.\nDo the math though and see for yourself.\nYou have ${after_taxes}.\nHow many years can you spend ${invest_loop} before you go broke?:")
        print("It looks likes you're overwhelmed with too many options.\nMaybe it's better if you didn't play the lottery\nPLEASE CALL 1-800-GAMBLNOMORE.")

else:
    print("Sorry for the bugs.\nTry the survey again\nHINT!!!!\n(TRY AND FOLLOW THE INSTRUCTIONS")





