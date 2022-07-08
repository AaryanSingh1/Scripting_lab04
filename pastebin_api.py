import requests

def post_new_paste(title, body_text, expiration='N', listed=True):
    
    print('pasting a new paste to pastebin...', end='')    
    
    params = {
        'api_dev_key': '0p6FtXb08YBURL79lCMkzhEy5R_xYdOp',
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_private': 0 if listed else 1,
        'api_paste_expire_date': expiration
    }
    
    paste_url = 'https://pastebin.com/api/api_post.php'
    
    resp_msg = requests.post(paste_url, data=params)

    if resp_msg.status_code == requests.codes.ok:
        print('Success')
        return resp_msg.text
    else:
        print('Failure')
        print(f'Error Code: {resp_msg.status_code}, Error Reason: {resp_msg.reason}')
        return None


