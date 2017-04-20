"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""
    def __init__(self,
                firstname,
                lastname,
                email,
                password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        # TODO: need to implement this

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: %s %s, %s>" % (
            self.firstname, self.lastname, self.email)


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {id: Customer object}
    """

    customers = {}

    for line in open(filepath):
        (firstname,
         lastname,
         email,
         password) = line.strip().split("|")

        customers[email] = Customer(firstname, lastname, email, password)

    return customers


def get_by_email(email):
    """Return a customer, given its email."""

    # This relies on access to the global dictionary `customers`

    return customers[email]


customers = read_customers_from_file("customers.txt")
