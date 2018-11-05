#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 05 10:09:48 2018
@author  : Morteza Allahpour (mortezaallahpour@outlook.com)
link    : https://mortza.github.io
"""
import sys
import logging
from sitemap_generator.crawler import Crawler
from sitemap_generator.xmlwriter import SiteMapWriter
from yaml import load as yaml_loader
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


logging.basicConfig(
    filename='log.log',
    format='%(asctime)s %(levelname)s %(filename)s ,'
           '@%(funcName)s:%(lineno)d, %(message)s',
    filemode='w+',
    level=logging.DEBUG)


def parse_config(config_path):
    stream = ''.join(open(config_path, mode='r', encoding='utf-8').readlines())
    return yaml_loader(stream, Loader=Loader)


def main():
    config_file_path = sys.argv[1] if len(
        sys.argv) > 2 else 'default_config.yml'
    logging.info("Reading config from: {}".format(config_file_path))
    config = parse_config(config_file_path)
    logging.info("Base address: {}"
                 .format(config['base_url']))
    logging.info("Sitemap file name: {}"
                 .format(config['sitemap_file_name']))
    logging.info("Sitemap file save path: {}"
                 .format(config['sitemap_file_path']))
    crawler = Crawler(config['base_url'])
    links = crawler.run()

    writer = SiteMapWriter(config)
    writer.write(links)


if __name__ == "__main__":
    main()
