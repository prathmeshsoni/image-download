import pandas as pd
import requests

scrape_do_api_key = '4b3140bceb62487c9cb9303b11123981c94d17ab2f8'

headers = {
    'authority': 'www.apriadirect.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
csv_name = 'apriadirect_data.csv'

df = pd.read_csv(csv_name, encoding='latin-1')

for i in df.index:
    sku_name = df['SKU #'][i]
    images = df['Product Images'][i]
    images_list = images.split(',')
    for k in range(len(images_list)):
        image_link = images_list[k].split('"')[1]

        scrape_do_api_url = f'http://api.scrape.do?token={scrape_do_api_key}&url={image_link}'
        try:
            response = requests.get(scrape_do_api_url, headers=headers)
            if response.status_code == 200:
                with open(f"{sku_name}_{k + 1}.png", 'wb') as f:
                    f.write(response.content)
                print('insert')
                break
            else:
                print(f'{response.status_code} = {image_link} ')
        except:
            pass
    print('Download')
