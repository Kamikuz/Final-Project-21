#CS 021
#Team Member: Kamiku Xue | Zhi You Mark Zuo | Haoyuan Pang
#Application Name: Global Tool 

#modules import
import requests
import json
import random
import numpy as np
from sys import exit


def main():
    
	time = Haoyuan_2()
	print("Welcome to the Gloabl Tool Application\nNow it's",time,".\n Please choose the function you want(Enter the number!): ")

	menu = int(input(""))

	if menu == 1:
		Kamiku()
	elif menu == 2:
		Mark()
	elif menu == 3:
		Haoyaun_1()
	else:
		print("Error Choise, try again!")
		app_error = True


#================Kamiku Branch==============
def Kamiku():
	#initialize the status code
	error = False
	stop = False

	# first exception handle
	while error == True or stop == False:
		try:
			#request and get the json of currency list (Chinese Ver.)
			print("Initializing...")
			currency_list_zh = requests.get('https://yxue.w3.uvm.edu/cs021/currency_list_zh.json')
			currency_list_zh = currency_list_zh.json()

			#(English Ver.)
			currency_list_en = requests.get('https://yxue.w3.uvm.edu/cs021/currency_list_en.json')
			currency_list_en = currency_list_en.json()
			error = False

		except:
			error = True
			#API error, try to get again
			print('The api is broken or no connection, try later o(╥﹏╥)o')


		#intro info
		print("\nWelcome to use the currency exchange system!\n")

		#promot the user to choose the language mode
		Pass = False
		while Pass == False:
			try:
				language = int(input('Please choose the Language(请选择语言)[English --> 0 | 简体中文 --> 1]: '))
				Pass = True

				#English Mode
				if language == 0:
					error = False
					Pass = True
					stop = English(currency_list_en)

				#Chinese Mode
				elif language == 1:
					error = False
					Pass = True
					stop = Chinese(currency_list_zh)
	
				else:
					error = True
					print("Choice do not exist, Try Again!\n选择不存在，请重试！")

			except ValueError:
				error = True
				print("Wrong Choose, try again!\n选择错误，请重试！")

def English(x):
	#list the currency and code
	print("\nHere is the code of currency\n----------------------------")
	print("#","CODE","Currency Name",sep='\t|')
	print("----------------------------")
	n = 1
	for item in x['list']:
		print(n,item['code'],item['name'],sep='\t|',end="\n")
		n += 1

	PASS = False
	while not PASS:
		#user input the source currency
		origin_currency = input("----------------------------\nPlease enter the source currency(Code): ")
		#case insensitive
		origin_currency = origin_currency.upper()

		#vailate the input
		while not origin_currency.isalpha() or len(origin_currency)>3:
			origin_currency = input("\nInvalid Code! Try again:")
			origin_currency = origin_currency.upper()

		for i in x['list']:
			if origin_currency == i['code']:
				PASS = True
		
		if not PASS:
			print("\nThe currency does not exist, try again!")

	PASS = False
	while not PASS:
		#user input the convert currency
		target_currency = input("\nPlease enter the target currency you want to convert(Code): ")
		target_currency = target_currency.upper()

		#vailate the input
		while not target_currency.isalpha() or len(target_currency)>3:
			target_currency = input("\nInvalid Code! Try again:")
			target_currency = target_currency.upper()

		for i in x['list']:
			if target_currency == i['code']:
				PASS = True

		if not PASS:
			print("\nThe currency does not exist, try again!")
	
	print("Loading(*￣︶￣)...")

	#call the request fun to get the rate
	RATE = float(request(origin_currency,target_currency))

	#prompt the user to input the amount
	PASS = False
	while not PASS:
		try:
			amount = float(input("\nPlease enter the number you want to convert: "))
			
			while amount <=0.0:
				amount = float(input("\nPlease input the valid amount:"))

			PASS = True
		except ValueError:
			print('Invalid Number,try again!')

	#calculate
	reuslt_amount = amount * RATE

	#call the output function to give the result
	output_en(origin_currency,target_currency,RATE,reuslt_amount,amount)

	STOP = input('Exchange again？(y/n): ')
	STOP = STOP.lower()
	
	if STOP == 'y':
		z = False

	elif STOP == 'n':
		z = True
		print("\nSee you!")
	return z

