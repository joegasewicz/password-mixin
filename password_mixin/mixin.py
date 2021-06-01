"""
PasswordMixin class
"""
from hashlib import pbkdf2_hmac

from password_mixin.errors import PasswordMatchError, PasswordAttributeError


SHA_256 = "sha256"


class PasswordMixin:

    _salt: bytes

    password_hash: str

    def _get_password(self):
        password = getattr(self, "password", None)
        if not password:
            raise PasswordAttributeError(
                "password-mixin error: Your object must contain a valid password attribute",
            )
        else:
            return password

    def _gen_salt(self) -> bytes:
        return self.__hash_secret__.encode("utf-8")

    def _gen_hash(self, password: bytes) -> str:
        self._hash = pbkdf2_hmac(
            SHA_256,
            password,
            self._gen_salt(),
            100_000,
        )
        return self._hash.hex()

    def hash_password(self) -> None:
        password = self._get_password().encode("utf-8")
        hashed = self._gen_hash(password)
        self.password_hash = f"{SHA_256}:{hashed}"

    def check_password(self, password: str) -> bool:
        _, prev_hash = self.password.split(":")
        salt = self._gen_salt()
        curr_hash = pbkdf2_hmac(
            SHA_256,
            password.encode("utf-8"),
            salt,
            100_000,
        ).hex()
        if prev_hash != curr_hash:
            raise PasswordMatchError("password-mixin error: Passwords do not match")
        else:
            return True
