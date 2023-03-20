# Understanding data preprocessing
Within this directory exists the files required to preprocess data for building a deep
neural network for sentiment analysis.

# To-do

1. Understand the code written in `collect_reuters.py`. For implementing or setting up
Selenium on your system follow the following [TUTORIAL](https://www.youtube.com/watch?v=SPM1tm2ZdK4)
2. I have implemented the code for the ticker `META`. I would want you all to internally
decide on a few tickers with relevant headlines (at least 5 per head) and check if the code
works for your tickers. (This code takes time to run, and so we will decide on tickers and let\
it run overnight)
   1. Do not change the collect_reuters.py file. However, after you run it in local machine
   make sure that the csv file is working for your tickers.
   2. After the code runs just let me know your final chosen tickers with relevant headlines.
4. Finally, once you are done with this I need you all to write a new script with following functionality
   1. Take my META csv file as a reference for the script. 
   2. Sort the headlines by date. 
   3. Take yahoo finance data for this specific ticker and then add the 
   following data for the column `price_change`. (feel free to use different tolerance)
      1. If price increases/decreases by 5% within the next month then give it -1/1
      2. If price increases/decreases by 10% within the next month then give it -2/2
5. I will also need one of you to please look at the following two forms and help me 
fill out the data needed for the forms and also print them and fill them out before 
the Wednesday. 
   1. https://trec.nist.gov/data/reuters/org_appl_reuters_v4.html
   2. https://trec.nist.gov/data/reuters/ind_appl_reuters_v4.html
6. With this our data preprocessing/collection will be done. 


**NOTE** - I need one person to make a shared google drive and also create a ppt and 
start working on the same. 