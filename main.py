import os
import CSSReplacer
import HTMLReplacer

__author__ = 'Tong'

html_base_url = "www\html"
css_base_url = "www\css"

# replace css
for parent, dirnames, filenames in os.walk(css_base_url):
    for inner_filename in filenames:
        CSSReplacer.replace(os.path.join(parent, inner_filename),
                            inner_filename[:inner_filename.find('.css')])

# replace html
for parent, dirnames, filenames in os.walk(html_base_url):
    for dirname in dirnames:
        inner_url = os.path.join(parent, dirname)
        for inner_parent, inner_dirnames, inner_filenames in os.walk(inner_url):
            for inner_filename in inner_filenames:
                HTMLReplacer.replace(os.path.join(inner_url, inner_filename), dirname)