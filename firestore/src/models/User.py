import logging

from src import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User:
    def __init__(self, user_id, first_name, last_name, date_of_birth, place_of_birth, citizenship):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.citizenship = citizenship

    def save(self):
        """Saves the user instance to Firestore."""
        user_ref = db.collection("users").document(self.user_id)
        user_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "place_of_birth": self.place_of_birth,
            "citizenship": self.citizenship,
        }
        user_ref.set(user_data)
        logger.info(f"User {self.first_name} {self.last_name} added to Firestore.")

    @classmethod
    def get(cls, user_id):
        """Retrieves a user from Firestore by user_id."""
        user_ref = db.collection("users").document(user_id)
        doc = user_ref.get()

        if doc.exists:
            data = doc.to_dict()
            logger.info(f"User data retrieved: {data}")
            return cls(
                user_id=user_id,
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                date_of_birth=data.get("date_of_birth"),
                place_of_birth=data.get("place_of_birth"),
                citizenship=data.get("citizenship"),
            )
        else:
            logger.info("No such document!")
            return None

    @classmethod
    def list_all(cls):
        """Retrieves all users from Firestore."""
        users_ref = db.collection("users")
        docs = users_ref.stream()
        users = []
        for doc in docs:
            data = doc.to_dict()
            user = cls(
                user_id=doc.id,
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                date_of_birth=data.get("date_of_birth"),
                place_of_birth=data.get("place_of_birth"),
                citizenship=data.get("citizenship"),
            )
            users.append(user)
            logger.info(f"{doc.id} => {data}")
        return users
