[![Upload Python Package](https://github.com/joegasewicz/password-mixin/actions/workflows/python-publish.yml/badge.svg)](https://github.com/joegasewicz/password-mixin/actions/workflows/python-publish.yml)
[![Python package](https://github.com/joegasewicz/password-mixin/actions/workflows/python-package.yml/badge.svg)](https://github.com/joegasewicz/password-mixin/actions/workflows/python-package.yml)

# Password Mixin
Mixin that adds some useful methods to ORM objects

Compatible with Python `3.5 >= 3.9`

# Install
```bash
pip install password-mixin
```

## Setup
first create your objects (or ORM model) and add a `__hash_secret__` meta field.
Assign your application's secret value to `__hash_secret__`.

```python

from password_mixin import PasswordMixin
from sqlalchemy import Model # or Django , Flask-Sqlalchemy... etc.

class UserModel(OrmModel, PasswordMixin):
    
    password = Column(String()) # you must have a `password`.
    
    
    # Now create a meta field to define the secret used to create the salt, for example:
    __hash_secret__ = "your-app-secret"
        
```

## Usage
The password is saved as the following: `"<hash_name>:<hash>"`

### Password Hashing
```python
from password_mixin import PasswordAttributeError
try:
    user = UserModel()
    user.password = "wizard123"
    user.hash_password() # password is now `sha256:7ac5cf88e8c9d262b49af168d9c30e47f2945cc9c207f20af0a39f09aa04595e`
    # Now you can save your user to your db etc.
except PasswordAttributeError:
    # handle no password attribute
    

```

### Validating Passwords
```python
from password_mixin import PasswordMatchError

try:
    user.check_password("wizard111")
except PasswordMatchError:
     # handle passwords don't match
```

### Example with Flask & Flask-Sqlalchemy
```python
class UserModel(db.Model, PasswordMixin):

    __tablename__ = "users"
    __hash_secret__ = "wizard123"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def create_user(self):
        self.hash_password()
        db.session.add(self)
```
Now, with the above setup you can run the following

```python
u = UserModel(email="test1@test.com", password="wizard123")
u.create_user()
db.session.commit()
```