# Greenstocks Application to Measure Stock "Greanness" Level

## Basic Design
![Basic_Design](https://user-images.githubusercontent.com/6631390/156235497-88ebee1b-2c54-4be7-b619-dcbef5b65490.jpg)

## Application Flow
![Application_Flow](https://user-images.githubusercontent.com/6631390/156803641-8b781d5c-5430-41ea-bcb8-d6d80cf67930.jpg)

# Create Greenstocks Running Environment

## Install python 3.7.9

* Make sure there is no previous Python installation; if there is, remove it
* Download python 3.7.9 (64-bit) and install it in <b>C:\Program Files\Python37</b> folder
* Update PC's <b>Environment Variables</b> by adding to PATH (System) the following two lines:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">C:\Program Files\Python37</span></br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:lightblue">C:\Program Files\Python37\Scripts</span>

##  Create Greenstocks project   
* Clone the repository https://github.com/antongeorgescu/greenstock to &lt;Greenstocks_Home&gt;
* Use the following credentials (HTTPS):
    user: antongeorgescu@gmail.com
    pwd(token): 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

## Start Greenstocks REST API
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

## Quick testing of Greenstocks REST API
* Open any browser and run the following URLs:<br/>
    http://127.0.0.1:5000/api/v1/resources/stocks/sector/list <br/>
    http://127.0.0.1:5000/api/v1/resources/stocks/sp500/profile/True

## Create a Reverse Proxy from IIS to Python Flask
Reverse Proxy allows client calls (eg SPA with React or Angular) being directed to IIS web site GreenstocksApi, and from there re-directed to Flask REST API</br>
To do that execute the following steps:</br>
* Create web site <span style="color:lightblue">GreenstocksApi</span> in Windows 10 IIS</br>
    This web site has its physical path in &lt;Greenstocks_Home&gt;/iis-restapi</br>
* After the site is created and running on port 8080 (for example), create the Reverse Proxy by following the instructions in the article <b>Creating a Reverse Proxy with URL Rewrite for IIS</b> at the link https://weblogs.asp.net/owscott/creating-a-reverse-proxy-with-url-rewrite-for-iis
* Test the newly created reveres proxy by opening any browser and running the following URLs:<br/>
    http://localhost:8080/api/v1/resources/stocks/sector/list <br/>
    http://localhost:8080/api/v1/resources/stocks/sp500/profile/True




