from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.XPATH, "//div[contains(@class, 'ui-layout-HeaderMainLogo')]")
    signin_button = (By.XPATH, "//div[@role='button' and contains(@class, 'ZGw-') and contains(@class, 'ZGw--mod-size-medium')]")
    search_button = (By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')
    
    # Agregar Selectores XPHAT, fallaba la prueba por no tenerlo, se agregaron nuevos los del feature no se encontraban
    logo_input = (By.XPATH, "//div[contains(@class, 'ui-layout-HeaderMainLogo')]")
    title_text = (By.XPATH, "//h2[contains(@class, 'P4Ui-title') and contains(@class, 'P4Ui-mod-theme-dark')]")
    login_button = (By.XPATH, "//div[@role='button' and contains(@class, 'ZGw-') and contains(@class, 'ZGw--mod-size-medium')]")
    favorite_button =(By.XPATH, "//span[@class='drawer-trigger-svg' and @aria-hidden='true']")
    
    list_menu =  (By.CLASS_NAME, "HtHs-nav-list")
    flights_button = (By.XPATH, "//a[contains(@class, 'dJtn') and @href='/flights' and @aria-label='Buscar vuelos ' and @aria-current='page' and @tabindex='0']")
    stays_button = (By.XPATH, "//a[@href='/stays' and @aria-label='Buscar hoteles ' and @class='dJtn dJtn-expanded dJtn-mod-variant-accordion' and @aria-current='false' and @tabindex='-1']")
    cars_button = (By.XPATH, "//a[@href='/cars' and @aria-label='Buscar autos ' and @class='dJtn dJtn-expanded dJtn-mod-variant-accordion' and @aria-current='false' and @tabindex='-1']")
    citybreaks_button = (By.XPATH, "//a[@href='/citybreaks' and @aria-label='Buscar vacaciones ' and contains(@class, 'dJtn-expanded') and contains(@class, 'dJtn-mod-variant-accordion') and @aria-current='false' and @tabindex='-1']")
    
    # Test