class Customer:
    def __init__(self, name, contact_information, loyalty_member=False):
        self.__name = name
        self.__contact_information = contact_information
        self.__loyalty_member = loyalty_member

    def getName(self):
        return self.__name

    def isLoyaltyMember(self):
        return self.__loyalty_member

    def __str__(self):
        return f"{self.__name} - Loyalty Member: {'Yes' if self.__loyalty_member else 'No'}"
