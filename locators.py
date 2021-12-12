from selenium.webdriver.common.by import By

locator = {
    "contact_us_button": (By.ID, "contact-link"),
    "selector_dropdown": (By.ID, "id_contact"),
    "email_field": (By.ID, "email"),
    "order_field": (By.ID, "id_order"),
    "message_field": (By.ID, "message"),
    "send_button": (By.ID, "submitMessage"),
    "success_message": (By.CSS_SELECTOR, "#center_column > p")

    }
# center_column > p
# #center_column > ul