def Chinese(x):
	#list the currency and code
	print("\n货币列表及其代号\n----------------------------")
	print("序号","代号","货币名称",sep='\t|')
	print("----------------------------")
	n = 1
	for item in x['data']:
		print(n,item['code'],item['name'],sep='\t|',end="\n")
		n += 1

	PASS = False
	while not PASS:
		#user input the source currency
		origin_currency = input("----------------------------\n请输入原货币的代号: ")
		#case insensitive
		origin_currency = origin_currency.upper()

		#validate the input
		while not origin_currency.isalpha() or len(origin_currency)>3:
			origin_currency = input("\n无效代号，请重新输入:")
			origin_currency = origin_currency.upper()

		for i in x['data']:
			if origin_currency == i['code']:
				PASS = True
		
		if not PASS:
			print("\n货币不存在，请重新输入货币代号!")

	PASS = False
	while not PASS:
		#user input the convert currency
		target_currency = input("\n请输入想要转换的货币代号: ")
		target_currency = target_currency.upper()

		#validate the input
		while not target_currency.isalpha() or len(target_currency)>3:
			target_currency = input("\n无效代号，请重新输入:")
			target_currency = target_currency.upper()

		for i in x['data']:
			if target_currency == i['code']:
				PASS = True

		if not PASS:
			print("\n货币不存在，请重新输入货币代号!")
	
	print("稍等(*^▽^*)")

	#call the request fun to get the rate
	RATE = float(request(origin_currency,target_currency))

	#promot the user to input the amount
	PASS = False
	while not PASS:
		try:
			amount = float(input("\n请输入想要转换的货币金额： "))

			while amount <=0.0:
				amount = float(input("\n请输入正确的金额： "))

			PASS = True
		except ValueError:
			print('无效数字，请重试!')

	#calculate
	reuslt_amount = amount * RATE

	#call the output function to give the result
	output_zh(origin_currency,target_currency,RATE,reuslt_amount,amount)

	STOP = input('重新转换？(y/n): ')
	if STOP == 'y':
		z = False

	elif STOP == 'n':
		print("\n再见!")
		z = True
	return z

def request(x,y):
	#import the appid to get the api
	para = {'appid':'01b615dcc108bd15c022160f14627541'}

	#add the para 'from' and 'to'
	para['form'] = x
	para['to'] = y

	#request by using get method
	response = requests.get('https://api.shenjian.io/exchange/currency',para)
	#load the json
	response = response.json()

	#get the key of rate
	z = response['data']['rate']

	#return the data
	return z

#English output
def output_en(a,b,c,d,e):
	#format the data
	d = format(d,'.3f')
	e = format(e,'.3f')

	#print them
	print("--------------Result--------------")
	print("Original Currency:\t",e,a)
	print("\nConvert Currency:\t",d,b)
	print("\nThe rate is:\t",c)
	print("----------------------------------")

#Chinese output
def output_zh(a,b,c,d,e):
	#format the data
	d = format(d,'.3f')
	e = format(e,'.3f')

	#print them
	print("--------------Result--------------")
	print("原货币:\t",e,a)
	print("\n转换货币及金额:\t",d,b)
	print("\n汇率:\t",c)
	print("----------------------------------")

