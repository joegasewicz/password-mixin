import pytest
from password_mixin import PasswordMixin, PasswordMatchError, PasswordAttributeError


class MockOrmModel:
    __tablename__ = "users"


class TestModel(MockOrmModel, PasswordMixin):
    pass


class TestPasswordMixin:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @pytest.mark.parametrize(
        "password1,secret1,password2,secret2,should_pass",
        [
            ("wizard123", "abc123", "wizard123", "abc123", True),  # passwords match
            ("wizard123", "abc123", "wizard223", "abc123", False),  # secrets dont match
            ("wizard123", "abc123", "wizard1234", "abc123", False),  # passwords dont match
        ]
    )
    def test_hash_password(self, password1, secret1, password2, secret2, should_pass):
        test_password = TestModel()
        test_password.password = password1
        test_password.__hash_secret__ = secret1
        test_password_two = TestModel()
        test_password_two.password = password2
        test_password_two.__hash_secret__ = secret2
        test_password.hash_password()
        test_password_two.hash_password()
        if should_pass:
            assert test_password.password_hash == test_password_two.password_hash
        else:
            assert test_password.password_hash != test_password_two.password_hash

    def test_check_password(self):
        test_password = TestModel()
        test_password.password = "wizard123"
        test_password.__hash_secret__ = "secret"
        test_password.hash_password()
        test_password.password = test_password.password_hash
        assert test_password.check_password("wizard123") is True
