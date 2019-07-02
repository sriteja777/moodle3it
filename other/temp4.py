import bs4
import requests

url = 'https://docs.google.com/forms/d/e/1FAIpQLSc0Pv7KIRU6a4aJB0sWC44uUmfGrdBPciXiYLsxktz_ZCy5eg/viewform'
# page = requests.get(url)
# print(page.status_code)
#
# print(page)
#
#
# sp = bs4.BeautifulSoup(page.text, 'lxml')

# print(sp)
data = {
'entry.639508196':	'sdf',
'entry.1466024362':	"134134",
'fvv':	1,
'draftResponse': "[null,null,'7505878136404283387']",
'pageHistory':	"0",
'fbzx':	"7505878136404283387"
}
value="[null,null,'4690552956041376602']"

s = requests.session()
print(s.headers)
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'})
print(s.headers)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '154',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie':'S=spreadsheet_forms=SgFfVwxEYHKO-rOZa2v-L-_B_cWTDa77; 1P_JAR=2019-3-2-22; NID=162=zAyAsTKj3uU_nGr5HWGnawNK71uGSYCekP_SramkJDYeSHtcKMD0qb2i47J7xZyin3t688E--yRgwTxwDlOeN2vwVpEzrhk5IQ8ZXoXflpo2ZruJn8t2y02vmjA6Kw0irXkfphQbFnxwJAdfEb2ajrxTQOikm15ZcueBgqNqXzLjlGrQ591zZ5vqgyEvSr1H9fLervneG9QFlHGrpdUQtA5fXBeU6hWYD3Sesa5WnEH5TYOZZMMuRe-oXBWffPqYjWVZlTk7Mq6tbqrfHe29VIdwfMaaDAxMlcWwZfbukvLZvqaz3k2zQAklWLnpr0kHmRkhlXnbCLMx4tuYZTrn1eFICgSvKafQ2_8Z9p8kErHRn39DDGCtmS-HJ6MW; OGP=-5061451:-19008374:-19010659:; CONSENT=YES+IN.en-GB+20170423-19-1; SID=HAcCp_IXcJlJIpjv6YPc1h5UTXMhmFsrcFYDyCF_LIf4cQFwc-zvPHeCu0Ih0oyAox5U3Q.; HSID=A_orPp2CpxLmspdy_; SSID=AptgZhhGgoBYmZkpk; APISID=qk4WWWOTOGxv3BYa/AShSY7xxjKlcTZxUi; SAPISID=VntubwIJZ3fJvazb/A5lRRl_4pgV6Pbt98; SIDCC=AN0-TYurBfrh698M4mZsgC3-NSMNvIESYcF1RZUC6xedMw71dSdD7G8j1gA_lB1jihV5mD0euYo; OGPC=19010494-2:19010659-1:; ANID=AHWqTUmavb7V3lWK0WDufMljn0fct71nHnyQhGnk47wSEhlznOGL-dxZCsttq8Ey',
    'DNT': '1',
    'Host': 'docs.google.com',
    'Pragma':'no-cache',
    'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSc0Pv7KIRU6a4aJB0sWC44uUmfGrdBPciXiYLsxktz_ZCy5eg/formResponse',
    'TE': 'Trailers',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
}

cookies= {
'1P_JAR':	'2019-3-2-22',
'ANID':	'AHWqTUmavb7V3lWK0WDufMljn0fct71nHnyQhGnk47wSEhlznOGL-dxZCsttq8Ey',
'APISID': 'qk4WWWOTOGxv3BYa/AShSY7xxjKlcTZxUi',
'CONSENT':	'YES+IN.en-GB+20170423-19-1',
'HSID':	'A_orPp2CpxLmspdy_',
'NID':	'162=zAyAsTKj3uU_nGr5HWGnawNK71uGSYCekP_SramkJDYeSHtcKMD0qb2i47J7xZyin3t688E--yRgwTxwDlOeN2vwVpEzrhk5IQ8ZXoXflpo2ZruJn8t2y02vmjA6Kw0irXkfphQbFnxwJAdfEb2ajrxTQOikm15ZcueBgqNqXzLjlGrQ591zZ5vqgyEvSr1H9fLervneG9QFlHGrpdUQtA5fXBeU6hWYD3Sesa5WnEH5TYOZZMMuRe-oXBWffPqYjWVZlTk7Mq6tbqrfHe29VIdwfMaaDAxMlcWwZfbukvLZvqaz3k2zQAklWLnpr0kHmRkhlXnbCLMx4tuYZTrn1eFICgSvKafQ2_8Z9p8kErHRn39DDGCtmS-HJ6MW',
'OGP':	'-5061451:-19008374:-19010659:',
'OGPC':	'19010494-2:19010659-1:',
'S':	'spreadsheet_forms=SgFfVwxEYHKO-rOZa2v-L-_B_cWTDa77',
'SAPISID':	'VntubwIJZ3fJvazb/A5lRRl_4pgV6Pbt98',
'SID':	'HAcCp_IXcJlJIpjv6YPc1h5UTXMhmFsrcFYDyCF_LIf4cQFwc-zvPHeCu0Ih0oyAox5U3Q.',
'SIDCC': 'AN0-TYtXy46xJ_7kwHHNdM3JGDu3Hvmq_kcBjM8htyMkLeqrhBzH5csW9mPboemTGQ6PWwkGzPU',
'SSID':	'AptgZhhGgoBYmZkpk'
}
page = requests.post(url, data=data, headers=headers, cookies=cookies)

print(page.status_code)

print(page)


sp = bs4.BeautifulSoup(page.text, 'lxml')
print(sp)
