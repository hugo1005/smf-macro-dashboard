import requests
import pandas as pd
import json
import time 
import numpy as np
from functools import reduce

def multi_merge(data_frames,on_key=None, how='inner'):
    if on_key:
        df_merged = reduce(lambda  left,right: pd.merge(left,right,on=on_key,
                                                how=how), data_frames)
    else:
        df_merged = reduce(lambda  left,right: pd.merge(left,right,left_index=True, right_index=True,
                                                how=how), data_frames)
        
    return df_merged

def get_yahoo_data(symbol, start=1514801765, end=1592820985): 
    url = 'https://query1.finance.yahoo.com/v8/finance/chart/' + symbol + '?symbol=' + symbol  +'&period1=' + str(int(start)) + '&period2=' + str(int(end)) +'&interval=1d&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=DyVbyPAh6W5&corsDomain=finance.yahoo.com'
    
    return requests.get(url, headers=headers_yahoo).text

def get_yahoo_symbol_dataframe(symbol, start, end):
    chart_data = json.loads(get_yahoo_data(symbol, start=start, end=end))
    
    quote = pd.DataFrame(chart_data['chart']['result'][0]['indicators']['quote'][0])
    quote['timestamp'] = pd.to_datetime(chart_data['chart']['result'][0]['timestamp'], unit='s').normalize()
    quote = quote.set_index('timestamp')
    
    return quote

def get_forexpros_data(symbol, start=1514801765, end=1592820985):
    url = 'https://tvc4.forexpros.com/734247637035e13fbd6482bf156b3023/1603302403/1/1/8/history?symbol='+str(symbol)+'&resolution=D&from='+ str(int(start)) +'&to=' + str(int(end))
    
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "text/plain",
        "Host": "tvc4.forexpros.com",
        "Origin": "https://tvc-invdn-com.akamaized.net",
        "Referer": "https://tvc-invdn-com.akamaized.net/web/1.12.27/index60-prod.html?carrier=734247637035e13fbd6482bf156b3023&time=1603302403&domain_ID=1&lang_ID=1&timezone_ID=8&version=1.12.27&locale=en&timezone=America/New_York&pair_ID=38545&interval=D&session=session&prefix=www&suffix=&client=1&user=204053647&family_prefix=tvc4&init_page=instrument&sock_srv=https://stream280.forexpros.com:443&m_pids=&watchlist=&geoc=IE&site=https://www.investing.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.271",
    }
    
    return requests.get(url, headers = headers).json()

def get_forexpros_symbol_dataframe(symbol, start, end):
    res = get_forexpros_data(symbol, start, end)
    data = res
    quote = pd.DataFrame(data)
    quote['timestamp'] = pd.to_datetime(quote['t'], unit='s')
    quote = quote.drop(columns=['t'])
    quote = quote.set_index('timestamp')
    
    col_mapping = {
        'vo':'volume',
        'c':'close',
        'o':'open',
        'h':'high',
        'l':'low'
    }
    
    quote.columns = [col_mapping[c] if c in col_mapping else c for c in quote.columns]
    
    return quote

def multi_append(data_frames):
    df_appended = reduce(lambda left,right: left.append(right),data_frames)

    return df_appended

headers_investing = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'sbcharts.investing.com',
    'If-Modified-Since': 'Sun, 08 Nov 2020 17:45:03 GMT',
    'If-None-Match': "145cf-5b39c0161db3e-gzip",
    'Origin': 'https://www.investing.com',
    'Referer': 'https://www.investing.com/economic-calendar/french-cpi-112',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

