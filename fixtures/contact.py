from model.contact import Contact


class ContactHelper:


    def __init__(self, app):
        self.app = app


    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def open_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()


    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_main_page()
        self.contact_cache = None


    def fill_contact_form(self, contact):
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("home", contact.home_number)
        self.change_field_value("email", contact.first_mail)
        self.change_field_value("address2", contact.second_address)


    def modify_first_contact(self):
        self.modify_contact_by_index(0)


    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.update_random_contact(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_to_main_page()
        self.contact_cache = None


    def update_random_contact(self, index):
        wd = self.app.wd
        update = wd.find_elements_by_xpath("//img[@alt='Edit']")
        update[index].click()


    contact_cache = None


    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_main_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastName = element.find_elements_by_tag_name("td")[1].text
                firstName = element.find_elements_by_tag_name("td")[2].text
                self.contact_cache.append(Contact(id=id, last_name=lastName, first_name=firstName))
        return list(self.contact_cache)


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


    def chose_random_checkbox(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.chose_random_checkbox(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_main_page()
        self.contact_cache = None


    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def count(self):
        wd = self.app.wd
        self.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))
