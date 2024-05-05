from sec_edgar_downloader import Downloader

def download_10k_filings(ticker):
    downloader = Downloader(company_name='School', email_address= 'varun.kulkarni2107@gmail.com')

    try:
        downloader.get("10-K", ticker, after = '1995-01-01', before = '2023-12-31')
        print(f"Downloaded {ticker} 10-K filing.")
    except Exception as e:
        print(f"Error downloading {ticker} 10-K filing:", str(e))

ticker = input("Enter a ticker: ")
download_10k_filings(ticker)