headers_yahoo = {
        "authority": "query1.finance.yahoo.com",
        "method": "GET",
        "path": "/v8/finance/chart/QCOM?symbol=QCOM&period1=1535997856&period2=1567519221&interval=1d&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=DyVbyPAh6W5&corsDomain=finance.yahoo.com",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "cookie": "APID=UP6e5b7010-bd11-11e8-a127-0681626d5a50; F=d=yDZXJdg9vLUbket1il3yfZQzCzexrWjoO8hhbh4Mr1mVewXPom5GkQ--; AO=u=1; Y=v=1&n=7nlvtglt01snk&l=ux2t12z1w5wxvsqv21s4uw3yv20s5tuu/o&p=028000000000000&r=qh&intl=us; GUC=AQEAAQJdb7xeOEIcMAQY&s=AQAAAMblUZRX&g=XW5uZw; B=ag7016tdl1sf3&b=4&d=1H9k4hlpYEKy5D5ESD1yzg--&s=uk&i=NY5qZtVFDduwOvV7c6Js; T=z=n5mbdBn5mbdB6E1JVs09Oy.MzUwNQYzMk81MzY1MTRPMDExTj&a=QAE&sk=DAA0D4SUrBO8wY&ks=EAATmeh3S36KFVy_W6RtY8.KA--~G&kt=EAAYNVqs1uglRNsGUCczudoVA--~I&ku=FAAkjhYmjzMRQsIUcSQN2vlC9MHYtbt566n0z9BTNhRjVOb4XsGaASJ2Tlb70eDLnJFvBhFmMlK.CAcRMsFfMxvrE8YEzvnskh0_EezrLR1.pxncrqdblJz3i7BWxk.T3nHrpwVwwj.jQm8uWfjZwxpd6VfUng.DwaNkBNGBdoC3qg-~A&d=bnMBeWFob28BZwFVM0U0VFI1SVE0TExDUFY3TU1EQzRTU1NVVQFhAVFBRQFhYwFBTUJVWF9CaAFsYXQBVDVtYmRCAWNzAQFhbAFodWdvamRvbGFuQGdtYWlsLmNvbQFzYwFkZXNrdG9wX3dlYgFmcwFEZXAuWFhSZGJtNGUBenoBVDVtYmRCQTdFAXNsAU5ESTNNZ0UwTlRneU5ERXlOak00TnpZMk9UTTRNVEUt&af=JnRzPTE1Njc1MTgzMTEmcHM9MnFqTUpkVGlRLlpaazNQX2poVURrQS0t; PH=fn=aBa73.MQBMkDK9ptag--&l=en-US&i=us; PRF=t%3DFTEC%252BFNCL%252BADSK%252B%255EVIX%252BFB%252BGPRO%252BXLK%252BACN%252BV",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }

macro_indicators = [
    {'indicator_name': 'CPI_MoM', 'indicator_country':'germany', 'indicator_code': 128, 'category': 'SURVEY'},
    {'indicator_name': 'CPI_MoM', 'indicator_country':'usa', 'indicator_code': 56, 'category': 'SURVEY'},
    {'indicator_name': '10Y_rate', 'indicator_country':'germany', 'indicator_code': 580, 'category': 'BOND'},
    {'indicator_name': '10Y_rate', 'indicator_country':'usa', 'indicator_code': 571, 'category': 'BOND'},
    {'indicator_name': 'PMI', 'indicator_country':'germany', 'indicator_code': 136, 'category': 'SURVEY'},
    {'indicator_name': 'PMI', 'indicator_country':'usa', 'indicator_code': 829, 'category': 'SURVEY'},
    {'indicator_name': 'GDP_QoQ', 'indicator_country':'germany', 'indicator_code': 131, 'category': 'METRIC'},
    {'indicator_name': 'GDP_QoQ', 'indicator_country':'usa', 'indicator_code': 375, 'category': 'METRIC'},
    {'indicator_name': 'consumer_confidence', 'indicator_country':'euro', 'indicator_code': 49, 'category': 'SURVEY'},
    {'indicator_name': 'consumer_confidence', 'indicator_country':'usa', 'indicator_code': 48, 'category': 'SURVEY'},
    {'indicator_name': 'unemployment_rate', 'indicator_country':'germany', 'indicator_code': 142, 'category': 'METRIC'},
    {'indicator_name': 'unemployment_rate', 'indicator_country':'usa', 'indicator_code': 300, 'category': 'METRIC'},
    {'indicator_name': 'balance_of_trade', 'indicator_country':'germany', 'indicator_code': 141, 'category': 'METRIC'},
    {'indicator_name': 'balance_of_trade', 'indicator_country':'usa', 'indicator_code': 286, 'category': 'METRIC'},
    {'indicator_name': 'current_account', 'indicator_country':'germany', 'indicator_code': 81, 'category': 'METRIC'},
    {'indicator_name': 'current_account', 'indicator_country':'usa', 'indicator_code': 1893, 'category': 'METRIC'},
]

