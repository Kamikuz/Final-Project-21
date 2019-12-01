#Kamiku Xue
#CS21 Final Project
#App Name: Currency Exchange

#modules import
import requests
import json

#def the main funciton
def main():
	print("Initializing...")
	currency_list = requests.get('https://api.shenjian.io/exchange/list?appid=01b615dcc108bd15c022160f14627541')
	currency_list = currency_list.json()

	#intro info
	print("\nWelcome to use the currency exchange system!\n")
	print("Here is the code of currency:")

	n = 1

	for item in currency_list['data']:
		print(n,item['code'],item['name'],sep='|',end='\n')
		n += 1

	#user input
	origin_currency = input("Please enter the source currency(Code): ")
	target_currency = input("\nPlease enter the target currency you want to convert(Code): ")
	print("Loading(*￣︶￣)...")

	#call the request fun to get the rate
	RATE = float(request(origin_currency,target_currency))

	#promot the user to input the amount
	amount = float(input("\nPlease enter the number you want to convert: "))

	#calculate
	reuslt_amount = amount * RATE

	#call the output function to give the result
	output(origin_currency,target_currency,RATE,reuslt_amount,amount)

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