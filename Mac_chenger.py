
import subprocess

def display_banner():
    banner_text = '''
**************************************************************

        
╭━━━╮╱╱╱╱╭╮╭╮╱╭╮╱╱╭╮╱╭━━╮
┃╭━╮┃╱╱╱╱┃┃┃┃╱┃┃╱╭╯╰╮┃╭╮┃
┃╰━╯┣━━┳━╯┃┃╰━╯┣━┻╮╭╯┃╰╯╰┳━━┳╮╱╭┳━━╮
┃╭╮╭┫╭╮┃╭╮┃┃╭━╮┃╭╮┃┃╱┃╭━╮┃╭╮┃┃╱┃┃━━┫
┃┃┃╰┫╭╮┃╰╯┃┃┃╱┃┃╭╮┃╰╮┃╰━╯┃╰╯┃╰━╯┣━━┃
╰╯╰━┻╯╰┻━━╯╰╯╱╰┻╯╰┻━╯╰━━━┻━━┻━╮╭┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯

Mac_Chenger v1.0
Coded by Musharaff
Donet paypal : mjykings12@gmail.com
Bitcoin : 1BMvK1jmYwvQn6VLfkZsTSThEiVXe7tQdU
    
****************************************************************    
 '''
    print(banner_text)

print(display_banner())



interface = input("Enter Interface: ")
New_mac = input("Enter New Mac: ")




subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + New_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)


print("Changing Mac Address "  +interface + " TO " + New_mac )
print("Process Start")

print("................................")

print("Process Compleat......")