import pytest
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_different_names(go_to_my_pets):
    '''Проверяем на отсутствие дубликатов имен у питомцев пользователя'''
    # установка неявного ожидания
    pytest.driver.implicitly_wait(5)

    # находим все имена
    names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')

    # задаем пустой список и счетчик
    pets_names = []
    r = 0

    # добавляем имена в список
    for name in names:
        name = name.text
        pets_names.append(name)
        print()
        print(pets_names)
        print('name=', name)

        # проверяем количество питомцев с таким же именем среди уже имеющихся элементов
        # При r != 1 выходим из цикла
        r = pets_names.count(name)
        if r != 1:
            break

    # проверяем, если r == 1, то повторяющихся имен нет.
    assert r == 1, "Есть питомцы с идентичными именами"
