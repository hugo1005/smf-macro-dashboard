import numpy as np
import pandas as pd
import datetime as dt
from datetime import datetime
import requests
import json
import time
from gekko import GEKKO
import scipy.stats as st

# Data Fetching Code

def get_yahoo_data(symbol, headers, offline=False, start=1514801765, end=1592820985): 
    url = 'https://query1.finance.yahoo.com/v8/finance/chart/' + symbol + '?symbol=' + symbol  +'&period1=' + str(int(start)) + '&period2=' + str(int(end)) +'&interval=1d&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=DyVbyPAh6W5&corsDomain=finance.yahoo.com'
    if offline:
        with open("./price_data/%s.txt" % symbol) as data:
            return data
    
    return requests.get(url, headers=headers).text

def get_yahoo_symbol_dataframe(symbol, headers, start, end, offline=False):
    chart_data = json.loads(get_yahoo_data(symbol, headers, offline=offline, start=start, end=end))
    quote = pd.DataFrame(chart_data['chart']['result'][0]['indicators']['quote'][0])
    quote['timestamp'] = pd.to_datetime(chart_data['chart']['result'][0]['timestamp'], unit='s').normalize()
    quote = quote.set_index('timestamp')
    
    return quote

def get_forexpros_data(symbol, headers, offline=False, start=1514801765, end=1592820985):
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

def get_forexpros_symbol_dataframe(symbol, headers, start, end, offline=False):
    res = get_forexpros_data(symbol, headers, offline, start, end)
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

def convert_close_prices_to_eur(closes, lookback_years, headers):
    start = time.time() - lookback_years * 3600 * 24 * 365
    end = time.time()
    usd_to_eur = pd.DataFrame(get_yahoo_symbol_dataframe('EUR=X',headers=headers,start=start, end=end)['close'])
    usd_to_eur.columns = ['USDEUR']

    merged = closes.merge(usd_to_eur, left_index=True, right_index=True)
    index = merged.index
    X = merged.values[:,:-1]
    Y = merged.values[:,-1].reshape((-1,1))
    merged = merged.drop(columns=['USDEUR'])
    cols = merged.columns
    merged = pd.DataFrame(X * Y)
    merged.columns = cols
    merged.index = index
    return merged

def get_tickers_for_lookback_period(tickers, lookback_years, headers):
    year_in_seconds = 60 * 60 * 24 * 365
    end = time.time() 
    start = time.time() - lookback_years * year_in_seconds
    portfolio_series = {}
    
    for ticker in tickers:
        if type(ticker) == type(''):
            # IF ITS FROM YAHOO ASSUME IT IS IN USD (IE USE ADR's)
            price_data = get_yahoo_symbol_dataframe(ticker, headers, start, end)
            price_data = convert_close_prices_to_eur(price_data, lookback_years, headers)
            portfolio_series[ticker] = price_data
        else:
            price_data = get_forexpros_symbol_dataframe(ticker, headers, start, end)
            portfolio_series[ticker] = price_data
        
    return portfolio_series

def get_ticker_closes_dataframe(portfolio_series):
    to_merge = []
    tickers = []
    for ticker in portfolio_series:
        to_merge.append(portfolio_series[ticker]['close'])
        tickers.append(ticker)

    closes = pd.DataFrame(to_merge).T
    closes.columns = tickers
    closes = closes.interpolate()
    
    return closes

def get_weighted_close_fn(user_weights):
    def compute_weighted_close(row):
        close_portfolio = 0

        for ticker, weight in user_weights.items():
            close_portfolio += weight * row[ticker]

        return close_portfolio
    
    return compute_weighted_close

def get_close_data(weights, lookback_years, headers, port_name='PORT'):
    tickers = list(weights.keys())
    portfolio_series = get_tickers_for_lookback_period(tickers, lookback_years, headers)
    closes = get_ticker_closes_dataframe(portfolio_series).interpolate()
    
    if type(port_name) != type(None):
        closes[port_name] = closes.apply(get_weighted_close_fn(weights), axis=1) 
    
    return closes

