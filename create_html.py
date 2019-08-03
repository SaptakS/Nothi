import json
import os
from distutils.dir_util import copy_tree

class HTMLCreator():
    def load_data(self):
        # load the json data for all logs
        log_data_file = open("data.json")
        self.log_data = json.load(log_data_file)

    def load_templates(self):
        # load all the html template files
        self.tag_html_template = open("src/includes/_tag.html", "r").read()
        self.item_html_template = open("src/includes/_item.html", "r").read()
        self.main_html_template = open("src/template.html", "r").read()

    def get_tags_html(self, tags):
        # loop through all the tags supplied
        # append each tag html to get the full list
        tags_html = ""
        for tag in tags:
            tags_html += self.tag_html_template.format(item_tag=tag) + "\n"
        return tags_html

    def get_items_html(self):
        # loop over all the log data in json.
        # using string formatting in the templates, add the necessary data
        # first in the tag template, then the tag and all other data in item
        # and then all item html in the main template
        items_html = ""
        for item in self.log_data:
            tags_html = self.get_tags_html(item["tags"])
            items_html += self.item_html_template.format(
                item_link=item["link"],
                item_title=item["title"],
                item_date=item["date"],
                item_tags=tags_html
            ) + "\n"
        
        return items_html

            
    def get_final_html(self):
        # get the list of items html and append it in the correct place in the
        # main template and return
        items_html = self.get_items_html()
        final_html = self.main_html_template.format(items=items_html)
        return final_html

    def write_final_html(self):
        # write the final html in index.html
        final_html = self.get_final_html()

        if not os.path.exists("dist"):
            os.mkdir("dist")
        index_html = open("dist/index.html", "w")
        index_html.write(final_html)
        index_html.close()

        # copy the css and js files
        copy_tree("src/css", "dist/css")
        copy_tree("src/js", "dist/js")

    def create(self):
        self.load_data()
        self.load_templates()
        self.write_final_html()


html_creator = HTMLCreator()
html_creator.create()