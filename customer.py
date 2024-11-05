class Customer:
    """Represents a customer of the bookstore."""

    def __init__(self, name, contact_information, loyalty_member=False, membership_date=None):
        """
        Initializes a new Customer object.

        Parameters:
        - name (str): The customer's name.
        - contact_information (str): The customer's contact details.
        - loyalty_member (bool): Indicates if the customer is a loyalty member 
        - membership_date (date): The date the customer joined the loyalty program 
        """
        self.__name = name
        self.__contact_information = contact_information
        self.__loyalty_member = loyalty_member
        self.__membership_date = membership_date

    # Getters and Setters

    def getName(self):
        """Returns the name of the customer."""
        return self.__name

    def setName(self, name):
        """Sets a new name for the customer."""
        self.__name = name

    def getContactInformation(self):
        """Returns the contact information of the customer."""
        return self.__contact_information

    def setContactInformation(self, contact_information):
        """Sets new contact information for the customer."""
        self.__contact_information = contact_information

    def isLoyaltyMember(self):
        """Returns True if the customer is a loyalty member, otherwise False."""
        return self.__loyalty_member

    def setLoyaltyMember(self, loyalty_member):
        """Sets the customer's loyalty membership status."""
        self.__loyalty_member = loyalty_member

    def getMembershipDate(self):
        """Returns the date the customer joined the loyalty program."""
        return self.__membership_date

    def setMembershipDate(self, membership_date):
        """Sets a new membership date for the customer."""
        self.__membership_date = membership_date

    def __str__(self):
        """
        Returns a string representation of the customer.
        
        Shows the customer's name, loyalty membership status, 
        and the date they joined the loyalty program (if applicable).
        """
        return f"{self.__name} - Loyalty Member: {'Yes' if self.__loyalty_member else 'No'}, Joined: {self.__membership_date}"
