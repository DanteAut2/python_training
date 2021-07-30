from model.contact import Contact
from model.group import Group
from selenium.webdriver.support.ui import Select
import re
import time
import random


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
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("home", contact.homephone)
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
        self.open_main_page()
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
                lastname = element.find_elements_by_tag_name("td")[1].text
                firstname = element.find_elements_by_tag_name("td")[2].text
                all_phones = element.find_elements_by_tag_name("td")[5].text
                all_emails = element.find_elements_by_tag_name("td")[4].text
                address = element.find_elements_by_tag_name("td")[3].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)


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


    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        id = int(id)
        self.open_main_page()
        self.select_edit_contact_by_id(id)
        time.sleep(2)
        self.fill_contact_form(new_contact_data)
        time.sleep(2)
        wd.find_element_by_name("update").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_main_page()
        self.contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_main_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones, address=address))
        return list(self.contact_cache)


    def select_edit_contact_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_main_page()
        self.contact_cache = None


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.update_random_contact(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, fax=fax,
                       email=email, email2=email2, email3=email3, address=address)


    def add_contact_to_group_by_id(self, contact_id, random_group_number):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_id("%s" % contact_id).click()
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[4]/select/option[%s]" % random_group_number).click()
        wd.find_element_by_name("add").click()
        try:
            wd.find_element_by_xpath("//*[text() = 'Users added']")
        except Exception:
            time.sleep(0.1)

    def delete_contact_from_group_by_id(self, group_id, orm):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()
        if not wd.find_element_by_xpath("//div[@id='content']/label/strong/span[@id='search_count']").text == 0:
            contacts = orm.get_contacts_in_group(Group(id='%s' % group_id))
            random_contact_number = random.randint(0, len(contacts)-1)
            contact_id = contacts[random_contact_number].id
            wd.find_element_by_id("%s" % contact_id).click()
            wd.find_element_by_name("remove").click()
            try:
                 wd.find_element_by_xpath("//*[text() = 'Users removed.']")
            except Exception:
                 time.sleep(0.1)


    def add_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_list_not_in_group()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % group_id).click()
        wd.find_element_by_name("add").click()
        self.contact_cache = None


    def open_contact_list_not_in_group(self):
        wd = self.app.wd
        self.open_main_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text("[none]")



    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_list_in_group_by_id(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()



    def open_contact_list_in_group_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        Select(wd.find_element_by_xpath('//*[@id="right"]/select')).select_by_value(id)