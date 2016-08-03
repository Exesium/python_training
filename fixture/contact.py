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
        self.change_contact_forms(self, "firstname", con.firstname)
        self.change_contact_forms(self, "middlename", con.middlename)
        self.change_contact_forms(self, "lastname", con.lastname)
        self.change_contact_forms(self, "nickname", con.nickname)
        self.change_contact_forms(self, "title", con.title)
        self.change_contact_forms(self, "company", con.company)
        self.change_contact_forms(self, "address", con.address)
        self.change_contact_forms(self, "mobile", con.mobile)
        self.change_contact_forms(self, "work", con.work)
        self.change_contact_forms(self, "email", con.email)
        self.change_contact_forms(self, "byear", con.b_year)
        # submit adding
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_1st(self, con):
        wd = self.app.wd
        # click edit button
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # editing forms
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(con.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(con.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(con.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(con.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(con.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(con.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(con.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(con.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(con.work)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(con.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[{0}]".format(con.b_day)).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[{0}]".format(con.b_month)).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(con.b_year)
        # submit changes
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def del_1st(self):
        wd = self.app.wd
        # checking 1st element
        wd.find_element_by_name("selected[]").click()
        # delete-button clicking
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