def get_index_closes(idx_weights, lookback_years, headers, start_date):
    idx_closes = {}

    for region in idx_weights:
        region_weights = idx_weights[region]


        closes_region_list = []

        for sector in region_weights:
            tickers = region_weights[sector]['tickers']
            ticker_weights = {ticker: 1 for ticker in tickers}

            # Think if we want to multiply weights x price or adjust for returns after...
            closes_sector = get_close_data(ticker_weights, lookback_years, headers, port_name=sector)
            closes_region_list.append(closes_sector[sector])

        closes_region_df = pd.DataFrame(closes_region_list).T
        closes_region_df[region] = get_close_data({region: 1}, lookback_years, headers, port_name=None)[region]

        idx_closes[region] = closes_region_df.interpolate().bfill()
        
    for region in idx_closes:
        idx_closes[region] = idx_closes[region][idx_closes[region].index >= pd.to_datetime(start_date, unit='s')]
    
    return idx_closes

# Weighting Approximation Code

def fit_historical_sector_weights(region, idx_closes, force_sector_weights = None):
    sector_returns = idx_closes[region].pct_change().interpolate().dropna()
    quarter = sector_returns.index.quarter

    years = sector_returns.index.year.unique().values
    quarter_sector_weights_approx = {year:{} for year in years}

    for year in years:
        for quarter in range(1,5):
            quarter_returns = sector_returns[(sector_returns.index.quarter == quarter) & (sector_returns.index.year == year)]
            if len(quarter_returns) > 0:
                
                if type(force_sector_weights) == type(None):

                    X = quarter_returns.drop(columns=region)
                    y = quarter_returns[region]

                    X_vals = X.values
                    X_cols = X.columns.values
                    y_vals = y.values

                    # Constrained Multiple Linear Regression

                    nd = y_vals.shape[0] # number of data points
                    nc = X_vals.shape[1]   # number of inputs
                    x = X_vals
                    y = y_vals


                    m = GEKKO()
                    m.options.IMODE=2

                    c  = m.Array(m.FV,nc) # Coefficients

                    for ci in c:
                        ci.STATUS=1
                        ci.LOWER=0
                        ci.UPPER=1

                    xd = m.Array(m.Param,nc)

                    for i in range(nc):
                        xd[i].value = x[:,i] # Assign each column vector of data

                    yd = m.Param(y) # True Y Values
                    yp = m.Var() # Predicted Y Values
                    eq = m.Param(value=1)

                    q = m.sum([c[i] for i in range(nc)])
                    q2 = m.sum([c[i]**2 for i in range(nc)])
                    s = m.sum([c[i]*xd[i] for i in range(nc)]) # Multiply each column by the coefficient and sum to get predicted y
                    eq =  m.Const(1)
                    
                    m.Equation(q == eq) # Constrain weights to sum to one
                    
                    m.Minimize((yd-s)**2 + 0.0005 * q2) # Least Squares Minimisation with L2

                    m.solve(disp=False)

                    a = [c[i].value[0] for i in range(nc)]

                    quarter_sector_weights_approx[year][quarter] = {X_cols[i]: c[i].value[0]for i in range(nc)}
                else:
                    quarter_sector_weights_approx[year][quarter] = force_sector_weights
    return quarter_sector_weights_approx

simple_return = lambda series, period, shift: (series.iloc[-1-shift] / series.iloc[-period-shift]) - 1

def get_period_returns_by_quarter_and_sector(closes, period, sectors):
        closes_filtered = closes.iloc[-period:].dropna()
        quarters = closes_filtered.index.quarter.unique()
        years = closes_filtered.index.year.unique()

        sector_period_returns = {sector:{year:{} for year in years} for sector in sectors}
        
        for sector in sectors:
            series = closes_filtered[sector]  
            for year in years:
                for quarter in quarters:
                    segment = series[(series.index.year == year) & (series.index.quarter == quarter)]
                    if len(segment):
                        sector_period_returns[sector][year][quarter] = (segment.iloc[-1] / segment.iloc[0]) - 1
                    
        return sector_period_returns

def approximate_index_returns(closes, period, sectors, quarter_sector_weights_approx):
    qs_returns = get_period_returns_by_quarter_and_sector(closes, period, sectors)

    sector_weighted_return_approx = 0

    for sector, sector_qs_returns in qs_returns.items():
        for year, year_returns in sector_qs_returns.items():
            for quarter, unweighted_return in year_returns.items():
                sector_weighted_return_approx += quarter_sector_weights_approx[year][quarter][sector] * unweighted_return
    
    return sector_weighted_return_approx

