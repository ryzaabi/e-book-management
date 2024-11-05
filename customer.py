class Customer:
    """Represents a customer of the bookstore."""

    def __init__(self, name, contact_information, loyalty_member=False, membership_date=None):
        self.__name = name
        self.__contact_information = contact_information
        self.__loyalty_member = loyalty_member
        self.__membership_date = membership_date

    # Getters and Setters
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getContactInformation(self):
        return self.__contact_information

    def setContactInformation(self, contact_information):
        self.__contact_information = contact_information

    def isLoyaltyMember(self):
        return self.__loyalty_member

    def setLoyaltyMember(self, loyalty_member):
        self.__loyalty_member = loyalty_member

    def getMembershipDate(self):
        return self.__membership_date

    def setMembershipDate(self, membership_date):
        self.__membership_date = membership_date

    def __str__(self):
        return f"{self.__name} - Loyalty Member: {'Yes' if self.__loyalty_member else 'No'}, Joined: {self.__membership_date}"
