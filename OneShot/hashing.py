from passlib.context import CryptContext


class Hash():
    def pasword_hashing(password: str):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(password)
