#Kamiku Xue
#CS21 Final Project
#App Name: Currency Exchange

#modules import
import requests
import json

#def the main funciton
def main():
	error = 0

	print("Initializing...")

	# first exception handle
	try:
		currency_list_zh = requests.get('https://yxue.w3.uvm.edu/cs021/currency_list_zh.json')
		currency_list_zh = currency_list_zh.json()

		currency_list_en = requests.get('https://yxue.w3.uvm.edu/cs021/currency_list_en.json')
		currency_list_en = currency_list_en.json()
	except:
		print('The api is broken or no connection, try later o(╥﹏╥)o')


	#intro info
	print("\nWelcome to use the currency exchange system!\n")

	language = int(input('Please choose the Language[English --> 0 | 简体中文 --> 1]: '))

	if language == 0:
		print("\nHere is the code of currency:")
		n = 1
		for item in currency_list_en['list']:
			print(n,item['code'],item['name'],sep='\t|',end='\n')
			n += 1

		#user input
		origin_currency = input("Please enter the source currency(Code): ")
		origin_currency = origin_currency.upper()

		target_currency = input("\nPlease enter the target currency you want to convert(Code): ")
		target_currency = target_currency.upper()
	
		print("Loading(*￣︶￣)...")

		#call the request fun to get the rate
		RATE = float(request(origin_currency,target_currency))

		#promot the user to input the amount
		amount = float(input("\nPlease enter the number you want to convert: "))

		#calculate
		reuslt_amount = amount * RATE

		#call the output function to give the result
		output(origin_currency,target_currency,RATE,reuslt_amount,amount)

	elif language == 1:
		print("\n下面是货币列表及其代码:")
		n = 1
		for item in currency_list_zh['data']:
			print(n,item['code'],item['name'],sep='\t|',end='\n')
			n += 1

		#user input
		origin_currency = input("请输入原货币的代码: ")
		origin_currency = origin_currency.upper()
		
		target_currency = input("\n请输入想要转换的货币代码: ")
		target_currency = target_currency.upper()
	
		print("请稍等(*￣︶￣)...")

		#call the request fun to get the rate
		RATE = float(request(origin_currency,target_currency))

		#promot the user to input the amount
		amount = float(input("\n请输入转换金额: "))

		#calculate
		reuslt_amount = amount * RATE

		#call the output function to give the result
		output(origin_currency,target_currency,RATE,reuslt_amount,amount)

	else:
		error = 1


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

def output(a,b,c,d,e):
	#format the data
	d = format(d,'.3f')
	e = format(e,'.3f')

	#print them
	print("--------------Result--------------")
	print("Original Currency:\t",e,a)
	print("\nConvert Currency:\t",d,b)
	print("\nThe rate is:\t",c)
	print("----------------------------------")

#excute
main()