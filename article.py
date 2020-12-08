import re


class Author:

    def __init__(self):
        self._aid = ''
        self._sequence = ''
        self._first_name = ''
        self._middle_name = ''
        self._last_name = ''
        self._email = ''
        self._affiliation = ''
        self._primary_contact = False

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
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @sequence.deleter
    def sequence(self):
        del self._sequence

    #########
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, fn):
        self._first_name = fn

    @first_name.deleter
    def first_name(self):
        del self._first_name

    #########
    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, mn):
        self._middle_name = mn

    @middle_name.deleter
    def middle_name(self):
        del self._middle_name

    #########
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, ln):
        self._last_name = ln

    @last_name.deleter
    def last_name(self):
        del self._last_name

    #########
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @email.deleter
    def email(self):
        del self._email

    #########
    @property
    def affiliation(self):
        return self._affiliation

    @affiliation.setter
    def affiliation(self, aff):
        self._affiliation = aff

    @affiliation.deleter
    def affiliation(self):
        del self._affiliation

    #########
    @property
    def primary_contact(self):
        return self._primary_contact

    @primary_contact.setter
    def primary_contact(self, value):
        if value == '1' or value == 1:
            value = True
        elif value == '0' or value == 0:
            value = False

        self._primary_contact = value

    @primary_contact.deleter
    def primary_contact(self):
        del self._primary_contact

    def get_full_name(self):

        is_chinese = re.compile(r'[\u4e00-\u9fff]+')

        if is_chinese.findall(self.first_name) \
                or is_chinese.findall(self.last_name):
            if self.middle_name:
                full_name = '{}•{}'.format(self.first_name,
                                           self.last_name)
            else:
                full_name = self.last_name + self.first_name
        else:
            if self.middle_name:
                full_name = '{} {} {}'.format(self.first_name,
                                              self.middle_name,
                                              self.last_name)
            else:
                full_name = '{} {}'.format(self.first_name,
                                           self.last_name)

        return full_name

    def __str__(self):
        return self.get_full_name()


class PDF:

    def __init__(self):
        self._link = ''
        self._pages = ''
        self._access_counter = 0

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value

    @link.deleter
    def link(self):
        del self._link

    #########
    @property
    def access_counter(self):
        return self._access_counter

    @access_counter.setter
    def access_counter(self, value):
        self._access_counter = int(value)

    @access_counter.deleter
    def access_counter(self):
        del self._access_counter

    #########
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value

    @pages.deleter
    def pages(self):
        del self._pages

    def __str__(self):
        return self._link


class Copyright:

    def __init__(self):
        self._holder = ''
        self._year = ''
        self._license_url = ''

    #########
    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, value):
        self._holder = value

    @holder.deleter
    def holder(self):
        del self._holder

    #########
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @year.deleter
    def year(self):
        del self._year

    #########
    @property
    def license_url(self):
        return self._license_url

    @license_url.setter
    def license_url(self, value):
        self._license_url = value

    @license_url.deleter
    def license_url(self):
        del self._license_url


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
        self._copyright = None
        self._journal = ''
        self._volume = ''
        self._issue = ''
        self._pdf = None

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
                author.primary_contact = value['primary_contact']
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

    def construct_author_str(self):
        author_list = []
        for author in self.authors:
            author_list.append(author.get_full_name())

        return ', '.join(author_list)

    #########
    @property
    def copyright(self):
        if not self._copyright.holder:
            self._copyright.holder = self.construct_author_str()

        return self._copyright

    @copyright.setter
    def copyright(self, value):
        cpr_obj = Copyright()
        cpr_obj.holder = self.construct_author_str()
        cpr_obj.year = value['year']
        cpr_obj.license_url = value['license_url']
        self._copyright = cpr_obj

    @copyright.deleter
    def copyright(self):
        del self._copyright

    #########
    @property
    def journal(self):
        return self._journal

    @journal.setter
    def journal(self, value):
        self._journal = value

    @journal.deleter
    def journal(self):
        del self._journal

    #########
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @volume.deleter
    def volume(self):
        del self._volume

    #########
    @property
    def issue(self):
        return self._issue

    @issue.setter
    def issue(self, value):
        self._issue = value

    @issue.deleter
    def issue(self):
        del self._issue

    #########
    @property
    def pdf(self):
        return self._pdf

    @pdf.setter
    def pdf(self, pdf_obj):
        self._pdf = pdf_obj

    @pdf.deleter
    def pdf(self):
        del self._pdf

    def __str__(self):
        return self._title


class Issue:

    def __init__(self):
        self._iid = ''
        self._journal = ''
        self._volume = ''
        self._number = ''
        self._year = ''
        self._cover = ''
        self._articles = []

    #########
    @property
    def iid(self):
        return self._iid

    @iid.setter
    def iid(self, value):
        self._iid = value

    @iid.deleter
    def iid(self):
        del self._iid

    #########
    @property
    def journal(self):
        return self._journal

    @journal.setter
    def journal(self, value):
        self._journal = value

    @journal.deleter
    def journal(self):
        del self._journal

    #########
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @volume.deleter
    def volume(self):
        del self._volume

    #########
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @number.deleter
    def number(self):
        del self._number

    #########
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @year.deleter
    def year(self):
        del self._year

    #########
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value

    @cover.deleter
    def cover(self):
        del self._cover

    #########
    @property
    def articles(self):
        return self._articles

    @articles.setter
    def articles(self, article_list):
        self._articles = article_list

    @articles.deleter
    def articles(self):
        del self._articles

    def __str__(self):
        return 'Vol. {}, No. {}, {}'.format(self._volume,
                                            self._number,
                                            self._year)
