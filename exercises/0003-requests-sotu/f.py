import requests
url = ['https://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-address-joint-session-congress', 'https://www.whitehouse.gov/the-press-office/remarks-president-state-union-address', 'https://www.whitehouse.gov/the-press-office/2011/01/25/remarks-president-state-union-addressehouse.gov/the-press-office/2012/01/24/remarks-president-state-union-address', 'https://www.whitehouse.gov/the-press-office/2013/02/12/remarks-president-state-union-address', 'https://www.whitehouse.gov/the-press-office/2014/01/28/president-barack-obamas-state-union-address', 'https://www.whitehouse.gov/the-press-office/2015/01/20/remarks-president-state-union-address-january-20-2015', 'https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address']
for i in range(len(url)):
	resp = requests.get(url[i])
	print(resp.url)
	print(len(resp.text))
	print(resp.text.upper().count("APPLAUSE"))