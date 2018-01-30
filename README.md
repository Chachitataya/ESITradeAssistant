# ESITradeAssistant
Python Trade Assistant utilizing the ESI API

1/29/2018
Cleaned out old files. First 'real' file will be MainFunctions - name is in progress, better functionality later.
MainFunction can pull buy/sell/all orders for a region, print the (top/bottom) 4 (order types) from a sorted list of json objects.
It can print this information, and it can also resolve locationID (station ID in a market order) to a solar system/region ID
It can also resolve locationID to a solar system or region NAME. 

====== TO DO LIST ======
SYSTEM Functionality:
A) Write to database or text file (database long-term, text-file mid-term). Store static information in database.
-a1) Holyshit make sure it's normalized at database start, at least third or fifth normalization.
-a2) Static data - region/system IDs and names. 
-a3) Caching permenant data - 'If we don't have a static item, get it and permenantly store it in [table]
-a4) Caching Dynamic data that just gets refreshed every five minutes, and everything else queries the database rather than sending webrequests.
B) HTML/Webpage Input Functionality - make this a webapp that allows input. 

I) Trade Run calculator: Compare buy/sell orders across regions, take input for ship Volume, IMPLEMENT SAFETY TOOLS ('min item checker', maybe price history analysis.)
-i) Find items that are profitable between two systems and show margins after baseline tax, no skills. 
-ii) Buy/Sell orders with basic volume protection and checking 'minimum item requirement'
 
II) Reprocessing/Mineral Arbitrage within system. 
-i) Max Reprocessing Skills, max Taxes/min Standing
-ii) Variable skills, max taxes/min standing
-iii) SSO Auth to pull relevant skills to calculate refine profit. 

Optimization:
-Reduce number of webrequests (See: A through -a4)
-Study optimization - reduce function calls?
-More to come, open-ended goal. 
