from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


def task1_a():
    try:
        print("____________________task1_a START ____________________")
        driver_path = 'C:\\Users\\Armen Boiadzhian\\PycharmProjects\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get("https://www.teb-akademia.pl/o-nas")
        name = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Prezes Zarządu')]/../h2")))[0].text
        print('Prezes Zarządu:', name)
    except Exception as e:
        print("Error occurred during running")
        print("Log:", e)
    finally:
        driver.close()
        print("____________________task1_a END ____________________")


def task1_b():
    try:
        print("____________________task1_b START ____________________")
        driver_path = 'C:\\Users\\Armen Boiadzhian\\PycharmProjects\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get(
            "https://www.wsb.pl/poznan/studia-i-szkolenia/studia-i-stopnia/kierunki-i-specjalnosci/informatyka/ceny")

        fixed_12 = driver.find_elements(By.XPATH,
                                        "//*[@id='fixed']/../..//*[contains(text(), '12 rat')]/../../tr//span")

        prices = " "

        for el in fixed_12:
            prices += el.text + " "
        price_list = prices.replace(")", ")\n").split("\n")

        # I YEAR
        try:
            assert "575 zł" in price_list[0], "Error in I year: should be '575 zł (12 x 575 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[0])

        try:
            assert "(12 x 575 zł)" in price_list[0], "Error in I year: should be '575 zł (12 x 575 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[0])

        # II YEAR
        try:
            assert "575 zł" in price_list[1], "Error in II year: should be '575 zł (12 x 575 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[1])

        try:
            assert "(12 x 575 zł)" in price_list[1], "Error in II year: should be '575 zł (12 x 575 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[1])

        # III YEAR
        try:
            assert "575 zł" in price_list[2], "Error in III year: should be '575 zł (12 x 575 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[2])

        try:
            assert "(12 x 575 zł)" in price_list[2], "Error in III year: should be '575 zł (12 x 575 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[2])

        # IV YEAR
        try:
            assert "675 zł " in price_list[3], "Error in IV year: should be '575 zł (12 x 575 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[3])

        try:
            assert "(5 x 675 zł)" in price_list[3], "Error in IV year: should be '575 zł (12 x 575 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[3])


    except Exception as e:
        print("Error occurred during running")
        print("Log:", e)
    finally:
        driver.close()
        print("____________________task1_b END ____________________")


def task1_c():
    try:
        print("____________________task1_c START ____________________")
        driver_path = 'C:\\Users\\Armen Boiadzhian\\PycharmProjects\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get(
            "https://www.wsb.pl/warszawa/studia-i-szkolenia/studia-i-stopnia/kierunki-i-specjalnosci/bezpieczenstwo-wewnetrzne/ceny")

        fixed_12 = driver.find_elements(By.XPATH,
                                        "//*[@id='graded']/../..//*[contains(text(), '12 rat')]/../../tr//span")

        prices = " "

        for el in fixed_12:
            prices += el.text + " "
        price_list = prices.replace(")", ")\n").split("\n")

        # I YEAR
        try:
            assert ("300 zł" or "380 zł") in price_list[0], "Error in I year: should be '300 zł 380 zł (12 x 330 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[0])

        try:
            assert "(12 x 330 zł)" in price_list[0], "Error in I year: should be '300 zł 380 zł (12 x 330 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[0])

        # II YEAR
        try:
            assert "475 zł" in price_list[1], "Error in II year: should be '475 zł (12 x 475 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[1])

        try:
            assert "(12 x 475 zł)" in price_list[1], "Error in II year: should be '475 zł (12 x 475 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[1])

        # III YEAR
        try:
            assert "675 zł" in price_list[2], "Error in III year: should be '675 zł (10 x 675 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[2])

        try:
            assert "(10 x 675 zł)" in price_list[2], "Error in III year: should be '675 zł (10 x 675 zł)'"
        except AssertionError as asrt:
            print("Bug was found")
            print("Log:", asrt, " | INSTEAD | ", price_list[2])

    except Exception as e:
        print("Error occurred during running")
        print("Log:", e)
    finally:
        driver.close()
        print("____________________task1_c END ____________________")


sys.stdout = open('D:\\Downloads\\Result.txt', 'w', encoding="utf-8")
task1_a()
task1_b()
task1_c()
