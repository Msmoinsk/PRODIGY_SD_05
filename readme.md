# Web Scrapper

## Steps to run the Code

### Step I :
Install Python version 3.8 or above

### Step II :
In terminal run 
```bash
sudo apt-get update
sudo apt-get install python3-tk
pip install tk
pip install beautifulsoup4
pip install pandas
```

### Step III 
in Terminal / CMD run
```bash
python web_scraper.py
```

To see the results 
1. You have Create the HTML file just as same webScraping
2. As the Code is design in such a way that by HTML ( className ) You can acess the HTML contect
3. This Code Doesn't work on the Application That uses JS to Dynamically Populate the HTML Content
4. You you need to provide the (className) for the HTML page to be scrape
5. Note : It only work on the E-commerce app as only this webApp contains these feilds
>> { Product_items, product_name, product_price, product_rating }