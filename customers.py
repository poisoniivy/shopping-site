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
        # self.password = password
        self.hashed_password = hash(password)

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: %s %s, %s>" % (
            self.firstname, self.lastname, self.email)

    def is_correct_password(self, password):
        """Check if `password` is correct password for this customer.

        Compares the hash of `password` to the stored hash of the
        original password.
        """

        return hash(password) == self.hashed_password

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
