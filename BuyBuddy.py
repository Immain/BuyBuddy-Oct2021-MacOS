##################################
# INFORMATION 
##################################
# The CSS Selector links are subject to change, as bots are usually detected through Bestbuy.com ( If the code fails to run, then something has changed on the site)

## REQUIREMENTS ##
# First you will need to install Python (this script is running 3.9.7) you can download it here. https://www.python.org/downloads/
# Next you will need to download Selenium, to do this, open terminal and run pip3 install selenium 
# Once selenium is installed, you will want to open chrome and see which version you are running. Current version is 93.0.4577.82 
# Next, download the chromedriver file and unzip it into your destination folder (https://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.63/)
# In the info.py file, you will need to put in your bestbuy login credentials and the CVV of the card you will be using for purchases (this is needed for fast track checkout)
# Lastly, save your files and open the script in Visual Studio Code, them go to the top bar and select "Run" and then "Run without debugging"

# Documentation Links #
# Python: https://www.python.org/downloads/
# Selenium: https://selenium-python.readthedocs.io/
# Chrome Driver: https://sites.google.com/chromium.org/driver/

##################################
# SCRIPT START
##################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import info

# make sure this path is correct and in the correct folder
PATH = "/Users/Example/Desktop/BuyBuddy/chromedriver"

driver = webdriver.Chrome(PATH)


# Links (Can only run one at a time, unless you rename script) - Comment out the one you want and the others you don't. Then give it a path name RTX3080 = "link"

#RTX3060TI = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402"
#RTX3070TI = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789"
RTX3080 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
#XBOXSERIESX = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324"
#XBOXLIMITEDED = "https://www.bestbuy.com/site/microsoft-xbox-series-x-halo-infinite-limited-edition-black/6477938.p?skuId=6477938"
#PLAYSTATION5DISK = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
#PLAYSTATION5DIGI = "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161"
#RX6600 = "https://www.bestbuy.com/site/xfx-speedster-qick308-amd-radeon-rx-6600-xt-8gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6474679.p?skuId=6474679"
#RX6700XT = "https://www.bestbuy.com/site/xfx-speedster-qick319-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6460664.p?skuId=6460664"


# Make sure the item within the () matches what you have above. 
driver.get(RTX3080)

# Don't touch this
isComplete = False

while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue

    print("Add to cart button found")

    try:
        # add to cart
        atcBtn.click()

        # go to cart and begin checkout as guest
        driver.get("https://www.bestbuy.com/cart")
        checkoutBtn = driver.find_element_by_class_name("btn-lg")
        checkoutBtn.click()
        print("Successfully added to cart - beginning check out")

        # fill in email and password
        emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailField.send_keys(info.email)

        pwField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        pwField.send_keys(info.password)

        # click sign in button
        signInBtn = checkoutBtn = driver.find_element_by_class_name("c-button-lg")
        signInBtn.click()
        print("Signing in")

        # fill in card cvv
        cvvField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cvv"))
        )
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")

        # place order
        placeOrderBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-block.btn-primary.button__fast-track"))
        )
        placeOrderBtn.click()

        isComplete = True
    except:
        # make sure this link is the same as the link passed to driver.get() before looping
        driver.get(RTX3080)
        print("Error - restarting bot")
        continue

print("Order successfully placed")


##################################
# SCRIPT END
##################################
