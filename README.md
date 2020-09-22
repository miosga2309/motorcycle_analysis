# Informed purchase of a motorcycle
This project is supposed to be an analysis of the current motorcycle market with regard to a few models I might be interested in to buy for myself. All motorcycles are more or less classic bikes or scramblers, have two cylinders and ABS.

## Models:
- Ducati Scrambler Icon Dark
- Ducati Scrambler Icon
- Ducati Scrambler Sixty2
- Moto Guzzi V7 III
- Moto Guzzi V9
- Royal Enfield Interceptor 650
- Yamaha XSR 700

## Progress:
**29/08/2020**: I have requested API keys for two car and motorcycle market places in the German area, [mobile](https://www.mobile.de/) and [autoscout24](https://www.autoscout24.de/).

**31/08/2020**: Testing a probably less stable version of information access by scraping the webpage with certain results manually, using beautifulsoup in Python. **UPDATE**: [mobile](https://www.mobile.de/) does not allow for that kind of scraping. It explicitly states that one has to use the API provided by them. Perhaps there are ways to bypass the defense mechanisms but let's wait for their reply on my API key request.

**01/09/2020**: [mobile](https://www.mobile.de/) replied that APIs are only provided for business customers and the basic monthly costs are already EUR 500. Well, that's not an option for me.

**01/09/2020**: I copied the source code of the relevant HTML objects from five pages of results for the Royal Enfield Intercepter 650 into the text file [mo_re_01092020.txt](https://github.com/miosga2309/motorcycle_analysis/blob/master/mo_re_01092020.txt) which now serves as my static, momentum-like scrape from [mobile](https://www.mobile.de/). The extraction of the relevant parts is done in [moto_scrape.py](https://github.com/miosga2309/motorcycle_analysis/blob/master/moto_scrape.py).

**22/09/2020**: I need to repeat the manual source extraction several times to get a bigger dataset. Most offers are new bikes and do only vary in price but obviously not in first registration date and mileage. Probably, I will use new bike offers only to calculate the mean price for that particular model which is useful because prices are mostly a lot different than advertised on the manufacturer's homepage. For retrieving used bikes again at later stages, I would have to give each offer an individual key so that I won't have duplicates in my data. However, offers that have a change in price will be handled as new offers since the price may be connected to increasing age or to a overly high entry price. Particularly the increasing age should be reflected by a decreasing price.
