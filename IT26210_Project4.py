import re
from requests import get
import socket

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#To check the format of the IP address both IPv4 & IPv6
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
regex2 = "^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"

print(" ")
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address1 = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"Your IP Address: {ip_address1}")
print("")


loopVariable = True

#loop for the loopVariable
while loopVariable:
    ip_address = input("Enter IP Address: ")
    def check(Ip):
        if(re.search(regex, Ip)):
            print("")
            print("IP Details")
            print('IP Address: ' + get('https://ipapi.co/'+ip_address+'/ip/').text)
            print('Country: ' + get('https://ipapi.co/'+ip_address+'/country_name/').text)
            print('Capital: ' + get('https://ipapi.co/'+ip_address+'/country_capital/').text)
            print('Postal Code: ' + get('https://ipapi.co/'+ip_address+'/postal/').text)
            print('City: ' + get('https://ipapi.co/'+ip_address+'/city/').text)
            print('Geolocation: ' + get('https://ipapi.co/'+ip_address+'/latlong/').text)
            print('ASN: ' + get('https://ipapi.co/'+ip_address+'/asn/').text)
            print('ORG: ' + get('https://ipapi.co/'+ip_address+'/org/').text)
        elif(re.search(regex2, Ip)):
            print(" ")
            print('IP Address: ' + get('https://ipapi.co/'+ip_address+'/ip/').text)
            print('Country: ' + get('https://ipapi.co/'+ip_address+'/country_name/').text)
            print('Capital: ' + get('https://ipapi.co/'+ip_address+'/country_capital/').text)
            print('Postal Code: ' + get('https://ipapi.co/'+ip_address+'/postal/').text)
            print('City: ' + get('https://ipapi.co/'+ip_address+'/city/').text)
            print('Geolocation: ' + get('https://ipapi.co/'+ip_address+'/latlong/').text)
            print('ASN: ' + get('https://ipapi.co/'+ip_address+'/asn/').text)
            print('ORG: ' + get('https://ipapi.co/'+ip_address+'/org/').text)
        else:
            print(" ")
            print(Fore.RED + "======================================================================")
            print(Fore.RED + " ||   The IP Address that you entered is INVALID. Please try Again. || ")
            print(Fore.RED + "======================================================================")
    #for checking the IP address
    if __name__ == '__main__' :
        check(ip_address)
    #loop for inputing another IP address
        answer = True
        while answer:
            print(" ")
            loopVariable2 = input("Do you want to try again?[Y/N]: ")
            print(" ")
            
            if loopVariable2 == 'Y' or loopVariable2 == 'y':
                loopVariable = True
                break
            elif loopVariable2 == 'n' or loopVariable2 == 'N':
                loopVariable = False
                break
            else:
               print(" ")
               print(Fore.RED + "==================================")
               print(Fore.RED + " ||   Error! Please try again. || ")
               print(Fore.RED + "==================================")
               answer