from selenium.webdriver.common.by import By
# Localizadores

from_field = (By.ID, "from")
to_field = (By.ID, "to")
taxi_button = (By.CLASS_NAME, "button.round")
comfort_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
phone_number_button = (By.CLASS_NAME, "np-button")
phone_number_field = (By.ID, "phone")
siguiente_button= (By.XPATH, '//button[text()="Siguiente"]')
code_field = (By.XPATH, '//form/div/div/input[@id="code"]')
confirmar_button = (By.XPATH, '//button[text()="Confirmar"]')
metodo_de_pago_button = (By.CLASS_NAME, "pp-text")
add_card_button = (By.CLASS_NAME, "pp-plus")
add_card_field = (By.ID, "number")
add_code_card_field = (By.XPATH, '//input[@placeholder="12"]')
agregar_button = (By.XPATH, '//button[text()="Agregar"]')
any_other_element = (By.CLASS_NAME, "plc")
cerrar_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
message_for_driver = (By.ID, "comment")
requisitos_del_pedido = (By.CLASS_NAME, "reqs-arrow.open")
manta_y_panuelos = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
helado_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
recorrido_button = (By.CLASS_NAME, "smart-button-main")
modal_de_busqueda = (By.CLASS_NAME, "order-header-title")


