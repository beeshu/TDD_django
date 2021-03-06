#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xzw on 2015/4/24

__author__ = 'xzw'

from .base import FunctinalTest
from selenium.webdriver.support.ui import WebDriverWait
import time


class LoginTest(FunctinalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to.window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def wait_for_element_with_id(self, id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda x: x.find_element_by_id(id)
        )

    def test_login_with_persona(self):
        # Edith goes to the awesome superlists site
        # and notices a "Sign in" link for the first time.
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        # A persona login box appears
        self.switch_to_new_window('Mozilla Persona')

        # Edith logs in with her email address
        ## Use mockmyid.com for test email
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys('beeshu@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        # The Persona window closes
        self.switch_to_new_window('To-Do')

        # She can see that she is logged in
        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('beeshu@mockmyid.com', navbar.text)