def draw_approximation_graphs(region, idx_closes, quarter_sector_weights_approx):
    ground_truth = []
    crude = []
    fitted = []
    periods = []
    
    region_data = idx_weights[region]
    for period in range(10,320,10):
        region_return = simple_return(idx_closes[region][region], period, 0)
        aproximate_return = approximate_index_returns(idx_closes[region], period, list(region_data.keys()), quarter_sector_weights_approx)

        crude_return = sum([
            region_data[sector]['weight'] * simple_return(idx_closes[region][sector], period, 0) for sector in region_data
        ])

        ground_truth.append(region_return)
        crude.append(crude_return)
        fitted.append(aproximate_return)
        periods.append(period)
        
    
    plt.figure(figsize=(20,7))
    ax1 = plt.subplot2grid((1,2), (0,0))
    ax2 = plt.subplot2grid((1,2), (0,1))

    pd.DataFrame({'Actual Returns': ground_truth, 'Latest Sector Weights': crude, 'Returns (Numerically Fitted)': fitted}, index=periods).plot(ax=ax1)
    ax1.set_xlabel("Shift (Days)")
    ax1.set_ylabel("Return (%)")
    ax1.set_title("Combining Sector Returns to Predict Region Index Returns")

    pd.DataFrame(quarter_sector_weights_approx[2020]).T.plot(kind='area', xticks=[1,2,3,4], ax=ax2)
    ax2.set_xlabel('Quarter')
    ax2.set_ylabel('Weights')
    ax2.set_title("Implied Sector Weightings for Index")
    plt.show()
    
def get_regional_sector_stocks(sectors, regions, region):
    regional_sectors = {}
    for sector, stocks in sectors.items():
        regional_sectors[sector] = []

        for stock in stocks:
            if stock in regions[region]:
                regional_sectors[sector].append(stock)
    
    return regional_sectors

def get_regional_portfolio_weight(regional_sectors, user_weights):
    # Get our normalisation value for region
    overall_region_weight = 0

    for sector, stocks in regional_sectors.items():
        for stock in stocks:
            overall_region_weight += user_weights[stock]
            
    return overall_region_weight

def normalise_regional_portfolio_weighting(regional_sectors, user_weights):
    # Compute regional sector weights
    user_regional_sector_weights = {}
    overall_region_weight = get_regional_portfolio_weight(regional_sectors, user_weights)

    for sector, stocks in regional_sectors.items():
        user_regional_sector_weights[sector] = 0

        for stock in stocks:
            user_regional_sector_weights[sector] += (user_weights[stock] / overall_region_weight)
            
    return user_regional_sector_weights

# Brinson Model Code

def compute_portfolio_sector_return(closes, regional_sectors, sector, period):
    n = len(regional_sectors[sector])
        
    if n > 0:
        sector_return = 0
        
        for stock in regional_sectors[sector]:
            sector_return += (closes[stock].iloc[-1] / closes[stock].iloc[0]) - 1
        
        return sector_return / n # Assume equal_weighting
    else:
        return 0

def compute_benchmark_sector_return(idx_closes, region, sector, period):
    return (idx_closes[region][sector].iloc[-1] / idx_closes[region][sector][0]) - 1

def compute_selection_effect(w_i, R_i, B_i, sector):
    return w_i[sector] * (R_i[sector] - B_i[sector])

def compute_allocation_effect(w_i, sector, region, period, idx_closes, benchmark_weights):
    benchmark_series = idx_closes[region][region].iloc[-period:]
    benchmark_sector_series = idx_closes[region][sector].iloc[-period:]
    
    A_i = 0
    W_i_avg = []   
    
    for year in benchmark_series.index.year.unique():
        
        benchmark_series_year = benchmark_series[benchmark_series.index.year == year]
        benchmark_sector_series_year = benchmark_sector_series[benchmark_sector_series.index.year == year]
        
        for quarter in benchmark_series_year.index.quarter.unique():
            
            benchmark_series_quarter = benchmark_series_year[benchmark_series_year.index.quarter == quarter]
            benchmark_sector_series_quarter = benchmark_sector_series_year[benchmark_sector_series_year.index.quarter == quarter]
            
            B_q = (benchmark_series_quarter.iloc[-1] / benchmark_series_quarter.iloc[0]) - 1
            B_i_q = (benchmark_sector_series_quarter.iloc[-1] / benchmark_sector_series_quarter.iloc[0]) - 1
            
            W_i_q = benchmark_weights[year][quarter][sector]
            A_i_q = w_i[sector] * (B_i_q - B_q) - W_i_q * (B_i_q - B_q)

            A_i += A_i_q
            W_i_avg.append(W_i_q)
            
    return A_i, sum(W_i_avg) / len(W_i_avg)
 
