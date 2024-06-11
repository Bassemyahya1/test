import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from jproperties import Properties
from selenium.webdriver.common.by import By

# Read properties from environment.properties file
from selenium.webdriver.support.wait import WebDriverWait

configs = Properties()
with open(r'C:\Users\basse\PycharmProjects\allure-python\allure-behave\environment.properties', 'rb') as config_file:
    configs.load(config_file)
Email = configs.get("Email").data
User_Login = configs.get("User_Login").data
User_Password = configs.get("User_Password").data
Supplier_Login_PPD = configs.get("Supplier_Login_PPD").data
Supplier_Password_PPD = configs.get("Supplier_Password_PPD").data


# Start the Feature


@when(u'the user set the filters "{country}" "{number}"')
def step_impl(context, country, number):

    # Click the access portal button
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/span').click()
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH, r'//*[@id="field-country"]/label[' + number + ']/span').click()
    print(country)
    context.browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/button').click()
    context.browser.implicitly_wait(10)
    # context.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/div/button"]').click()

    try:
        WebDriverWait(context.browser, 200).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                                                      '#lk-react-container > div > div > div > section > div > div.Box-sc-5738oh-0.dBYxpC.DashboardHeaderContainer__InternalDashboardHeaderContainer-sc-1lnkdqd-0.kNTtXK > div > div > div.Box-sc-5738oh-0.DashboardHeaderMenu__Container-sc-1w7j53l-0.bIZvBa.fIGzfT > div > div > button')))
        # context.browser.execute_script('return document.readyState;')
        print("hi")

    finally:
        print('loader disappeared')
        time.sleep(5)

        print("hi")
        context.browser.switch_to.frame(context.browser.find_element_by_id("categories-sales-analysis-iframe"))
        time.sleep(2)

@then(u'Tiles promotion sales insights x sales amount are well displayed')
def step_impl(context):

        time.sleep(5)
        context.browser.execute_script("document.getElementById('dashboard-layout-wrapper').scrollBy(0,1000)")
        time.sleep(2)

        # Supplier sales amount,

        # context.browser.find_element(By.ID,'dashboard_button_for_element_33bfe5c88ba55cae93594016c21de807""]').click()
        # comment = context.browser.find_element(By.XPATH,'//*[@id="dashboard-layout-wrapper"]/div[1]/div/div[17]/div/section/div/div[1]/h2/div').text
        # print(comment)
        # time.sleep(5)
        # INSTANT_COFFEES= context.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[12]/div/section/div/div[2]/div[3]/div[4]/span[4]').text
        # print(INSTANT_COFFEES)
        HOT_BEVERAGES =context.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[13]/div/section/div/div[2]/div[3]/div[4]/span[11]').text
        print(HOT_BEVERAGES )
        time.sleep(3)

        #
        # #Categories sales amount
        #
        STILL_WATER=context.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[13]/div/section/div/div[2]/div[3]/div[4]/span[1]').text
        print(STILL_WATER )
        time.sleep(3)

        # #Evolution categories & supplier sales amount (%)
        #
        FROZEN_PIZZAS = context.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[13]/div/section/div/div[2]/div[3]/div[4]/span[8]').text
        print(FROZEN_PIZZAS)
        time.sleep(3)
        context.browser.execute_script("document.getElementById('dashboard-layout-wrapper').scrollBy(0,700)")
        time.sleep(5)
        # Evolution supplier sales amount by period (%)

        perc = context.browser.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[14]/div/section/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/span[1]').text
        #
        print(perc)
        perc1 = context.browser.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[14]/div/section/div/div[2]/div[2]/div/div[1]/div[1]/div/p'
                                             ).text
        #
        time.sleep(2)

        # svg_item = context.browser.find_element(By.CSS_SELECTOR,
        #                                          '#highcharts-yxex41o-1304 > svg > rect.highcharts-background')
        # time.sleep(2)

        # svg_url = svg_item.get_attribute('data')
        # svg_item = context.browser.find_element(By.CSS_SELECTOR,
        #                                           '#highcharts-j9t9k4j-0 > svg:nth-child(2) > g:nth-child(16) > g:nth-child(4) > text:nth-child(1) > tspan:nth-child(1)')
        print("hi")
        print([my_elem.text for my_elem in WebDriverWait(context.browser, 20).until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "svg:nth-child(2) tspan")))])
        print(perc1)
        print(perc)

# End of the feature
