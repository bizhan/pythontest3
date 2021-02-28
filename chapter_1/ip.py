import os.path
import sys

def ip_file_valid():
  ip_file = input("\n # Enter file path: ")

  #checking if the file exists
  if os.path.isfile(ip_file) == True:
    print("\n IP file is valid \n")
  else:
    print("Bad file name")
    sys.exit()

  #open user selected file for reading
  selected_ip_file = open(ip_file, 'r')

  #starting from the begining of the file
  selected_ip_file.seek(0)

  #Reading each line  in the file
  ip_list = selected_ip_file.readlines()

  #Closing the file
  selected_ip_file.close()

  return ip_list

#print(ip_file_valid())