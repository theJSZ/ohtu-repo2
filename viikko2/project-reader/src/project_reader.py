from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        dict1 = tomli.loads(content)
        dict2 = dict1["tool"]["poetry"]

        name = dict2["name"]
        description = dict2["description"]
        dependencies = []
        dev_dependencies = []

        for x in dict2["dependencies"]:
            dependencies.append(f'{x}')

        for x in dict2["dev-dependencies"]:
            dev_dependencies.append(f'{x}')

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
