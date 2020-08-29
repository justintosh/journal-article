from .db_class import DBClass, SettingHandler, SettingType
import re

class Article:

    def __init__(self):

        self._aid = ''
        self._title = ''
        self._abstract = ''
        self._subject = ''
        self._doi = ''
        self._authors = []
        self._citations = ''
        self._sponsor = ''
        self._copyright_holder = ''

    #########
    @property
    def aid(self):
        return self._aid

    @aid.setter
    def aid(self, value):
        self._aid = value

    @aid.deleter
    def aid(self):
        del self._aid

    #########
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @title.deleter
    def title(self):
        del self._title

    #########
    @property
    def abstract(self):
        return self._abstract

    @abstract.setter
    def abstract(self, value):
        self._abstract = value

    @abstract.deleter
    def abstract(self):
        del self._abstract

    #########
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @subject.deleter
    def subject(self):
        del self._subject

    #########
    @property
    def doi(self):
        return self._doi

    @doi.setter
    def doi(self, value):
        self._doi = value

    @doi.deleter
    def doi(self):
        del self._doi

    #########
    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, author_ld):
        if type(author_ld) is dict:
            for key, value in author_ld.items():
                author = Author()
                author.sequence = key
                author.aid = value['id']
                author.first_name = value['first_name']
                author.middle_name = value['middle_name']
                author.last_name = value['last_name']
                author.affiliation = value['affiliation']
                self._authors.append(author)
                del author
        elif type(author_ld) is list:
            self._authors = author_ld

    @authors.deleter
    def authors(self):
        del self._authors

    #########
    @property
    def sponsor(self):
        return self._sponsor

    @sponsor.setter
    def sponsor(self, value):
        self._sponsor = value

    @sponsor.deleter
    def sponsor(self):
        del self._sponsor

    #########
    @property
    def citations(self):
        return self._citations

    @citations.setter
    def citations(self, value):
        self._citations = value

    @citations.deleter
    def citations(self):
        del self._citations

    #########
    @property
    def copyright_holder(self):
        return self._copyright_holder

    @copyright_holder.setter
    def copyright_holder(self, authors):
        author_list = []
        for author in authors:
            author_list.append(author.get_full_name())

        self._copyright_holder = ', '.join(author_list)

    @copyright_holder.deleter
    def copyright_holder(self):
        del self._copyright_holder
        
