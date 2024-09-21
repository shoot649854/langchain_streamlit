from src.models.User import User


def add_user(user_id, first_name, last_name, date_of_birth, place_of_birth, citizenship):
    """Handles the logic to create and save a new user."""
    user = User(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        place_of_birth=place_of_birth,
        citizenship=citizenship,
    )
    user.save()
    return user


def get_user(user_id):
    """Handles the logic to retrieve a specific user."""
    return User.get_single(user_id)


def get_all_users():
    """Handles the logic to retrieve all users."""
    return User.get_all()


def delete_user(user_id):
    """Handles the logic to delete a specific user."""
    User.delete(user_id)
    return f"User {user_id} deleted."
