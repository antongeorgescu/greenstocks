# Greenstocks Investment Advisor (GIA)

## About GIA
<mark>Greenstocks Investment Advisor (GIA) is an online application powered by machine learning algorithms, that facilitates reliable stock market investments in companies that implement a high Environmental, Social and Governance policy.</mark>

## What is ESG Investing
<mark>ESG stands for Environmental, Social, and Governance. Investors are increasingly applying these non-financial factors as part of their analysis process to identify material risks and growth opportunities.</mark> ESG metrics are not commonly part of mandatory financial reporting, though companies are increasingly making disclosures in their annual report or in a standalone sustainability report. Numerous institutions, such as the Sustainability Accounting Standards Board (SASB), the Global Reporting Initiative (GRI), and the Task Force on Climate-related Financial Disclosures (TCFD) are working to form standards and define materiality to facilitate incorporation of these factors into the investment process.

![ESG_Explained](https://user-images.githubusercontent.com/6631390/161564529-8be8cf16-98a6-47b4-90d8-818cae6eebb4.JPG)

## Machine Learning in Smart Finances
<mark>As an application of artificial intelligence, machine learning focuses on developing systems that can access pools of data, and the system automatically adjusts its parameters to improve experiences. Computer systems run operations in the background and produce outcomes automatically according to how it is trained.Nowadays, many leading fintech and financial services companies are incorporating machine learning into their operations, resulting in a better-streamlined process, reduced risks, and better-optimized portfolios.</mark>

<mark>Our Greenstocks Investment Advisor tool allows intelligent Stock Trading Portfolio Management by using advanced machine learning algorithms from Natural Language Processing (NLP) space.</mark>

## Greenstocks Investment Advisor Features
<mark>While the user is in charge with selecting the industry, the secor and the stock, the application is doing the rest: it calculates the <i>green score</i> and provides investment recommendation.

The green scores are calculated in two ways, for enhanced accuracy, and represenets the percentage of "green tokens" (driven by an ever growing dictionary) out of "article tokens." The current score categories are encoded to range of numbers (&) as following:

* Poor: 0-4%
* Decent: 5-9%
* Good: 10-19%
* Excelent: >= 20%
</mark>
### Overall Functionality
<mark>Greenstocks Investment Advisor (GIA) is built as a simple,user friendly web application that allows the user, through only a few clicks, to discover and invest in stocks that comply to ESG policies.</mark> Down below you can see a normal use of the prototype that we built.
<u>Note:</u>&nbsp;Since this is only a prototype, we have left aside a bunch of features that are important and can be further developed, like:
+ Batch Inference that run batch jobs in the background (i.e. GIA Business Engine) to identify the shorter list of stocks with both ESG and ROI
+ Data persistance that saves both user preferences and high ESG/ROI stocks for further use and monitoring
+ Replace yFinance investment recommendation with a GIA contained ML algorithm that is using linear regression predictions applied to stock time series.
+ Replace both NLP and Linear Regression Algorithms running locally with Azure machine learning (either core or Azure Databricks based) 
+ Add to dashboard a component that allows the user to manage and customize the "green token dictionary" (currently refreshed from NLTK source repsoitory every time the application runs)
+ Add to dashboard a component that allows the user to manage the range of numbers (%) for the 4 categories of <i>green score</i> we currently offer: excellent, good, decent, poor.

### An Example of Normal Use
The following set of screenshots are captured from running GIA against an iPhone 12 Pro screen emaulator.

+ User browses a list of industries subject to single selection<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Select_Industry](https://user-images.githubusercontent.com/6631390/161561116-51bb2fb2-64b3-40f3-ba9b-73b4c2e6169c.JPG)

+ After selecting the industry, the user will pick up the stock they are interested in<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Select_Stock](https://user-images.githubusercontent.com/6631390/161561195-5ece4308-8fc8-47d2-b57e-15a756e65098.JPG)

+ If the selected stock's green score is between 10-19% the following layout is displayed. The layout contains both the <i>green score</i> and the stock performance during the last 30 days:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Good_Green_Score](https://user-images.githubusercontent.com/6631390/161561264-3884d9e0-7713-45ce-a92b-3d28548336d1.JPG)

+ If the selected stock's green score is between 5-9% the following layout is displayed:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Decent_Green_Score](https://user-images.githubusercontent.com/6631390/161561318-a57137c6-81dc-4a00-9909-eb7a0328b438.JPG)

+ If the selected stock's green score is between 0-4% the following layout is displayed:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Poor_Green_Score](https://user-images.githubusercontent.com/6631390/161584103-dbd9150a-8786-4494-9573-08eb56f60f14.JPG)

## Design, Implementation and Deployment

### Basic Design
<mark>GIA design is N-tier, microservices based.</mark> It includes the following functional layers:
1. Web GIA Dashboard as single-page application (SPA) implemented with Angular javascript framework</mark>
2. REST API layer implemented with Python Flask</mark>
3. Business Engine implemented with Python libraries (incl NPL library)</mark>
4. yFinance Stock Trading API </mark>
5. Web articles space</mark>

<mark>GIA Dashboard has a responsive design that allows it to adapt seamlessly to both desktop and mobile formats
Business Engine contains the MVC model functionality. It includes a powerful Natural Language Processing (NLP) library based on Python NLTK (Matural Language Toolkit). <br/>
NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.
GIA Business Engine has also a web scrapper, based on Python's BeautifulSoup package, that allows it to extract structured stock information from yFinance API. <br/>
</mark>


![Basic_Design](https://user-images.githubusercontent.com/6631390/161576879-34cd90be-7bc3-43fb-8b77-70962586453e.jpg)


### Application Flow
The following diagram shows the set of basic workflow (set of steps) required to calculate the "green score" attached to a stock, and show performance information. These elements altogether allows the investor to execute an educated investment, that is driven by both ESG and ROI decision factors.
![Application_Flow](https://user-images.githubusercontent.com/6631390/161577206-c66a3cc0-5186-4baf-ad9b-56a630261d3f.jpg)

### Code Source Control
The code is currently saved in Github, under repository located under https://github.com/antongeorgescu/greenstocks

### Create Greenstocks Running Environment

#### Install python 3.7.9

* Make sure there is no previous Python installation; if there is, remove it
* Download python 3.7.9 (64-bit) and install it in <b>C:\Program Files\Python37</b> folder
* Update PC's <b>Environment Variables</b> by adding to PATH (System) the following two lines:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">C:\Program Files\Python37</span></br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">C:\Program Files\Python37\Scripts</span>

####  Create Greenstocks project   
* Clone the repository https://github.com/antongeorgescu/greenstock to &lt;Greenstocks_Home&gt;
* Use the following credentials (HTTPS):
    user: antongeorgescu@gmail.com
    pwd(token): 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

#### Start Greenstocks REST API
* Go to directory &lt;Greenstocks_Home&gt;/restapi and open a Terminal (cmd prompt)
* Run command <span style="color:lightblue">python -m venv dev</span></br>
    This will create a <span style="color:lightblue">restapi\dev folder</span>
* Open restapi\dev\pyvenv.cfg file and make sure the following content is there:</br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">home = C:\Program Files\Python37</span></br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">include-system-site-packages = false</span></br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">version = 3.7.9</span></br>
* Activate dev venv by running the following command in restapi folder:</br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">.\dev\scripts\activate</span></br>
    After the command is done, the following line shows up: </br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">(dev) &lt;Greenstocks_Home&gt\restapi</span>
* Start Flask REST API by running the following:<br/>
    1) set 'host' and 'port' in app.py (last line)
        Example:<br/>
        <span style="color:lightblue">if ` __`name`__` == `__`main`__`:</br></span>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">app.run(host='127.0.0.12', port =5099,debug=True)</span></br>
    2) execute the following line in command prompt:</br>
        <span style="color:lightblue">python app.py</span>

#### Quick testing of Greenstocks REST API
* Open any browser and run the following URLs:<br/>
    http://127.0.0.1:5000/api/v1/resources/stocks/sector/list <br/>
    http://127.0.0.1:5000/api/v1/resources/stocks/sp500/profile/True

#### Create a Reverse Proxy from IIS to Python Flask
Reverse Proxy allows client calls (eg SPA with React or Angular) being directed to IIS web site GreenstocksApi, and from there re-directed to Flask REST API</br>
To do that execute the following steps:</br>
* Create web site <span style="color:lightblue">GreenstocksApi</span> in Windows 10 IIS</br>
    This web site has its physical path in &lt;Greenstocks_Home&gt;/iis-restapi</br>
* After the site is created and running on port 8080 (for example), create the Reverse Proxy by following the instructions in the article <b>Creating a Reverse Proxy with URL Rewrite for IIS</b> at the link https://weblogs.asp.net/owscott/creating-a-reverse-proxy-with-url-rewrite-for-iis
* Test the newly created reveres proxy by opening any browser and running the following URLs:<br/>
    http://localhost:8080/api/v1/resources/stocks/sector/list <br/>
    http://localhost:8080/api/v1/resources/stocks/sp500/profile/True