indexes_yahoo = {
    'Gold': 'GLD',
    'SP500': 'SPY',
    'DAX': 'DAX',
    'EUROSTOXX50': 'FEZ',
    'EUROSTOXX600': 'EXSA.DE',
    'VIX':'^VIX'
}

indexes_forex = {
    'WTI Crude': 8849,
    'EURUSD': 1,
    'USDJPY': 3
}

def scrape_macro_indicator(indicator_name, indicator_country, indicator_code, indicator_category):
    data = requests.get('https://sbcharts.investing.com/events_charts/us/%s.json' % indicator_code, headers=headers_investing).json()
    df = pd.DataFrame(data['attr'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.set_index('timestamp')
    df.index = df.index.date
    # df = df[['actual_state', 'actual']]
    df = df[['actual']]
    # df.columns = ['%s_%s_vs_forecast' % (indicator_name,indicator_country),'%s_%s_value'% (indicator_name,indicator_country)]
    df.columns = ['%s_%s_%s'% (indicator_category, indicator_name,indicator_country)]

    return df

def scrape_data():
    print("Scraping Macro Data")
    macro_indicators_data = []

    for indicator_obj in macro_indicators:
        indicator_name = indicator_obj['indicator_name']
        indicator_country = indicator_obj['indicator_country']
        indicator_code = indicator_obj['indicator_code']
        indicator_category = indicator_obj['category']

        macro_indicators_data.append(scrape_macro_indicator(indicator_name, indicator_country, indicator_code, indicator_category))

    index_indicators = []

    YR =  time.time() - 1*365*24*3600

    for indicator_name in indexes_yahoo:
        symbol = indexes_yahoo[indicator_name]
        df= get_yahoo_symbol_dataframe(symbol, YR, time.time())
        df = pd.DataFrame(df['close'])
        df.columns = ['INDEX_%s' % indicator_name]

        index_indicators.append(df)

    for indicator_name in indexes_forex:
        symbol = indexes_forex[indicator_name]
        df= get_forexpros_symbol_dataframe(symbol, YR, time.time())
        df = pd.DataFrame(df['close'])
        df.columns = ['FX|COMMODITY_%s' % indicator_name]

        index_indicators.append(df)

    merged_indicators = multi_merge(macro_indicators_data, how='outer').ffill().dropna()
    merged_indexes = multi_merge(index_indicators, how='outer').ffill().dropna()

    export_data = {}

    for col in merged_indicators.columns:
        sample_data = merged_indicators[col].reset_index()
        sample_data.columns = ['date','value']
        sample_data['date'] = sample_data['date'].astype('str')

        export_data[col.upper()] = json.loads(sample_data.to_json(orient='records'))

    for col in merged_indexes.columns:
        sample_data = merged_indexes[col].reset_index()
        sample_data.columns = ['date','value']
        sample_data['date'] = sample_data['date'].astype('str')

        export_data[col.upper()] = json.loads(sample_data.to_json(orient='records'))

    print("Scraping Macro Data Completed!")
    
    return export_data

# if __name__ == '__main__':
#     print("reached")
#     d = scrape_data()

#     lists = [[{'indicator': key, 'value': obj['value'], 'date': obj['date']} for obj in d[key]] for key in d]

#     all_data = []
#     for l in lists:
#         all_data += l

#     pd.DataFrame(all_data).to_csv("indicators.csv")