def attribute_regional_performance(idx_closes, equity_closes, user_weights, sectors, regions, region='SPY', period=252, verbose=False, force_sector_weights = None):
    regional_sectors = get_regional_sector_stocks(sectors, regions, region)  
    user_regional_sector_weights = normalise_regional_portfolio_weighting(regional_sectors, user_weights)
    c = equity_closes
    
    print("Approximating historical sector weights...")
    
    quarter_sector_weights_approx = fit_historical_sector_weights(region, idx_closes, force_sector_weights = force_sector_weights)
    
    # if verbose:
    #     draw_approximation_graphs(region, idx_closes, quarter_sector_weights_approx)
    
    print("Atrributing Performance...")
    
    w_i = user_regional_sector_weights
    R_i = {sector: compute_portfolio_sector_return(c, regional_sectors, sector, period) for sector in w_i}
    B_i = {sector: compute_benchmark_sector_return(idx_closes, region, sector, period) for sector in w_i}
    S_i = {sector: compute_selection_effect(w_i, R_i, B_i, sector) for sector in w_i}
    A_i_W_i_Avg = {sector: compute_allocation_effect(w_i, sector, region, period, idx_closes, quarter_sector_weights_approx) for sector in w_i}
    A_i = {sector: A_i_W_i_Avg[sector][0] for sector in w_i}
    W_i_avg = {sector: A_i_W_i_Avg[sector][1] for sector in w_i}

    B = (idx_closes[region][region].iloc[-1] / idx_closes[region][region].iloc[0]) - 1
    print(region, " Benchmark performance: ", B)
    print(idx_closes[region][region])
    BrinsonFachlerModel = (pd.DataFrame([{
        'Sector': sector,
        'Portfolio Return': R_i[sector],
        'Portfolio Weight': w_i[sector],
        'Benchmark Return': B_i[sector],
        'Avg Benchmark Weight*': W_i_avg[sector],
        'Selection': S_i[sector],
        'Allocation': A_i[sector],
        #'S+A': S_i[sector] + A_i[sector],
        #'S+A (Check)': w_i[sector] * (R_i[sector] - B) - W_i_avg[sector] * (B_i[sector] - B), # Note this should be approx = S+A 
        'Portfolio Weighted Return': R_i[sector] * w_i[sector],
        'Benchmark Weighted Return*': B_i[sector] * W_i_avg[sector]
    } for sector in sectors]).set_index('Sector'))

    R = (BrinsonFachlerModel['Portfolio Return'] * BrinsonFachlerModel['Portfolio Weight']).sum()

    aggregate_BF_Model = pd.DataFrame([{
        'Portfolio Total Return': R,
        'Benchmark Total Return': B,
        #'Benchmark Total Return (Check)': sum([W_i_avg[sector]*B_i[sector] for sector in sectors]), # Approx
        #'Benchmark Weight (Check)': sum([W_i_avg[sector] for sector in sectors]), # Approx
        'Portfolio Outperformance': R - B, # Note R - B != S + A as our benchmark weights are only approximations not exact.
        'Selection Effect': BrinsonFachlerModel['Selection'].sum(),
        'Allocation Effect': BrinsonFachlerModel['Allocation'].sum(),
        'Total Effect': BrinsonFachlerModel['Selection'].sum() + BrinsonFachlerModel['Allocation'].sum(),
    }]).T

    aggregate_BF_Model.columns = ['Returns (%)']

    start = idx_closes[region][region].index[-period]
    end = idx_closes[region][region].index[-1]

    model_df = (BrinsonFachlerModel * 100).round(2).sort_values(by='Portfolio Weighted Return', ascending=False)
    aggregate_model_df = (aggregate_BF_Model * 100).round(2)

    return {'model_df': model_df, 'aggregate_model_df': aggregate_model_df}

