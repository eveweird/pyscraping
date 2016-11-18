import requests, bs4

dlynx = []
blynx = []

def main(site):
    res = requests.get(site)
    if res.status_code == 404:
        print('broken:', site)
        blynx.append(site)
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        lynx = soup.select('a')
        for i in range(len(lynx)):
            if not (lynx[i].get('href') in dlynx):
                dlynx.append(lynx[i].get('href'))
                try:
                    main(lynx[i].get('href'))
                except Exception as exc:
                    print()
            

main('http://ms.demo.org/98/')
print(blynx)
