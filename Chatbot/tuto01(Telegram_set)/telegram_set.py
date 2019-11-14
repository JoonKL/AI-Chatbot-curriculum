from urllib.request import Request, urlopen

## https://core.telegram.org/bots/api#getupdates

API_KEY = '900118457:AAEX6TdsiVYzSNSabp_NG5ctCdy1M41s76E'
WEBHOOK_URL = 'https://d7ba79cd.ap.ngrok.io'
BOT_INFO_URL = 'https://api.telegram.org/bot{API_KEY}/getMe'.format(API_KEY=API_KEY)
BOT_UPDATE_URL = 'https://api.telegram.org/bot{API_KEY}/getUpdates?offset=1'.format(API_KEY=API_KEY)
BOT_SET_WEBHOOK_URL = 'https://api.telegram.org/bot{API_KEY}/setWebhook?url={WEBHOOK_URL}'\
    .format(API_KEY=API_KEY, WEBHOOK_URL=WEBHOOK_URL)
BOT_DELETE_URL = 'https://api.telegram.org/bot{API_KEY}/deleteWebhook'.format(API_KEY=API_KEY)
BOT_GET_INFO_URL = 'https://api.telegram.org/bot{API_KEY}/getWebhookinfo'.format(API_KEY=API_KEY)

def bot_info_call():
    """
    bot 의 정보를 출력하는 함수 
    """
    request = Request(BOT_INFO_URL)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    print(response_body)


def bot_update_call():
    """
    bot 의 업데이트 정보를 출력하는 함수 
    """
    request = Request(BOT_UPDATE_URL)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    print(response_body)


def bot_set_webhook_call():
    """
    bot 의 Webhook 을 세팅하는 함수
    """
    request = Request(BOT_SET_WEBHOOK_URL)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    print(response_body)


def delete_webhook():
    """
    bot 의 Webhook 을 제거하는 함수
    """
    request = Request(BOT_DELETE_URL)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    print(response_body)

def get_webhook_info():
    request = Request(BOT_GET_INFO_URL)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    print(response_body)

# delete_webhook()
bot_set_webhook_call()