class ContactHelper:

    def __init__(self, app):
        self.app = app


    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def open_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()


    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_main_page()


    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("home", contact.home_number)
        self.change_field_value("email", contact.first_mail)
        self.change_field_value("address2", contact.second_address)


    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_to_main_page()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def chose_first_contact(self):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_main_page()


    def count(self):
        wd = self.app.wd
        self.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))
