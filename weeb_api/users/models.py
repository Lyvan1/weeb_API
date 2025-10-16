from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class User(models.Model):
    """_User Entity_

    Args:
        first_name (str): user's firstname
        last_name (str): user's lastname
        email (str): user's email --> unique
        password (str)
    """
    
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 128) #128 --> because of password hash
    
    def __str__(self):
        return self.email
    
    def set_password(self, raw_password):
        """
        Hash password and save it to the object.

        Args:
            raw_password (str): password not hashed.
        """
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """
        check if the given apssword is the same as the hashed password.

        Args:
            raw_password (str): password not hashed to check.

        Returns:
            bool: True if password corred, else False.
        """
        return check_password(raw_password, self.password)