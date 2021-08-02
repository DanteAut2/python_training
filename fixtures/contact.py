from model.contact import Contact
import re
import time

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def open_add_contact_screen(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def add_new_contact(self, contact):
        wd = self.app.wd
        self.open_add_contact_screen()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.street)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='" + contact.birthday_day + "']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='" + contact.birthday_month + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath("(//option[@value='" + contact.anniversary_day + "'])[2]").click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath("(//option[@value='" + contact.anniversary_month + "'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.note)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_contact_page()
        self.contacts_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        #wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.open_contact_to_edit_by_index(index)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.street)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='" + contact.birthday_day + "']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='" + contact.birthday_month + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath("(//option[@value='" + contact.anniversary_day + "'])[2]").click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath("//option[@value='" + contact.anniversary_month.lower() + "']").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.note)
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.open_contact_page()
        self.contacts_cache = None

    def edit_contact_by_id(self, id, contact_to_edit):
        wd = self.app.wd
        self.open_contact_page()
        #wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.open_contact_to_edit_by_id(int(id))
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_to_edit.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact_to_edit.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_to_edit.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact_to_edit.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact_to_edit.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_to_edit.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_to_edit.street)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_to_edit.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_to_edit.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact_to_edit.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact_to_edit.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_to_edit.email)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='" + contact_to_edit.birthday_day + "']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='" + contact_to_edit.birthday_month + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact_to_edit.birthday_year)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath("(//option[@value='" + contact_to_edit.anniversary_day + "'])[2]").click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath("//option[@value='" + contact_to_edit.anniversary_month.lower() + "']").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact_to_edit.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact_to_edit.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact_to_edit.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact_to_edit.note)
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.open_contact_page()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_contact_page()
        self.contacts_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_contact_page()
        self.contacts_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                fname = element.find_element_by_xpath("td[3]").text
                lname = element.find_element_by_xpath("td[2]").text
                street = element.find_element_by_xpath("td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contacts_cache.append(Contact(firstname=fname, lastname=lname, id=id, street=street,
                                                   all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contacts_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        street =  wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, street=street, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2)

    def add_contact_to_group(self, id, group):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_css_selector("select[name = 'to_group'] > option[value = '%s']" % group.id).click()
        wd.find_element_by_xpath("(//input[@value='Add to'])").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_contact_page()
        self.contacts_cache = None

    def delete_contact_from_group(self, id, group):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("select[name = 'group'] > option[value = '%s']" % group.id).click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("remove")
        wd.find_element_by_name("remove").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_contact_page()
        self.contacts_cache = None