import pytest
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By

def test_show_name_age_species(go_to_my_pets):
   '''Проверяем карточки питомцев на наличие имени, возраста и породы'''

   # установка неявного ожидания
   pytest.driver.implicitly_wait(5)

   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   for i in range(len(names)):
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0