#=====================Mark Branch=====================
def Mark():
    poker_name = ['♦10', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦A', '♦J', '♦K', '♦Q',
                  '♣10', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣A', '♣J', '♣K', '♣Q',
                  '♥10', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥A', '♥J', '♥K', '♥Q',
                  '♠10', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠A', '♠J', '♠K', '♠Q']

    # Set the score for each card according to the name in the deck
    poker_value = {'♣A': 1, '♥A': 1, '♠A': 1, '♦A': 1, '♦10': 10, '♦2': 2, '♦3': 3, '♦4': 4, '♦5': 5, '♦6': 6, '♦7': 7,
                   '♦8': 8, '♦9': 9, '♦J': 10, '♦K': 10, '♦Q': 10,
                   '♣10': 10, '♣2': 2, '♣3': 3, '♣4': 4, '♣5': 5, '♣6': 6, '♣7': 7, '♣8': 8, '♣9': 9, '♣J': 10, '♣K': 10,
                   '♣Q': 10,
                   '♥10': 10, '♥2': 2, '♥3': 3, '♥4': 4, '♥5': 5, '♥6': 6, '♥7': 7, '♥8': 8, '♥9': 9, '♥J': 10, '♥K': 10,
                   '♥Q': 10,
                   '♠10': 10, '♠2': 2, '♠3': 3, '♠4': 4, '♠5': 5, '♠6': 6, '♠7': 7, '♠8': 8, '♠9': 9, '♠J': 10, '♠K': 10,
                   '♠Q': 10}


    # It is used to determine whether there is an A in the hand,
    # and to choose whether the score of A is 10 or 1 based on the score
    Ace = {'♣A', '♥A', '♠A', '♦A'}


    def dealing_poker(poker_database):
        # Deal a card and remove it from the deck
        return poker_database.pop(random.randint(0, len(poker_database) - 1))


    def score_count(hand_poker):
        # Count the number of CARDS
        score = 0
        have_ace = False
        for k in hand_poker:
            score += poker_value[k]
        for i in hand_poker:
            if i in Ace:
                have_ace = True
                break
            else:
                continue
        if have_ace is True:
            if score + 10 <= 21:
                score += 10
        return score


    def judgement(your_score, pc_score):
        # At the end of the card, calculate the number of points on both sides to determine whether to win or lose
        if your_score > 21 and pc_score > 21:
            print('PUSH')
            return np.array([0, 0])
        elif your_score > 21 and pc_score <= 21:
            print('YOU LOSE')
            return np.array([0, 1])
        elif your_score <= 21 and pc_score > 21:
            print('YOU WIN')
            return np.array([1, 0])
        elif your_score <= 21 and pc_score <= 21:
            if your_score < pc_score:
                print('*' * 20)
                print('Your Score:', your_score)
                print("Pc's Score:", pc_score)
                print('*' * 20)
                print('YOU LOSE')
                return np.array([0, 1])
            elif your_score > pc_score:
                print('*' * 20)
                print('Your Score:', your_score)
                print("Pc's Score:", pc_score)
                print('*' * 20)
                print('YOU WIN')
                return np.array([1, 0])
            else:
                print('*' * 20)
                print('Your Score:', your_score)
                print("Pc's Score:", pc_score)
                print('*' * 20)
                print('PUSH')
                return np.array([0, 0])


    def hit_or_stand():
        # The player needs to decide whether to call again
        ask_poker = input('Would You Hit?(Y/N)>>:')
        if ask_poker.upper() == 'Y':
            return dealing_poker(poker_database)
        elif ask_poker.upper() == 'N':
            print('You stand')
            return False
        else:
            print('Wrong input, please input Y/y or N/n!>>')
            return hit_or_stand()


    def continue_or_quit():
        # At the end of each round, determine whether to continue with the next round of the game.
        # When the number of CARDS in the deck is insufficient, automatically stop the game
        next_round = input('Would you like start next round?(Y/N)>>')
        if next_round.upper() == 'Y':
            if len(poker_database) < 10:
                print('The left pokers is not enough')
                input('Game Over')
                exit(1)
            else:
                return True
        elif next_round.upper() == 'N':
            input('Game Over')
            exit(1)
        else:
            print('Wrong Input, Please Try One More Time!')
            continue_or_quit()


    def start_dealing(poker_database):
        # At the beginning, two CARDS are automatically dealt to the player and the computer
        return [poker_database.pop(random.randint(0, len(poker_database) - 1)),
                poker_database.pop(random.randint(0, len(poker_database) - 1))]


    def one_round(poker_database):
        # A one-round game
        you_get = start_dealing(poker_database)
        pc_get = start_dealing(poker_database)
        print(f'Your hand poker:{you_get[0]} , {you_get[1]}')
        print(f'PC\'s hand poker:{pc_get[0]} , ?\n')
        your_hand_poker.extend(you_get)
        pc_hand_poker.extend(pc_get)
        score = np.array([score_count(your_hand_poker), score_count(pc_hand_poker)])
        if score[0] == 21 or score[1] == 21:
            print('BlackJack')
            return judgement(score[0], score[1])
        else:
            while score[0] <= 21:
                get_new_poker = hit_or_stand()
                if get_new_poker is not False:
                    your_hand_poker.append(get_new_poker)
                    print(f'You Hand Poker:{your_hand_poker}')
                    score[0] = score_count(your_hand_poker)
                    if score[0] > 21:
                        print('You Bust')
                        print(f'PC\'s Hand Poker:{pc_hand_poker}')
                        return judgement(score[0], score[1])
                    else:
                        continue
                elif get_new_poker is False:
                    while score[1] < score[0]:
                        pc_ask_poker = dealing_poker(poker_database)
                        pc_hand_poker.append(pc_ask_poker)
                        pc_score = score_count(pc_hand_poker)
                        score[1] = pc_score
                    print(f'PC final hand poker:{pc_hand_poker}')
                    return judgement(score[0], score[1])
                    break
                else:
                    continue


    if __name__ == '__main__':
        poker_deck = 1  # There are several CARDS to play
        poker_database = poker_name * poker_deck  # The resulting deck
        total_score = np.array([0, 0])  # The scoreboard for the total score
        Round = 1
        while len(poker_database) > 10:
            your_hand_poker = []
            pc_hand_poker = []
            #  input('Start Dealing, good luck...<<Enter>>\n')
            print('Start Dealing, good luck...\n')
            print(f'Round {Round}:')
            print('.' * 60)
            score = one_round(poker_database)
            total_score += score
            print(f'Total score is:{total_score[0]}:{total_score[1]}')
            Round += 1
            continue_or_quit()

#=====================Haoyuan Branch=====================
def Haoyaun_1():

  print("This program will help you to get the current time of the location you choice")
  print("----------------------------")
  print("There are different timezone areas: ")
  
  # requests api
  timezone_total_area = requests.get("https://hpang.w3.uvm.edu/cs021/timezon_total_area.json")
  timezone_area_1 = requests.get("https://hpang.w3.uvm.edu/cs021/timezone_area_1.json")
  timezone_area_2 = requests.get("https://hpang.w3.uvm.edu/cs021/timezone_area_2.json")

  # convert th json
  timezone_total_area = timezone_total_area.json()
  timezone_area_1 = timezone_area_1.json()
  timezone_area_2 = timezone_area_2.json()
  
  again = "Y"
  
  # set the loop
  while again == "Y":
    #print the total timezone areas for user choice
    print(*timezone_total_area, sep = ", ") 
    
    print("-----------------------------")
    # input the user's area
    user_timezone_area = input("Please enter a timezone area from above:")
    
    print("-----------------------------")
    # if user enter timezone area 2
    while not user_timezone_area in timezone_area_2 and not user_timezone_area in timezone_area_1:
      print("Please enter the region given (please use the same capitalization)")
      user_timezone_area = input("Please enter a timezone area from above:")

    else:
      if user_timezone_area in timezone_area_2:

        x = "http://worldtimeapi.org/api/timezone/" + user_timezone_area + ".json"
        current_time = requests.get(x)
        current_time = current_time.json()
        print ("Your enter area current time: ", current_time["datetime"])
        print("---------------------------------------")
    
        b = input("Do you want to try again (Y or N): ")
        b = b.upper()
        again = b
        while again != "Y" and again != "N":
            again = tryagain(again)

      elif user_timezone_area in timezone_area_1:
        y = "https://hpang.w3.uvm.edu/cs021/" + user_timezone_area + ".json"
        z = requests.get(y)
        z = z.json()

        print("There are the locations of the area you entered: ")
        print("----------------------------")
        # print the locaion of the area that user can choice
        print(*z, sep = ", ") 

        print("----------------------------")
        # input the location of the area from above
        user_location = input("Please choose the location of the area you entered from above: ")

        # set loop for the location
        while not user_location in z:
          print("Please enter the region given (please use the same capitalization)")
          user_location = input("Please choose the location of the area you entered from above: ")

        else:

          a = "http://worldtimeapi.org/api/timezone/" + user_timezone_area + "/" + user_location + ".json"
          current_time = requests.get(a)
          current_time = current_time.json()
          print ("Your enter area current time: ", current_time["datetime"])
        
          # again
          print("----------------------------------")
          b = input("Do you want to try again (Y or N): ")
          b = b.upper()
          again = b

          # if user do not enter Y or N
          while again != "Y" and again != "N":
            again = tryagain(again)
   
# set the tryagain function
def tryagain(x):
    b = input("Please enter Y or N: ")
    b = b.upper()
    x = b

    return x

def Haoyuan_2():
    ip = requests.get("http://worldtimeapi.org/api/ip")
    ip = ip.json()


    return ip["datetime"]

#start the application
main()