import requests

def main():
    r = requests.get('https://api.tradestie.com/v1/apps/reddit')

    dict = r.json()
    
    bullish_count = 0
    bearish_count = 0
    
    for d in dict:
        attitude = d['sentiment']
        if attitude == 'Bearish':
            bearish_count += 1
        elif attitude == 'Bullish':
            bullish_count += 1

    print(f"Bearish: {bearish_count}")
    print(f"Bullish: {bullish_count}")

if __name__ == '__main__':
    main()
