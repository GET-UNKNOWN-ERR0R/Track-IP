import webbrowser
import sys
import os
import json
import urllib.request

class IPAddressLocator:
    COLORS = {
        'R': '\033[91m',
        'G': '\033[32m',
        'CY': '\033[36m',
        'W': '\033[37m',
        'Y': '\033[93m'
    }

    def __init__(self):
        self.path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')

    def clear_screen(self):
        os.system('clear')

    def display_header(self):
        self.clear_screen()
        print(f"{self.COLORS['W']}MADE BY-{self.COLORS['R']}\n"
              "\n ╰┈➤ ❝ [𝙶𝙴𝚃 𝚄𝙽𝙺𝙽𝙾𝚆𝙽 𝙴𝚁𝚁𝙾𝚁] ❞\n")

    def display_menu(self):
        print(f"{self.COLORS['W']}\n CHOOSE OPTION {self.COLORS['R']}\n"
              f"\n01>>{self.COLORS['W']} CHECK SYSTEM IP"
              f"\n{self.COLORS['R']}02>>{self.COLORS['W']} TRACK IP [IPv4 OR IPv6]"
              f"\n{self.COLORS['R']}03>>{self.COLORS['W']} EXIT HERE\n")
        try:
            choice = int(input(f"{self.COLORS['G']}ENTER YOUR CHOICE [01 02 03]: {self.COLORS['W']}"))
            if choice == 1:
                self.check_system_ip()
            elif choice == 2:
                self.track_ip()
            elif choice == 3:
                print(f"{self.COLORS['W']}<<    END    >>{self.COLORS['W']}")
                sys.exit(0)
            else:
                print(f"{self.COLORS['W']}\nINVALID CHOICE! PLEASE ENTER CORRECT VALUE\n")
                self.display_menu()
        except ValueError:
            print(f"{self.COLORS['W']}\nINVALID CHOICE! PLEASE ENTER CORRECT VALUE\n")
            self.display_menu()

    def display_ip_details(self, data):
        print(f"{self.COLORS['W']}\nHERE ARE THE DETAILS ABOUT THE IP:")
        print(f"{self.COLORS['Y']}")
        print(f"{self.COLORS['G']}1) IP ADDRESS : {self.COLORS['Y']}{data['query']}\n")
        print(f"{self.COLORS['G']}5) COUNTRY : {self.COLORS['Y']}{data['country']}\n")
        print(f"{self.COLORS['G']}4) REGION : {self.COLORS['Y']}{data['regionName']}\n") 
        print(f"{self.COLORS['G']}3) CITY : {self.COLORS['Y']}{data['city']}\n")
        print(f"{self.COLORS['G']}6) LOCATION\n")
        print(f"{self.COLORS['G']}\tLATITUDE : {self.COLORS['Y']}{data['lat']}\n")
        print(f"{self.COLORS['G']}\tLONGITUDE : {self.COLORS['Y']}{data['lon']}\n")
        print(f"{self.COLORS['G']}2) TELECOM COMPANY : {self.COLORS['Y']}{data['org']}\n")
        map_link = f'https://www.google.com/maps/place/{data["lat"]}+{data["lon"]}'
        print(f"{self.COLORS['R']}\n#{self.COLORS['Y']} GOOGLE MAP LINK IS HERE : {self.COLORS['CY']}{map_link}")
        self.ask_to_open_browser(map_link)

    def ask_to_open_browser(self, link):
        open_command = f'am start -a android.intent.action.VIEW -d {link}' if self.path else None
        choice = input(f"{self.COLORS['R']}\n>>{self.COLORS['CY']} DO YOU WANT TO OPEN THIS LINK IN THE BROWSER?{self.COLORS['G']} (Y|N): {self.COLORS['W']}")
        if choice.lower() == 'Y':
            os.system(f"{open_command} > /dev/null") if open_command else webbrowser.open(link, new=0)
        elif choice.lower() == 'N':
            print(f"\nCHECK FOR ANOTHER IP or EXIT USING CTRL + C\n\n")
        else:
            print(f"\nINVALID CHOICE! PLEASE ENTER CORRECT VALUE\n")
        self.display_menu()

    def fetch_ip_details(self, url):
        try:
            response = urllib.request.urlopen(url)
            data = json.load(response)
            self.display_ip_details(data)
        except KeyError:
            print(f"{self.COLORS['R']}\nERROR! INVALID IP ADDRESS!\n{self.COLORS['W']}")
            self.display_menu()
        except urllib.error.URLError:
            print(f"{self.COLORS['R']}\nError!{self.COLORS['Y']} PLEASE CHECK YOUR INTERNET CONNECTION!\n{self.COLORS['W']}")
            sys.exit(1)

    def track_ip(self):
        ip_address = input(f"{self.COLORS['G']}\n>>> {self.COLORS['Y']}ENTER IP ADDRESS:{self.COLORS['W']} ")
        if ip_address:
            url = f'http://ip-api.com/json/{ip_address}'
            self.fetch_ip_details(url)
        else:
            print(f"{self.COLORS['R']}\nENTER VALID IP ADDRESS!")
            self.track_ip()

    def check_system_ip(self):
        url = 'http://ip-api.com/json/'
        self.fetch_ip_details(url)

    def run(self):
        try:
            self.display_header()
            self.display_menu()
        except KeyboardInterrupt:
            print(f"{self.COLORS['Y']}\nGOOD BYE ❤ :){self.COLORS['W']}")

if __name__ == "__main__":
    IPAddressLocator().run()
