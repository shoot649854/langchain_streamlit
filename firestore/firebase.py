from src.Controllers.Controllers import get_all_users, get_user  # add_user


def main():
    # add_user(
    #     user_id="jdoe",
    #     first_name="John",
    #     last_name="Doe",
    #     date_of_birth="1990-01-01",
    #     place_of_birth="New York",
    #     citizenship="USA",
    # )

    get_user("jdoe")

    # Example: Listing all users
    get_all_users()


if __name__ == "__main__":
    main()
