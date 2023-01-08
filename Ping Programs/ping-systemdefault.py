import os

ipAddress = input("Enter in IP address/website to ping: ")

os.system("ping {}".format(ipAddress))
