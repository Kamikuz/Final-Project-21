# Haoyuan Pang
# CS 021
# Final Project

# Project: Worldtime

# import
import requests
import json

# main function
def main():

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

main()