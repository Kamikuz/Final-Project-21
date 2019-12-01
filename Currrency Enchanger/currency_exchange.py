#Kamiku Xue
#CS21 Final Project
#App Name: Currency Exchange

#modules import
import requests
import json

#def the main funciton
def main():
	#initialize the status code
	error = 0
	stop = 0

	#start!
	print("Initializing...")

	# first exception handle
	while error == 1 or stop != 1:
		try:
			#request and get the json of currency list (Chinese Ver.)
			currency_list_zh = requests.get('https://yxue.w3.uvm.edu/cs021/currency_list_zh.json')
			currency_list_zh = currency_list_zh.json()

			#(English Ver.)
			currency_list_en = requests.get('https://yxue.w3.uvm.edu/cs021/currency_list_en.json')
			currency_list_en = currency_list_en.json()
			stop = 1

		except:
			error = 1
			#API error, try to get again
			print('The api is broken or no connection, try later o(╥﹏╥)o')


		#intro info
		print("\nWelcome to use the currency exchange system!\n")

		language = int(input('Please choose the Language(请选择语言)[English --> 0 | 简体中文 --> 1]: '))

		#English Mode
		if language == 0:
			#list the currency and code
			print("\nHere is the code of currency\n----------------------------")
			print("#","CODE","Currency Name",sep='\t|')
			print("----------------------------")
			n = 1
			for item in currency_list_en['list']:
				print(n,item['code'],item['name'],sep='\t|',end="\n")
				n += 1

			PASS = 0
			while PASS == 0:
				#user input the source currency
				origin_currency = input("----------------------------\nPlease enter the source currency(Code): ")
				#case insensitive
				origin_currency = origin_currency.upper()

				#vailate the input
				while not origin_currency.isalpha() or len(origin_currency)>3:
					origin_currency = input("\nInvalid Code! Try again:")
					origin_currency = origin_currency.upper()

				for i in currency_list_en['list']:
					if origin_currency == i['code']:
						PASS = 1
				
				if PASS == 0:
					print("\nThe currency does not exist, try again!")

			PASS = 0
			while PASS == 0:
				#user input the convert currency
				target_currency = input("\nPlease enter the target currency you want to convert(Code): ")
				target_currency = target_currency.upper()

				#vailate the input
				while not target_currency.isalpha() or len(target_currency)>3:
					origin_currency = input("\nInvalid Code! Try again:")
					target_currency = target_currency.upper()

				for i in currency_list_en['list']:
					if target_currency == i['code']:
						PASS = 1

				if PASS == 0:
					print("\nThe currency does not exist, try again!")
			
			print("Loading(*￣︶￣)...")

			#call the request fun to get the rate
			RATE = float(request(origin_currency,target_currency))

			#promot the user to input the amount
			amount = float(input("\nPlease enter the number you want to convert: "))
			
			while amount <=0.0:
				amount = float(input("\nPlease input the valid amount:"))			

			#calculate
			reuslt_amount = amount * RATE

			#call the output function to give the result
			output_en(origin_currency,target_currency,RATE,reuslt_amount,amount)

			stop = int(input('Enchange again？(Yes--> 0 | No(Quit)--> 1): '))

		#Chinese Mode
		elif language == 1:
			#list the currency and code
			print("\n货币列表及其代号\n----------------------------")
			print("序号","代号","货币名称",sep='\t|')
			print("----------------------------")
			n = 1
			for item in currency_list_zh['data']:
				print(n,item['code'],item['name'],sep='\t|',end="\n")
				n += 1

			PASS = 0
			while PASS == 0:
				#user input the source currency
				origin_currency = input("----------------------------\n请输入原货币的代号: ")
				#case insensitive
				origin_currency = origin_currency.upper()

				#vailate the input
				while not origin_currency.isalpha() or len(origin_currency)>3:
					origin_currency = input("\n无效代号，请重新输入:")
					origin_currency = origin_currency.upper()

				for i in currency_list_en['list']:
					if origin_currency == i['code']:
						PASS = 1
				
				if PASS == 0:
					print("\n货币不存在，请重新输入货币代号!")

			PASS = 0
			while PASS == 0:
				#user input the convert currency
				target_currency = input("\n请输入想要转换的货币代号: ")
				target_currency = target_currency.upper()

				#vailate the input
				while not target_currency.isalpha() or len(target_currency)>3:
					origin_currency = input("\n无效代号，请重新输入:")
					target_currency = target_currency.upper()

				for i in currency_list_zh['data']:
					if target_currency == i['code']:
						PASS = 1

				if PASS == 0:
					print("\n货币不存在，请重新输入货币代号!")
			
			print("稍等(*^▽^*)")

			#call the request fun to get the rate
			RATE = float(request(origin_currency,target_currency))

			#promot the user to input the amount
			amount = float(input("\n请输入想要转换的货币金额： "))

			while amount <=0.0:
				amount = float(input("\n请输入正确的金额： "))

			#calculate
			reuslt_amount = amount * RATE

			#call the output function to give the result
			output_zh(origin_currency,target_currency,RATE,reuslt_amount,amount)

			stop = int(input('重新转换？(是--> 0 | 否(退出)--> 1): '))

		else:
			error = 1
			print("选择不存在，请重试！")


def request(x,y):
	#impot the appid to get the api
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

	#retutn the data
	return z

#english output
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

#chinese output
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

#excute
main()