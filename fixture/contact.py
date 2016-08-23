# -*- coding: utf-8 -*-
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_contact_forms(self, form_name, form_value):
        wd = self.app.wd
        if form_value is not None:
            wd.find_element_by_name(form_name).click()
            wd.find_element_by_name(form_name).clear()
            wd.find_element_by_name(form_name).send_keys(form_value)

    def add_new(self, con):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # change_forms
        self.change_contact_forms("firstname", con.firstname)
        self.change_contact_forms("middlename", con.middlename)
        self.change_contact_forms("lastname", con.lastname)
        self.change_contact_forms("nickname", con.nickname)
        self.change_contact_forms("title", con.title)
        self.change_contact_forms("company", con.company)
        self.change_contact_forms("address", con.address)
        self.change_contact_forms("mobile", con.mobile)
        self.change_contact_forms("work", con.work)
        self.change_contact_forms("email", con.email)
        self.change_contact_forms("byear", con.b_year)
        # submit adding
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def first_contact_edit_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def edit_1st(self, con):
        self.edit_by_index(0, con)

    def edit_by_index(self, index, con):
        wd = self.app.wd
        # click edit button
        self.edit_contact_page_by_index(index)
        # editing forms
        self.change_contact_forms('firstname', con.firstname)
        self.change_contact_forms('middlename', con.middlename)
        self.change_contact_forms('lastname', con.lastname)
        self.change_contact_forms('nickname', con.nickname)
        self.change_contact_forms('title', con.title)
        self.change_contact_forms('company', con.company)
        self.change_contact_forms('address', con.address)
        self.change_contact_forms('mobile', con.mobile)
        self.change_contact_forms('work', con.work)
        self.change_contact_forms('email', con.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[{0}]".format(con.b_day)).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[{0}]".format(con.b_month)).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(con.b_year)
        # submit changes
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_page_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[{}]/td[8]/a/img".format(index+2)).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def del_by_index(self, index):
        wd = self.app.wd
        # checking 1st element
        self.select_by_index(index)
        # delete-button clicking
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                name = element.find_element_by_name("selected[]").get_attribute("title")[8:-1]
                first_name = name.split(" ")[0]
                last_name = name.split(" ")[1]
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id))
        return self.contact_cache
