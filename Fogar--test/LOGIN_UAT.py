import unittest #libreria que ejecuta las pruebas propiamente dichas
from selenium import webdriver #libreria que aporta a muchos lenguajes
from pageindex import PageIndex
from pageItems import PageItems
import time


class SearchCases(unittest.TestCase): #las clases se definen con la palabra reservada CLASS

    def setUp(self): #METODO SUTUP:se ejecuta antes de cada prueba (Precondicion)
        self.driver = webdriver.Chrome('/home/daniel/workspaces/fogar-testing/Automation - Clases/chromedriver')
        self.driver.get('http://dev-guaranteefunds.mobeats.com.ar/#/')
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndex(self.driver)  # crea el objeto del tipo PageItems= indexPage

    '''def test_LG_UAT(self): #los metodos se definen con la palabra reservada DEF
        self.indexPage.search('mfontenla')
        time.sleep(6)'''

    def test_LG_UAT(self): #los metodos se definen con la palabra reservada DEF
        self.indexPage.search('mfontenla', 'admin')
        time.sleep(6)





    def tearDown(self): #METODO TEARDOWN: Se ejecuta al terminar cada prueba (post condicio)
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()