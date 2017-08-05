from coinmarketcap import Market
import operator
coinmarketcap = Market()

def infoPulled(n):
	numberPulled = coinmarketcap.ticker(limit=n)
	unsortedArray = []
	for i in numberPulled:
		currencyObj = []
		for keys in i:
			if keys == "name":
				currencyObj.insert(0, i[keys])
			elif keys == "percent_change_24h":
				currencyObj.insert(1, round(float(i[keys]),1))
			elif keys == "price_usd":
				currencyObj.insert(2, '$' + str(round(float(i[keys]),2)))
			elif keys == "symbol":
				currencyObj.insert(3, i[keys])
			elif keys == "rank":
				currencyObj.insert(4, 'rank: ' + i[keys])
		unsortedArray.append(currencyObj)
	print(sorted(unsortedArray, key=operator.itemgetter(1), reverse=True))


infoPulled(5)

