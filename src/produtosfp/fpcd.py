import requests
from bs4 import BeautifulSoup
from decouple import config
import pandas as pd

# Inicia a sessão
session = requests.session()

payload = {
    'USE_Username': config('GF_USERNAME'),
    'USE_Password': config('GF_PASSWORD')
}

urls_fp_gf = {
    'login_fp_gf':'https://850153b.freshportal.com.br/',
    'logout_fp_gf':'https://850153b.freshportal.com.br/login/index/logout/',
}

# Login no FP
login_response = session.post(urls_fp_gf['login_fp_gf'], data=payload)
print(login_response)
if login_response.status_code == 200:
    print('Login bem sucedido no FP GF!')
