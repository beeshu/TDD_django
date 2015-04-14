#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xzw on 2015/4/10

__author__ = 'xzw'


from .base import FunctinalTest


class ItemValidationTest(FunctinalTest):
        
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item!")
                
        # She tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Buy Milk\n')
        self.check_for_row_in_list_table('1: Buy Milk')
        
        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys('\n')
        
        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy Milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item!")
        
        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make Tea\n')
        self.check_for_row_in_list_table('1: Buy Milk')
        self.check_for_row_in_list_table('2: Make Tea')
        
        