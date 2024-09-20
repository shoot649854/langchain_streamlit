import logging

from src.Controllers.Controllers import (
    add_user_controller,
    get_user_controller,
    list_all_users_controller,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    add_user_controller(
        user_id="jdoe",
        first_name="John",
        last_name="Doe",
        date_of_birth="1990-01-01",
        place_of_birth="New York",
        citizenship="USA",
    )

    user = get_user_controller("jdoe")
    if user:
        print(f"Retrieved User: {user.first_name} {user.last_name}")
    else:
        print("User not found.")

    # Example: Listing all users
    users = list_all_users_controller()
    print("\nAll Users:")
    for user in users:
        print(
            f"{user.user_id}: {user.first_name} {user.last_name}, "
            f"DOB: {user.date_of_birth}, "
            f"Place of Birth: {user.place_of_birth}, "
            f"Citizenship: {user.citizenship}"
        )


if __name__ == "__main__":
    main()
