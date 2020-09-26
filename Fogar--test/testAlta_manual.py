import unittest
from selenium import webdriver
from FOGAR_page_object.pagelogin import PageLogin
from FOGAR_page_object.pagedash import PageDash
from FOGAR_page_object.pagecliente import PageCliente
from FOGAR_page_object.pageguarantee import PageGuarantee
import time
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        #option.add_argument("start-maximized")
        #option.add_argument("incognito")
        #option.add_argument("--headless")
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver',
                                       chrome_options=option)
        
        self.driver.get('http://dev-guaranteefunds.mobeats.com.ar')
        self.driver.implicitly_wait(45)
        self.loginPage = PageLogin(self.driver)
        self.dashPage = PageDash(self.driver)
        self.clientePage = PageCliente(self.driver)
        self.guaranteePage = PageGuarantee(self.driver)


    def test_LG_PREP(self):
        self.loginPage.search('20263000006', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '1942', '28-08-2020', '01-12-2020', '12', '14-12-2020', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        self.guaranteePage.guardar()
        time.sleep(8)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
