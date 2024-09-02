# Python-Test-Automation-Framework 

# Description

Test Automation Framework using selenium, Pytest and Python with the below features:

- Framework is based on page object model.
- Locator Management: All locators are centralized in the Pages/Locators.py file for easy maintenance.
- Allure Reporting: Generates detailed, visually appealing test reports.


# Install dependences

- Install the depended packages in `requirements.txt` using `pip3 install -r requirements.txt`

#  test Scenarios
Created 2 test cases as part of this framework.

Test1: Search iphone14 in flipkart search box and fetch the price
Steps:
    1. Launch "https://www.flipkart.com/" URL
    2. Enter user input ("iphone 14") in search box
    3. Validate user desired iphone is present at page
    4. Validate the price of iphone

Test2:  Search Samsung Mobile in flipkart and add to cart and validate price 
Steps:
    1. Launch "https://www.flipkart.com/" URL
    2. Enter samsung user input ("Samsung S24 ultra") in search box
    3. Click on Samsung S24 ultra mobile, it redirects to next tab.
    4. click on add to cart option
    5. Validate card value is same as mobile value

# Test Execution

Test will run with chrome and edge browser.  

To execute the test cases, use the following command:
```
pytest --alluredir=Reports
```

You can then generate and view the Allure report with:
``` 
allure serve Reports
```

For parallel execution use below commands:
``` 
pytest -n 4 --alluredir=Results
```

