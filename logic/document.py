from datetime import date


class Document(object):
    """
    Class used to represent a Document
    """

    def __init__(self, isbn: str = "Isbn", title: str = 'Title', author: str = "Author", type: str = "Type",
                 date_publication: date = 'yyyy-mm-dd', number: int = 0):
        """Document constructor using the Person

        :param isbn: id of document.
        :type isbn: str
        :param author: name of author the document.
        :type author: str
        :param type: type of document.
        :type type: str
        :param date_publication: date the publication of document
        :returns: document object
        param number: number of pages of document
        type: int
        returns: number of pages
        :rtype: object
        """
        self.number = number
        self.date_publication = date_publication
        self.type = type
        self.isbn = isbn
        self.title = title
        self.author = author

    @property
    def isbn(self) -> str:
        """ Returns id person of the person.
            :returns: id of person.
            :rtype: int
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn: str):
        """ the isbn of the document
          :param isbn: isbn of the document.
          :rtype: str
        """
        self._isbn = isbn

    @property
    def title(self) -> str:
        """ Returns the title of the document
            :returns: title of the person
            :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """ The title of the document
         :param title: title of document
         :type: str
        """
        self._title = title

    @property
    def author(self) -> str:
        """Returns the author of the document.
         :return: author of document.
         :rtype: str.
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """ The author of the document
         :param author: author of document
         :rtype: str
        """
        self._author = author

    @property
    def type(self) -> str:
        """ Return type of document
         :return: type of document
         :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """ The type of the document
         :param type: type of document
         :rtype: str
        """
        self._type = type

    @property
    def date_publication(self) -> date:
        """Return date publication of the document
        : return: date publication of document
        : rtype: str
        """
        return self._date_publication

    @date_publication.setter
    def date_publication(self, date_publication: date):
        """ The date publication of the document
        :param date_publication: data publication of document
        :rtype: date
        """
        self._date_publication = date_publication

    @property
    def number(self) -> int:
        """Return number of pages of the document
        : return: number of pages of document
        : rtype: int
        """
        return self._number

    @number.setter
    def number(self, number: int):
        """ The number of pages of the document
        :param number: data publication of document
        :rtype: date
        """
        self._number = number

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self.isbn, self.title, self.author, self.type,
                                                       self.date_publication, self.number)


if __name__ == '__main__':

    edwin = Document(isbn='IL2', title='Mundi', author="Esneider", type='Libero',
                     date_publication=date.today(), number=12)
    print(edwin)
