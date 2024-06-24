import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import locators

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:

# Controlador

    def __init__(self, driver):
        self.driver = driver
# Espera a que aparezca el campo DESDE:
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.from_field))
# Busco y relleno el campo DESDE:
    def set_from(self, from_address):
        self.driver.find_element(locators.from_field).send_keys(from_address)
# Busco y relleno el campo HASTA:
    def set_to(self, to_address):
        self.driver.find_element(locators.to_field).send_keys(to_address)
# Este código me devuelve el valor del campo DESDE:
    def get_from(self):
        return self.driver.find_element(locators.from_field).get_property('value')
# Este código me devuelve el valor del campo HASTA:
    def get_to(self):
        return self.driver.find_element(locators.to_field).get_property('value')
# Busco y hago clic en el botón PEDIR TAXI:
    def click_taxi_button(self):
        self.driver.find_element(locators.taxi_button).click()
#Todas estas acciones juntas:
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.get_from()
        self.get_to()
        self.click_taxi_button()

#Espero hasta que aparezca el botón COMFORT:
    def wait_for_comfort_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.comfort_button))
# Busco y selecciona el botón COMFORT:
    def click_in_comfort(self):
        return self.driver.find_element(locators.comfort_button).click()
    def comfort_button_is_selected(self):
        return self.driver.find_element(locators.comfort_button).is_selected()

# Busco, hago clic en el campo "agregar un número teléfono", se abre ventana emergente,
    def click_telephone_number(self):
        return self.driver.find_element(locators.phone_number_button).click()

# agrego un número de teléfono, hago clic en siguiente
    def add_telephone_number(self,phone_number):
        return self.driver.find_element(locators.phone_number_field).send_keys(phone_number)
    def click_siguiente_button(self):
        return self.driver.find_element(locators.siguiente_button).click()
    def get_telephone_description(self):
        return self.driver.find_element(locators.phone_number_field).text

# Se abre ventana emergente, obtengo código y busco y agrego código, hago clic en confirmar:


    def get_code(self):
        get_phone_code = retrieve_phone_code()
        return self.driver.find_element(locators.code_field).send_keys(get_phone_code)
    def click_in_confirmar_button(self):
        self.driver.find_element(locators.confirmar_button).click()

# Busco y hago clic en "Método de pago", se abre ventana emergente, clic nuevamente en "agregar una tarjeta",
    def click_metodo_de_pago(self):
        return self.driver.find_element(locators.metodo_de_pago_button).click()
    def click_add_card(self):
        return self.driver.find_element(locators.add_card_button).click()

# Busco e ingreso numero de tarjeta de crédito, busco e ingreso código de tarjeta:
    def add_card_number(self):
        return self.driver.find_element(locators.add_card_field).send_keys(data.card_number)
    def add_code_number(self):
        return self.driver.find_element(locators.add_code_card_field).send_keys(data.card_code)

# hago clic en cualquier otro elemento, hago clic en agregar, aparece ventana emergente, busco y clic en "cerrar"
    def click_in_any_other_element(self):
        return self.driver.find_element(locators.any_other_element).click()
    def click_in_agregar(self):
        return self.driver.find_element(locators.agregar_button).click()
    def get_number_credit_card(self):
        return self.driver.find_element(locators.add_card_field).text
    def get_code_credit_card(self):
        return self.driver.find_element(locators.code_field).text
    def click_in_cerrar(self):
        return self.driver.find_element(locators.cerrar_button).click()

#Todo el proceso junto para agregar una tarjeta de credito
    def all_the_process_to_add_credit_card(self):
        self.click_metodo_de_pago()
        self.click_add_card()
        self.add_card_number()
        self.add_code_number()
        self.click_in_any_other_element()
        self.click_in_agregar()
        self.click_in_cerrar()

# Scroll hasta que aparezca en pantalla el campo "Mensaje para el conductor", Busco el campo y Agrego mensaje:
    def search_message_for_driver(self):
        message_driver = self.driver.find_element(locators.message_for_driver)
        return self.driver.scroll_to_element(message_driver)
    def wait_for_message_for_driver(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.message_for_driver))

    def send_message_for_driver(self):
        self.driver.find_element(locators.message_for_driver).send_keys(data.message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(locators.message_for_driver).text

# Scroll hasta que veo "requisitos del pedido", Busco y hago clic en requisitos del pedido

    def search_requisitos_del_pedido(self):
        requisitos_del_pedido = self.driver.find_element(locators.requisitos_del_pedido_button)
        return self.driver.scroll_to_element(requisitos_del_pedido)
    def wait_for_requisitos_del_pedido(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.requisitos_del_pedido_button))
    def click_requisitos_del_pedido(self):
       return self.driver.find_element(locators.requisitos_del_pedido_button).click()

