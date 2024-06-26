import requests

print("""  ______      ______      __  __      __      ______          __  __      _____      __    __          ______      ______      __   __     
/\  == \    /\  ___\    /\ \/ /     /\ \    /\  == \        /\ \_\ \    /\  __-.   /\ "-./  \        /\  ___\    /\  ___\    /\ "-.\ \    
\ \  __<    \ \  __\    \ \  _"-.   \ \ \   \ \  __<        \ \  __ \   \ \ \/\ \  \ \ \-./\ \       \ \ \__ \   \ \  __\    \ \ \-.  \   
 \ \_\ \_\   \ \_____\   \ \_\ \_\   \ \_\   \ \_\ \_\       \ \_\ \_\   \ \____-   \ \_\ \ \_\       \ \_____\   \ \_____\   \ \_\\"\_\  
  \/_/ /_/    \/_____/    \/_/\/_/    \/_/    \/_/ /_/        \/_/\/_/    \/____/    \/_/  \/_/        \/_____/    \/_____/    \/_/ \/_/  
                                                                                                                                           """);

url = 'https://hidemn.org/ru/demo/'

if 'Ваша электронная почта' in requests.get(url).text:
    
    email = input('Введите электронную почту для получения тестового периода: ')

    response = requests.post('https://hidemn.org/ru/demo/success/', data={
        "demo_mail": f"{email}"
    })

    if 'Ваш код выслан на почту' in response.text:
        confirm = input('Введите полученную ссылку для подтверждения e-mail адреса: ')
        
        while True:
            try:
                response = requests.get(confirm)
                if 'Спасибо' in response.text:
                    print('Почта подтверждена. Код отправлен на вашу почту!')
                    break
                else:
                    confirm = input('Ссылка невалидная, повторите попытку: ')
            except:
                confirm = input('Ссылка невалидная, повторите попытку: ')
                continue


    else:
        print('Указанная почта не подходит для получения тестового периода ')

else:
    print('Невозможно получить тестовый период')
