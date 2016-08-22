# -*- coding: utf-8 -*-


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

    def edit_1st(self, con):
        wd = self.app.wd
        # click edit button
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
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

    def del_1st(self):
        wd = self.app.wd
        # checking 1st element
        wd.find_element_by_name("selected[]").click()
        # delete-button clicking
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
