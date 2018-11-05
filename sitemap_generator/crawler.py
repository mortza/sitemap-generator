#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 05 10:18:45 2018
author  : Morteza Allahpour (mortezaallahpour@outlook.com)
link    : https://mortza.github.io
"""
import bs4
from requests import get as page_loader
import urllib3
import logging


logger = logging.getLogger(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class PageLoader():
    def __init__(self):
        pass

    def load(self, url):
        logger.debug('Loading URL: {}'.format(url))
        page = page_loader(url, verify=False)
        logger.debug('{} status code: {}'.format(url, page.status_code))
        return page.content


class LinkExtractor():
    def __init__(self, start_with=None):
        self.start_with = start_with

    def extract(self, page):
        soup = bs4.BeautifulSoup(page, 'html.parser')
        page_links = soup.find_all('a')
        links = []
        for a_tag in page_links:
            href = self._get_href(a_tag)
            if self._is_valid_link(href):
                links.append(href)

        logger.debug("Total links found: {}".format(len(links)))
        return links

    def _is_valid_link(self, href):
        return href.startswith(self.start_with)

    def _get_href(self, link):
        href = link.get('href')
        return href


class Crawler():
    def __init__(self, base_url):
        self.base_url = base_url

    def run(self):
        links = [self.base_url]
        laoder = PageLoader()
        linke_extractor = LinkExtractor(self.base_url)
        visited_links = list()
        while len(links) > 0:
            link = links.pop(0)  # take head item
            page = laoder.load(link)
            page_links = linke_extractor.extract(page)
            for p_link in page_links:
                if p_link not in visited_links:
                    visited_links.append(p_link)
                    links.append(p_link)

        logger.debug('Total links grabbed from {}: {}'.format(
            self.base_url, len(visited_links)))
        return visited_links
