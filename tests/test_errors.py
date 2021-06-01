import pytest
from password_mixin import PasswordMixin, PasswordMatchError, PasswordAttributeError


class TestModel(PasswordMixin):
    pass


class TestPasswordMatchError:

    def test_raises(self):
        test_password = TestModel()
        test_password.password = "wizard123"
        test_password.__hash_secret__ = "secret"
        test_password.hash_password()
        test_password.password = test_password.password
        with pytest.raises(PasswordMatchError):
            test_password.check_password("wizard111")


class TestPasswordAttributeError:

    def test_raises(self):
        test_password = TestModel()

        # None
        test_password.password = None
        test_password.__hash_secret__ = "secret"
        with pytest.raises(PasswordAttributeError):
            test_password.hash_password()

        # Empty string
        test_password.password = ""
        test_password.__hash_secret__ = "secret"
        with pytest.raises(PasswordAttributeError):
            test_password.hash_password()
