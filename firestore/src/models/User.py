from src import db  # type: ignore
from src.Logging.Logging import logger


class User:
    def __init__(self, user_id, first_name, last_name, date_of_birth, place_of_birth, citizenship):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.citizenship = citizenship

    def create(self):
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

    def update(self, **kwargs):
        """Updates specific fields of a user in Firestore."""
        user_ref = db.collection("users").document(self.user_id)
        updated_fields = {key: value for key, value in kwargs.items() if value is not None}

        if updated_fields:
            user_ref.update(updated_fields)
            logger.info(f"User {self.user_id} updated with fields: {updated_fields}.")
        else:
            logger.warning(f"No valid fields provided to update for user {self.user_id}.")

    @classmethod
    def get_single(cls, user_id):
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
            logger.warning("No such document!")
            return None

    @classmethod
    def get_all(cls):
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

    @classmethod
    def delete_single(cls, user_id):
        """Deletes a user from Firestore by user_id."""
        user_ref = db.collection("users").document(user_id)
        if user_ref.get().exists:
            user_ref.delete()
            logger.info(f"User with ID {user_id} has been deleted from Firestore.")
        else:
            logger.warning(f"User with ID {user_id} does not exist.")
