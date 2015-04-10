#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xzw on 2015/4/10

__author__ = 'xzw'


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title