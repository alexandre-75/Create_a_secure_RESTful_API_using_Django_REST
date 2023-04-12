from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    """
     A class representing a user in the system.

     This class inherits from Django's AbstractUser class, which provides functionality for
     user management.

     Attributes:
         username (str): The username of the user, (other attributes inherited from the AbstractUser class).

     Methods:
         __str__: Returns a string representation of the User object,
                   which is simply the username.

     """

    def __str__(self):
        return self.username

    pass
