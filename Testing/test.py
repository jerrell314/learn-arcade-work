class Address:
    """ Hold all the fields for a mailing address. """
    def __init__(self):
        """ Set up the address fields. """
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""


def main():
    home_address = Address()
    home_address.name = "John Smith"


main()