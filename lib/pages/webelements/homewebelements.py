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
    
    list_menu =  (By.CLASS_NAME, "HtHs-nav-list")
    flights_button = (By.XPATH, "//a[@class='dJtn dJtn-active dJtn-expanded dJtn-mod-variant-accordion' and contains(@aria-label, 'Buscar vuelos') and @aria-current='page' and @tabindex='-1']")
    stays_button = (By.XPATH, "//a[@href='/stays' and @aria-label='Buscar hoteles ' and @class='dJtn dJtn-expanded dJtn-mod-variant-accordion' and @aria-current='false' and @tabindex='-1']")
    cars_button = (By.XPATH, "//a[@href='/cars' and @aria-label='Buscar autos ' and @class='dJtn dJtn-expanded dJtn-mod-variant-accordion' and @aria-current='false' and @tabindex='-1']")
    citybreaks_button = (By.XPATH, "//a[@href='/citybreaks' and @aria-label='Buscar vacaciones ' and contains(@class, 'dJtn-expanded') and contains(@class, 'dJtn-mod-variant-accordion') and @aria-current='false' and @tabindex='-1']")
    