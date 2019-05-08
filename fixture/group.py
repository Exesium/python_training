# -*- coding: utf-8 -*-
from model.group import Group


class GroupHelper:

    group_cache = None

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
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.group_cache = None

    def select_1st_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_1st(self, group):
        self.edit_by_index(0, group)

    def edit_by_index(self, index, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_index(index)
        # edit-button clicking
        wd.find_element_by_name("edit").click()
        # editing forms
        self.change_group_forms("group_name", group.name)
        self.change_group_forms("group_header", group.header)
        self.change_group_forms("group_footer", group.footer)
        # submit changes
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.group_cache = None

    def edit_by_id(self, id, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_id(id)
        # edit-button clicking
        wd.find_element_by_name("edit").click()
        # editing forms
        self.change_group_forms("group_name", group.name)
        self.change_group_forms("group_header", group.header)
        self.change_group_forms("group_footer", group.footer)
        # submit changes
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.group_cache = None

    def del_1st_group(self):
        self.del_by_index(0)

    def del_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_index(index)
        # delete-button clicking
        wd.find_element_by_name("delete").click()
        self.app.open_home_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            # for element in wd.find_elements_by_css_selector("span.group"):
            for element in wd.find_elements_by_xpath("//input[@type='checkbox']"):
                text = element.text
                identity = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, identity=identity))
        return list(self.group_cache)

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='{}']".format(id)).click()

    def del_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_id(id)
        # delete-button clicking
        wd.find_element_by_name("delete").click()
        self.app.open_home_page()
        self.group_cache = None