# Scroll, busco y clic la opción de pedir manta y pañuelos.
    def search_manta_y_panuelos(self):
        manta_y_panuelos = self.driver.find_element(locators.manta_y_panuelos_button)
        return self.driver.scroll_to_element(manta_y_panuelos)
    def wait_for_pedido(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.manta_y_panuelos_button))
    def click_in_manta_y_panuelos(self):
        return self.driver.find_element(locators.manta_y_panuelos_button).click()

#Chequear que manta y pañuelos está seleccionado:
    def manta_y_panuelos_is_selected(self):
       return self.driver.find_element(locators.manta_y_panuelos_button).is_selected()

# Scroll, Busco y hago dos veces clic a "Helado":
    def search_icecream(self):
        icecream = self.driver.find_element(locators.helado_button)
        return self.driver.scroll_to_element(icecream)
    def wait_for_icecream_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.helado_button))
    def click_in_icecream(self):
        self.driver.find_element(locators.helado_button).double_click(locators.helado_button)

    def icecream_is_selected(self):
        self.driver.find_element(locators.helado_button).is_selected()

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    # Prueba 1: que los campos DESDE y HASTA se llenaron y guardaron correctamente:
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(10)
        routes_page.wait_for_load_home_page()
        routes_page.set_route(data.from_address, data.to_address)
        assert routes_page.get_from() == data.from_address
        assert routes_page.get_to() == data.to_address


    #Prueba 2: comprueba que se ha seleccionado la opción comfort:
    def test_comfort_button_is_selected(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_comfort_button()
        routes_page.click_in_comfort()
        comfort_is_selected = routes_page.comfort_button_is_selected()
        assert comfort_is_selected == "True"


    #Prueba 3: comprueba que se ha llenado correctamente el campo de numero de telefono:
    def test_telephone_number_field_is_filled(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.add_telephone_number(data.phone_number)
        routes_page.click_siguiente_button()
        routes_page.get_code()
        routes_page.click_in_confirmar_button()
        telephone_description = routes_page.get_telephone_description()
        assert telephone_description == phone_number

    #Prueba 4: Comprueba la funcionalidad de Agregar una tarjeta de crédito. Para que se active el el botón 'link' (enlace) no se activa hasta que el campo CVV
    # de la tarjeta en el modal 'Agregar una tarjeta' pierde el enfoque.
    # Se necesita el código de confirmación requerido para agregar una tarjeta.

    def test_credit_card_is_filled(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.all_the_process_to_add_credit_card()
        assert routes_page.get_number_credit_card() == data.card_number
        assert routes_page.get_code_credit_card() == data.card_code

    #Prueba 5:  Comprueba que se haya guardado el mensaje para el  controlador.

    def test_message_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.search_message_for_driver()
        routes_page.wait_for_message_for_driver()
        routes_page.send_message_for_driver()
        text_message_for_driver = routes_page.get_message_for_driver()
        assert text_message_for_driver == data.message_for_driver


    # Prueba 6: Comprueba si se agrego al pedido una manta y pañuelos.
    def test_manta_y_panuelos_is_selected(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.search_manta_y_panuelos()
        routes_page.wait_for_pedido()
        routes_page.click_in_manta_y_panuelos()
        manta_y_panuelos_is_selected = routes_page.manta_y_panuelos_is_selected()
        assert manta_y_panuelos_is_selected == "True"

    # Prueba 7: Comprueba si se agregaron al pedido 2 helados.

    def add_two_icecream(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.search_icecream()
        routes_page.wait_for_icecream_button()
        routes_page.click_in_icecream()
        is_icecream_selected = routes_page.icecream_is_selected()
        assert  is_icecream_selected == "True"



    # Prueba 8: Comprueba si aparece el modal para buscar un taxi.

    #Prueba 9 (opcional): Esperar a que aparezca la informacion del conductor en el modal.





    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
