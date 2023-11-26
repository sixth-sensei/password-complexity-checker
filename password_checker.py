import re
import emoji
from colorama import Fore, Style
from rich.progress import track

special = re.compile("[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]")
complexity = 0

user_password = input("\nEnter a desired password: ")

#Defining scoring criteria
if len(user_password) < 8:
    complexity -= 1
if len(user_password) > 8:
     complexity +=1
if len(user_password) > 12:
    complexity += 1
if len(user_password) > 18:
        complexity += 1
if re.search(special, user_password):
        complexity += 2
if re.search("[A-Z]", user_password):
    complexity += 1
if re.search("[0-9]", user_password):
    complexity += 2

#Using colors to indicate bad or good complexity score
if complexity <= 3:
    print(f"\nYour password complexity score is {Style.BRIGHT}{Fore.RED}{complexity}/8{Fore.RESET}{Style.RESET_ALL} {emoji.emojize(':thumbs_down:')}")
elif complexity > 3:
     print(f"\nYour password complexity score is {Style.BRIGHT}{Fore.GREEN}{complexity}/8{Fore.RESET}{Style.RESET_ALL} {emoji.emojize(':thumbs_up:')}")


#Testing password security against known common passwords
with open("combined-pass-list.txt","r", encoding="ISO 8859-1") as file:
    common_pass = file.read().split()

print(f"\n---Checking your password {Style.BRIGHT}{user_password}{Style.RESET_ALL} against common {Style.BRIGHT}{len(common_pass)}{Style.RESET_ALL} passwords---\n")

if user_password in track(common_pass, description='[green]Please wait...'):
    print(f"\nFound in common passwords list, can be cracked in less than a min {emoji.emojize(':crying_face:')}; not secure!")
else:
    print(f"\nPassword is secure, at least to stall the hacker for some time! {emoji.emojize(':winking_face:')}")

