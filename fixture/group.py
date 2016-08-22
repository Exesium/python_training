# -*- coding: utf-8 -*-


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def change_group_forms(self, form_name, form_value):
        wd = self.app.wd
        if form_value is not None:
            wd.find_element_by_name(form_name).click()
            wd.find_element_by_name(form_name).clear()
            wd.find_element_by_name(form_name).send_keys(form_value)

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill forms
        self.change_group_forms("group_name", group.name)
        self.change_group_forms("group_header", group.header)
        self.change_group_forms("group_footer", group.footer)
        # submit new group
        wd.find_element_by_name("submit").click()
        self.app.open_home_page()

    def select_1st_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_1st(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_1st_group()
        # edit-button clicking
        wd.find_element_by_name("edit").click()
        # editing forms
        self.change_group_forms("group_name", group.name)
        self.change_group_forms("group_header", group.header)
        self.change_group_forms("group_footer", group.footer)
        # submit changes
        wd.find_element_by_name("update").click()
        self.app.open_home_page()

    def del_1st(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_1st_group()
        # delete-button clicking
        wd.find_element_by_name("delete").click()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))