cfg = {
    "start_date": 1607641200,
    "headers": {
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
    },
    "portfolio_equity_weights": {
        "BLK": 0.051577,
        "DIS": 0.025979,
        "GOOG": 0.128988393,
        "WMT": 0.031639432,
        "PG": 0.020142968,
        "JNJ": 0.100128004,
        "MSFT": 0.130701028,
        "DG": 0.076398,
        "WM": 0.042881482,
        "NSRGY": 0.092963657,
        "VWDRY": 0.070327971,
        "NVS": 0.085778035,
        "SBGSY": 0.085525394,
        "IBDSF": 0.056969947,
    },
    "benchmark_region_weights": {
        "SPY": 0.614,
        46323: 0.386
    },
    "portfolio_equities_sector_classification": {
        "Communications": ["DIS","GOOG"],
        "Consumer_Disrectionary": ["DG"],
        "Consumer_Staples": ["NSRGY","WMT","PG"],
        "Energy_Renewables": ["VWDRY"],
        "Financials": ["BLK"],
        "Health_Care": ["NVS","JNJ"],
        "Information_Technology": ["MSFT"],
        "Industrials": ["WM","SBGSY"],
        "Utilities": ["IBDSF"],
        "Other": []
    },
    "index_sectors": {
        "SPY":{
            "Communications": {"weight": 0.108 , "tickers":["XLC"]},
            "Consumer_Disrectionary": {"weight": 0.116 , "tickers":["XLY"]},
            "Consumer_Staples": {"weight": 0.07, "tickers":["XLP"]},
            "Energy_Renewables": {"weight": 0.021, "tickers":["XLE"]},
            "Financials": {"weight": 0.097 , "tickers":["XLF"]},
            "Health_Care": {"weight": 0.142 , "tickers":["XLV"]},
            "Information_Technology":{"weight": 0.282 , "tickers":["XLK"]} ,
            "Industrials": {"weight": 0.026 , "tickers":["XLI"]},
            "Utilities": {"weight": 0.03 , "tickers":["XLU"]},
            "Other": {"weight": 0.109 , "tickers":["XLB","XLRE"]}
        },
        46323:{
            "Communications": {"weight": 0.04 , "tickers":[46335,47545]},
            "Consumer_Disrectionary": {"weight": 0.098 , "tickers":[38542]},
            "Consumer_Staples": {"weight": 0.135, "tickers":[38548, 38545]},
            "Energy_Renewables": {"weight": 0.021, "tickers":[38546]},
            "Financials": {"weight": 0.144 , "tickers":[38543,46351,46344]},
            "Health_Care": {"weight": 0.159 , "tickers":[46417]},
            "Information_Technology":{"weight": 0.08 , "tickers":["EXV3.DE"]} ,
            "Industrials": {"weight": 0.092 , "tickers":[38538]},
            "Utilities": {"weight": 0.048 , "tickers":[46413]},
            "Other": {"weight": 0.149 , "tickers": [47542,38551]}
        }
    },
    "portfolio_equities_region_classification": {
        "SPY": ["BLK","DIS","GOOG","WMT","PG","JNJ","MSFT","DG","WM"],
        46323: ["NSRGY","VWDRY","NVS","SBGSY","IBDSF"]
    }
}

