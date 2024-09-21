from src.Controllers.Controllers import (  # create_user,
    get_all_users,
    get_user,
    update_user,
)


def main():
    # create_user(
    #     user_id="jdoe",
    #     first_name="John",
    #     last_name="Doe",
    #     date_of_birth="1990-01-01",
    #     place_of_birth="New York",
    #     citizenship="USA",
    # )

    get_user("jdoe")
    get_user("jdoeee")
    get_all_users()

    update_user(
        user_id="user123",
        first_name="NewFirstName",
        last_name="NewLastName",
    )


if __name__ == "__main__":
    main()
