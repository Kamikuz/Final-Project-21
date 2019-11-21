#Kamiku Xue
#CS21 
#Final Project 1 - Anime Tracker

#Modules import
import requests
import mysql.connector

#Connect to the database
database = mysql.connector.connect(
  host="webdb.uvm.edu",
  user="yxue_admin",
  passwd="********",
  database="YXUE_final"
)

def main():
	pass

#User Login
def login():
	print('Lite Anime Tracker System\nPlease login to track your anime\n---------------------')
	username = input("Username")

	#start the catch the username in database
	try:
		mycursor = mydb.cursor()
		sql = "SELECT * FROM customers WHERE username = '"+ username +"'"
		mycursor.execute(sql)
		result = mycursor.fetchall()

	if result.get():
		regist()
	else:
		password = input("password")

#User Register
def regist():
	pass

#Get the API of user info
def getinfo():
	pass

#Print the HTML page