def get_attribution_report():
    print("Fetching attribution report")
    attribution = {}

    headers = cfg['headers']
    start_date = cfg['start_date']

    # lookback_years = (current_date - start_date) / (3600 * 24 * 365)
    lookback_years = 2
    portfolio_equity_weights = cfg['portfolio_equity_weights']
    equity_sectors = cfg['portfolio_equities_sector_classification']
    equity_regions = cfg['portfolio_equities_region_classification'] 
    index_sectors = cfg['index_sectors']
    benchmark_region_weights = cfg['benchmark_region_weights']
    
    idx_closes = get_index_closes(index_sectors, lookback_years, headers, start_date)   
    equity_closes = get_close_data(portfolio_equity_weights, lookback_years, headers)

    equity_closes = equity_closes[equity_closes.index >= pd.to_datetime(start_date, unit='s')]

    attribution_period = len(equity_closes)
    # Indivdidual Region Analysis
    for region in equity_regions.keys():
        attribution[region] = attribute_regional_performance(idx_closes, equity_closes, portfolio_equity_weights, equity_sectors, equity_regions, region=region, period=attribution_period, verbose=True)

    # Overall Analysis
    # The regions become sectors
    region_as_equity_sectors = equity_regions
    # All stocks now become in one super region (the world)
    world_as_equity_regions = {'BENCHMARK': list(portfolio_equity_weights.keys())}
    region = 'BENCHMARK'
    # The index closes for the benchmark contains the sub sector indices which are the regional benchmarks
    idx_benchmark_closes = [idx_closes[region][region] for region in equity_regions.keys()]
    # The actual index returns are all we really care about anyway so we will arbitrarily set it to start at value 100 
    idx_benchmark_closes = {region: idx_closes[region][region] for region in equity_regions.keys()}
    idx_benchmark_closes = pd.DataFrame(idx_benchmark_closes).interpolate()
    idx_benchmark_closes = idx_benchmark_closes.bfill()

    idx_benchmark_closes_returns = {region: (idx_benchmark_closes[region].values[1:] / idx_benchmark_closes[region].values[:-1]) - 1 for region in equity_regions.keys()}
    idx_benchmark = [100]

    any_region = list(equity_regions.keys())[0]
    for i in range(0, len(idx_benchmark_closes_returns[any_region])):
        weighted_regions_return = sum([returns[i] * benchmark_region_weights[region] for region, returns in idx_benchmark_closes_returns.items()])
        idx_benchmark.append((1 + weighted_regions_return) * idx_benchmark[i])

    idx_benchmark_closes['BENCHMARK'] = idx_benchmark
    idx_closes['BENCHMARK'] = idx_benchmark_closes

    # Attribute
    attribution['overall'] = attribute_regional_performance(idx_closes, equity_closes, portfolio_equity_weights, region_as_equity_sectors, world_as_equity_regions, region=region, period=attribution_period, verbose=True, force_sector_weights = benchmark_region_weights)

    # Formatted Output
    EUROSTOXX = 46323
    attribution_eu = attribution[EUROSTOXX]['model_df'][['Selection', 'Allocation']]
    attribution_us = attribution['SPY']['model_df'][['Selection', 'Allocation']]
    atrribution_effects = attribution_eu.merge(attribution_us, left_index=True, right_index=True, suffixes=('_EU','_US'))

    portfolio_daily_returns = pd.DataFrame(equity_closes.iloc[:,:-1].pct_change().apply(get_weighted_close_fn(portfolio_equity_weights), axis=1).dropna())
    portfolio_daily_returns.columns=['PORTFOLIO']
    benchmark_daily_returns = pd.DataFrame(idx_closes['BENCHMARK']['BENCHMARK'].pct_change().dropna())
    benchmark_port_returns = benchmark_daily_returns.merge(portfolio_daily_returns, left_index=True, right_index=True)
    benchmark_port_returns['DELTA'] = benchmark_port_returns['PORTFOLIO'] - benchmark_port_returns['BENCHMARK']

    tracking_error_pct = round(benchmark_port_returns['DELTA'].std() * 100,2)
    sharpe = portfolio_daily_returns.mean() / portfolio_daily_returns.std()

    Y = benchmark_port_returns['PORTFOLIO'].values.reshape(-1,1)
    x_1 = benchmark_port_returns['BENCHMARK'].values.reshape(-1,)
    x_0 = np.ones(x_1.shape)
    X = np.array([x_0,x_1]).T
    
    alpha, beta = (np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, Y))).reshape(-1,)
    alpha, beta = round(alpha,3), round(beta,3)
    sharpe = round(sharpe.values[0],3)

    print("Fetching attribution report completed!")

    return {
        "portfolio_summary_stats": {
            "sharpe": sharpe,
            "alpha": alpha,
            "beta": beta,
            "tracking_error_pct": tracking_error_pct,
        },
        "attribution": {
            "regions":{
                "Overall": json.loads(attribution['overall']['aggregate_model_df'].to_json())['Returns (%)'],
                "Europe": json.loads(attribution[EUROSTOXX]['aggregate_model_df'].to_json())['Returns (%)'],
                "US": json.loads(attribution['SPY']['aggregate_model_df'].to_json())['Returns (%)'],
            },
            "sectors": json.loads(atrribution_effects.T.round(2).to_json()),
        }
    }
