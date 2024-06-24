from selenium.webdriver.common.by import By
# Localizadores

from_field = (By.ID, "from")
to_field = (By.ID, "to")
taxi_button = (By.CLASS_NAME, "button.round")
comfort_button = (By.ID, "tariff-card-4")
phone_number_button = (By.CLASS_NAME, "np-button")
phone_number_field = (By.ID, "phone")
siguiente_button= (By.XPATH, '//button[text()="Siguiente"]')
code_field = (By.CSS_SELECTOR, '[name="phone"]')
confirmar_button = (By.CSS_SELECTOR, "Confirmar")
metodo_de_pago_button = (By.CLASS_NAME, "pp-text")
add_card_button = (By.CLASS_NAME, "pp-plus")
add_card_field = (By.ID, "number")
add_code_card_field = (By.CLASS_NAME, "card-code-input")
agregar_button = (By.XPATH, '//button[text()="Agregar"]')
any_other_element = (By.CLASS_NAME, "plc")
cerrar_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
message_for_driver = (By.CSS_SELECTOR, "Mensaje para el conductor")
requisitos_del_pedido_button = (By.CLASS_NAME, "reqs-head")
manta_y_panuelos_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
helado_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')


