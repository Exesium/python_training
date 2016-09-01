# -*- coding: utf-8 -*-
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

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
        self.change_contact_forms('home', con.home)
        self.change_contact_forms('mobile', con.mobile)
        self.change_contact_forms('work', con.work)
        self.change_contact_forms('fax', con.fax)
        self.change_contact_forms("email", con.email)
        self.change_contact_forms('email2', con.email2)
        self.change_contact_forms('email3', con.email3)
        self.change_contact_forms("byear", con.b_year)
        self.change_contact_forms("phone2", con.phone2)
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
        self.open_for_edit_contact_page_by_index(index)
        # editing forms
        self.change_contact_forms('firstname', con.firstname)
        self.change_contact_forms('middlename', con.middlename)
        self.change_contact_forms('lastname', con.lastname)
        self.change_contact_forms('nickname', con.nickname)
        self.change_contact_forms('title', con.title)
        self.change_contact_forms('company', con.company)
        self.change_contact_forms('address', con.address)
        self.change_contact_forms('home', con.home)
        self.change_contact_forms('mobile', con.mobile)
        self.change_contact_forms('work', con.work)
        self.change_contact_forms('fax', con.fax)
        self.change_contact_forms('email', con.email)
        self.change_contact_forms('email2', con.email2)
        self.change_contact_forms('email3', con.email3)
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[{0}]".format(con.b_day)).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[{0}]".format(con.b_month)).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(con.b_year)
        self.change_contact_forms("phone2", con.phone2)
        # submit changes
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_for_edit_contact_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
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

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                name = element.find_element_by_name("selected[]").get_attribute("title")[8:-1]
                first_name = name.split(" ")[0]
                last_name = name.split(" ")[1]
                identity = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, identity=identity))
        return self.contact_cache

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_for_edit_contact_page_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        identity = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, identity=identity, address=address,
                       email=email, email2=email2, email3=email3,
                       home=home, work=work, mobile=mobile, phone2=phone2)

    def get_contact_list_new(self):
        # if self.contact_cache is None:
        wd = self.app.wd
        self.app.open_home_page()
        self.contact_cache = []
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            identity = cells[0].find_element_by_tag_name("input").get_attribute("value")
            lastname = cells[1].text
            firstname = cells[2].text
            address = cells[3].text
            all_emails = cells[4].text
            all_phones = cells[5].text
            self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,
                                              identity=identity, address=address,
                                              all_emails=all_emails, all_phones_from_homepage=all_phones))
        return list(self.contact_cache)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)
