from src.models.User import User


def add_user_controller(user_id, first_name, last_name, date_of_birth, place_of_birth, citizenship):
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


def get_user_controller(user_id):
    """Handles the logic to retrieve a specific user."""
    user = User.get(user_id)
    return user


def list_all_users_controller():
    """Handles the logic to retrieve all users."""
    users = User.list_all()
    return users
