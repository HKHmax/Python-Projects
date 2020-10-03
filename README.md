# Python-Projects
## This file includes all the python projects done by Max Hong Ka Ho and I am going to introduce you with the projects I have done so far: (In chronological order of finishing)
## It mainly targets python application to finance especially testing of algorithmic trading strategies, Big Data as well as Data Science projects

1. Predict Future HSI Stock Price Using Facebook Prophet:

This project uses a famous machine learning library - Facebook Prophet, I employ it to predict the HSI index price(the stock index of HKEX) where input is past stock prices and output is future stock prices. From this paper, I would shed light on whether this library works well in stock predictions which is an extremely complex system in real life.

2. Predict Stock Price Using Tensorflow and Scikit-Learn:

This is a project with integration of deep learning, statistics, and finance. In our real life, we may easily find some stock csv files. However, can we build a model that inputs some common data like past Open, High, Low, Close, Volume and output the future close prices? We would embark on our journey to make one! The project here uses neural network in deep learning, multiple regression, random forest, and decision-making trees model with HSI data. They all have the same inputs in this experiment and output tomorrow's stock price. Detailed comparison in the 4 models will be studied with the help of statistical measures like accuracy, R-squared, MSE, etc.

3. Applying Neural Network to Construct a Trading Strategy In Stock:

This is based on the Neural Network Model built last time and I use it as trading signals in HSI. Besides, a simulation of wealth to follow the signal has been made to testify whether our model is reliable or not

4. Pair Trading Strategy For Apple And Microsoft:

Pair Trading is a renowned trading strategy making decisions to buy and sell two pair of stocks after sophisticated mathematical analysis namely the cointegration and correlation analysis with sets of underlying assumptions need to be tested in order to make the results robust in practice. I would display how to use python on executing the model in real life. It starts from using hypothesis testing to testify whether the assumptions hold, then goes on with a few steps of standardization of data. Finally, back test have been done on the test data.

5. Create Candlestick Chart and Capture Some Common Price Patterns With S&P500:

Candlestick chart is a ubiquitous tool using by many traders to summarize the day's high, low, open, and close respectively on a candle. Price patterns (for instance Doji, Morning Stars) are the specific shapes and combinations of candlesticks which yield different meanings like reversal, continuation, etc. Many people try to discern those patterns with naked eyes but is there any objective ways to identify them and place orders accordingly? In this project, I would show you how to capture them with codes in a clever manner!

6. Momentum Trading On Tencent

MTM(Momentum) is a stock indicator calculating the momentum of stock price movements. The changing sign of momentum marks the outset of another trend as perceived by many day traders. Here Tencent will be our experimental data set we attempting to back test with, its performance can be found in the project page. Parameter optimizations have been performed to filter the best parameters used in MTM (i.e. the period of MTM) in order to give us the highest expected value, accuracy, Sharpe ratio and minimum Max Drawdown, etc.

7. Trade Google With RSI

RSI (Relative Strength Index) is a useful tool in spotting out whether the stocks are overbought / oversold. Under the erratic market movements, we are trying to catch the turning points of trend with overbought / oversold signal of RSI. Parameter optimizations have also been performed to filter the best parameters used in RSI (i.e. the period of RSI) to give us the highest expected value, accuracy, Sharpe ratio and minimum Max Drawdown, etc.

8. Simple Moving Average On Trading FaceBook

Simple Moving Average (SMA) is the smoothing price of stock. From all accounts, SMA crossover is one of the oldest strategies used by traders. This time, I would test the SMA crossover strategies with Facebook historical stock prices. In the second part of project, I would focus on another function of SMA: used as trend filtering, specifically speaking, to distinguish the bull and bear market where we would long (short) the stock until the price drop below (rise above) the SMA.

9. Youtube Downloader

This is a project with different natures as the above mentioned and it is a big data project. I have customized a program for the users to download YouTube videos. Some useful libraries are used in the program such as pytube and re which assists me to retrieve the html code in YouTube and download videos. What's worth mentioning is that I have created it to a tailor-made program which has the following functions: 1) Enable users to choose whether they want to download the sound track or video 2) To choose whether they want to download the subtitles 3) Allow the users to choose their own saving directory 4) Enable to download the whole playlist but not a single video which saves us lots of time

10. Use Web-scraping Techniques to Massively Extract Whatsapp Stickers

It is a web scraping project which displays the readers how we can effectively retrieve information from a webpage in which this experiment uses WhatsApp stickers webpage. I have shown in detail with pictures on how to analyze the HTML code inside a website to choose the right location with Python code. At first, I start with a particular sticker page and save the stickers in new files which all are done automatically. Then, I make the code more generalized to start with the main page. The program itself will automatically click in a particular stick category and crawl all the stickers in that page + new folder is created for each new page so that we can easily manage the data.

11. Crawl Images From Website With ASPX Structure -- Google Images

This project demonstrates some advanced techniques on how Data Scientists can use Selenium and BeautifulSoup library to mimic a Google Chrome object, and then ask the chrome object to scroll down automatically in order to beat the APSX structure of websites(For what is ASPX, please refer to my project). With this tactic, we can try to crawl all the images from the Google Images engine in a clever way since it is a website which updates its HTML with request and always perceived as a difficult type of website to handle in web-scraping.

12. Extract News Articles From Times To Local Excel File

Saving the news articles extensively from an online news website is always perceived as a time-consuming task. To solve this problem, I use TIMES news articles as our testing targets and write a complete program (in exe file) to extract the news articles + compile them into an organized excel file for storage. There are 4 main features in the program: 1) Users can choose the category of news to download according to the TIMES classification (e.g. Economy) 2) Users can specify the pages to download in TIMES web (e.g. 3-5) 3) Users can designate the directory to save all the articles in excel file 4) All the data are real-time crawling and can automatically write in the excel with 4 columns including header, date, author and whole article.

13. Create News Articles Summary from TIMES News Downloader

Serving as the second part of the previous project. I further extend the News downloader built in last project and combine it with NLP(Natural Language Processing) technique in order to generate news summary alongside our scraping process. It saves the users much time in reading redundant details.





People who are interested can feel free to play with the code written by me


**WARNING: IF YOU WANT TO CITE MY CODE TO OTHER WEBSITES, PLEASE LET ME KNOW AND PLEASE PASTE MY ORIGINAL GITHUB LINK ON THAT**
