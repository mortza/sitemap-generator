#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 05 13:21:59 2018
author  : Morteza Allahpour (mortezaallahpour@outlook.com)
link    : https://mortza.github.io
"""
from jinja2 import Environment, FileSystemLoader, select_autoescape


class SiteMapWriter():
    """docstring for SiteMapWriter"""

    def __init__(self, args):
        self.sitemap_file_name = args['sitemap_file_name']
        self.sitemap_file_path = args['sitemap_file_path']
        self.env = Environment(
            loader=FileSystemLoader('./templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def write(self, links):
        template = self.env.get_template('sitemap.xml.template')
        rendered = template.render(links=links)
        file_path = self.sitemap_file_path+self.sitemap_file_name
        file = open(file_path, mode='w', encoding="utf-8")
        file.write(rendered)
        file.close()
