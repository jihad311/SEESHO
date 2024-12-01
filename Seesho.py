import requests
import time
import random
import sys
import os

def alvino_xy(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()

def clear():
    os.system("clear")

def back():
    menu()

def banner():
    clear()
    print(f""" \x1b[36m               
@@@@@@@@@@    @@@@@@    @@@@@@   @@@@@@@   
@@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
@@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  
!@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  
@!! !!@ @!@  @!@  !@!  @!@!@!@!  @!@  !@!  
!@!   ! !@!  !@!  !!!  !!!@!!!!  !@!  !!!  
!!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  
:!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!  
:::     ::   ::::: ::  ::   :::   :::: ::  
 :      :     : :  :    :   : :  :: :  :   
                             
\x1b[32m____________________________________________

TOOL BY  :\x1b[34m  @riimcc

TELE     :\x1b[35m  https://t.me/riimcc
____________________________________________\x1b[32m""")

def menu():
    banner()
    print("")
    print(" 1 - FILE ")
    print("")
    BALEN = input('  CHOSE : ')
    if BALEN in ['1', '01']:
        FILE()
        exit()


banner()


tim = str(time.time()).split('.')[0]


ugen = []

for _ in range(10000):
    ugen.append(
        random.choice([
            'Mozilla/5.0 (Linux; Android ' + str(random.choice(range(11, 15))) + '; ' + random.choice(['SM-G991B', 'SM-G996B', 'SM-G998B', 'Pixel 4a', 'Pixel 5', 'Pixel 6']) + ') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' + str(random.choice(range(88, 95))) + '.0.' + str(random.choice(range(4324, 5000))) + '.' + str(random.choice(range(50, 150))) + ' Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS ' + str(random.choice(range(13, 17))) + '_' + str(random.choice(range(0, 5))) + ' like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/' + str(random.choice(range(13, 15))) + '.0 Mobile/15E148 Safari/604.1',
        ])
    )


user =input("مطلوب يوزر الحساب: ")
pas =input("مطلوب باسورد الحساب: ")
cookies = {
    'csrftoken': '8ZKR_rf_aCMud5lcihSNO1',
}


headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/?next=%2Fusers%2Fself&source=mobile_nav',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A145P"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': random.choice(ugen),
    'x-asbd-id': '129477',
    'x-csrftoken': '8ZKR_rf_aCMud5lcihSNO1',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1018535731',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'D319C710-C23C-465E-8DE5-B84952754224',
}


data = {
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{pas}',
    'etoken': 'AbgL8JrGd3MCKSnptsaJ8K-FABbYtm0hiQ7h4-mvHvHcpgwP6daZ5fOU4bzGAXp9x_74Q8yQ6uIIR2BOWlfInvau7bruwonmn6W4ne8Y2xusSwwnHPT62U1m',
    'username': user,
}


response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)


if 'userId' in response.text:
    banner()  
    print("\nتم سحب سيشن\n")
    es = response.cookies.get_dict()
    ses = es.get('sessionid', 'غير موجود')
    print(ses)
else:
    banner()  
    print("\nتم رفض الطلب كلمة سر غير صحيحه او محاولات كتيرة ياحبيبي\n")


time.sleep(random.uniform(5, 10))