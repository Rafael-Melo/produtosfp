import requests
from bs4 import BeautifulSoup
from decouple import config
import pandas as pd

# Inicia a sessão
session = requests.session()

payload = {
    'USE_Username': config('RJ_USERNAME'),
    'USE_Password': config('RJ_PASSWORD')
}

urls_fp_RJ = {
    'login_fp_RJ':'https://850153rj01.freshportal.com.br/',
    'logout_fp_RJ':'https://850153rj01.freshportal.com.br/login/index/logout/',
}

# Login no FP
login_response = session.post(urls_fp_RJ['login_fp_gf'], data=payload)
print(login_response)
if login_response.status_code == 200:
    print('Login bem sucedido no FP RJ!')

url = 'https://850153rj01.freshportal.com.br/product/index/data/?1=1&page=1'

texto = 'NÃO USAR - '
