import os, platform
os.system('git pull')
try:

        import requests

except:

        os.system('pip2 install requests')



import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from bypass import main

        main()



elif bit == "32bit":

        from bypass import main


        main()
