import os
import json
import re

class Searcher:

    def __init__(self, content_to_search, target_dir):
        self.content_to_search = content_to_search
        self.target_dir = target_dir
        self.list_of_results = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        pass

    def search_in_txt(self):
        for file in os.listdir(self.target_dir):
            path = rf"{self.target_dir}/{file}"
            if os.path.isfile(path) and os.path.splitext(path)[1] in [".txt"]:
                with open(path) as in_file:
                    lines = in_file.readlines()
                    results = lines[0].split("link:")[1] if lines[0].startswith("link:") else None
                    for line in lines:
                        if self.content_to_search in line:
                            self.list_of_results.append(results.replace('\n', '').lstrip())
        if  self.list_of_results:
            return self.list_of_results
        else:
            return [f"The content: \"{self.content_to_search}\" not found in all .txt files in this directory"]

    def search_in_json(self):
        for file in os.listdir(self.target_dir):
            path = rf"{self.target_dir}/{file}"
            if os.path.isfile(path):
                with open(path) as in_file:
                    json_data = json.load(in_file)
                    if isinstance(json_data, list):
                        for obj in json_data:
                            for key, val in obj.items():
                                if self.content_to_search in val:
                                    self.list_of_results.append(obj)
        if self.list_of_results:
            return self.list_of_results
        else:
            return[f"The content: \"{self.content_to_search}\" not found in all .json files in this directory"]


