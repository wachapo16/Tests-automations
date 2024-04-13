from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, '.primary-content h2')
    signin_button = (By.CSS_SELECTOR, '.menu__wrapper .menu-label__wrapper button')
    search_button = (By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')
    
    # Agregar Selectores XPHAT, fallaba la prueba por no tenerlo, se agregaron nuevos los del feature no se encontraban
    logo_input = (By.XPATH, "//div[contains(@class, 'main-logo__logo') and contains(@class, 'has-compact-logo')]")
    title_text = (By.XPATH, "//h2[@class='title dark' and contains(text(), 'Busca en cientos de webs de vuelos a la vez')]")
    login_button = (By.XPATH, "//div[@class='auth-account-wrap menu__wrapper']//button[contains(@class, 'Button-No-Standard-Style')]")
    favorite_button =(By.XPATH, "//button[@class='trips-drawer-trigger triggerV2' and @aria-label='Abrir Trips']")
    