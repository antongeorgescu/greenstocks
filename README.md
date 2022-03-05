# Greenstocks Application to Measure Stock "Greanness" Level

## Basic Design
![Basic_Design](https://user-images.githubusercontent.com/6631390/156235497-88ebee1b-2c54-4be7-b619-dcbef5b65490.jpg)

## Application Flow
![Application_Flow](https://user-images.githubusercontent.com/6631390/156803641-8b781d5c-5430-41ea-bcb8-d6d80cf67930.jpg)

## Create Greenstocks Running Environment

### Install python 3.7.9

* Make sure there is no previous Python installation
* Download python 3.7.9 (64-bit) and install it in <b>C:\Program Files\Python37</b> folder
* Update PC's <b>Environment Variables</b> by adding to PATH (System) the following two lines:
    C:\Program Files\Python37
    C:\Program Files\Python37\Scripts

###  Create Greenstocks project   
* Clone the repository https://github.com/antongeorgescu/greenstock to &lt;Greenstocks_Home&gt;
* Use the following credentials (HTTPS):
    user: antongeorgescu@gmail.com
    pwd(token): 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

### Start Greenstocks REST API
* Go to directory &lt;Greenstocks_Home&gt;/restapi and open a Terminal (cmd prompt)
* Run command python -m venv dev
    thus will create a restapi\dev folder
* Open restapi\dev\pyvenv.cfg file and make sure the following content is there:
    home = C:\Program Files\Python37
    include-system-site-packages = false
    version = 3.7.9
* Activate dev venv by running the following command in restapi folder:
    .\dev\scripts\activate
    the following line sjows up: (dev) &lt;Greenstocks_Home&gt\restapi
* Start Flask REST API by running the following command:
    set FLASK_ENV = dev
    flask run

### Quick testing the REST API
* Open any browser and run the following URLs:<br/>
    http://127.0.0.1:5000/api/v1/resources/stocks/sector/list <br/>
    http://127.0.0.1:5000/api/v1/resources/stocks/sp500/profile/True


