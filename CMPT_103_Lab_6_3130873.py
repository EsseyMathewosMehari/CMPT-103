# ID# 3130873
# Lab 6
import os
def add_user(user: str) -> bool:
    """
    Add a user to the system.

    Parameters: The username to be added.
    
    Return: True if the user is successfully added, False otherwise.
     bool
    """
    # Validate the username
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-")
    if not all(char in valid_chars for char in user):
        return False

    # Check if user_data.txt file exists, and if not, create it
    try:
        with open("user_data.txt", "r") as file:
            existing_users = set(line.strip() for line in file)
    except FileNotFoundError:
        existing_users = set()

    # Check if the user already exists in the set
    if user in existing_users:
        return False

    # If the user is not a duplicate, add them to the set and write to the file
    existing_users.add(user)
    with open("user_data.txt", "w") as file:
        file.write("\n".join(existing_users))

    return True

def ban_user(user: str) -> bool:
    """
    Ban a user from the system.

    Parameters:
        user: The username to be banned.

    Return:
    bool: True if the user is successfully banned, False otherwise.
    """
    # Validate the username
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-")
    if not all(char in valid_chars for char in user):
        return False

    # Check if the user_data.txt file exists, if not, create it
    if not os.path.exists("user_data.txt"):
        return False

    # Check if the banned_users.txt file exists, if not, create it
    if not os.path.exists("banned_users.txt"):
        with open("banned_users.txt", "w"):
            pass

    # Read existing users from user_data.txt
    with open("user_data.txt", "r") as user_data_file:
        existing_users = set(line.strip() for line in user_data_file)

    # Check if the user exists in the set of current users
    if user not in existing_users:
        return False

    # Read existing banned users from banned_users.txt
    with open("banned_users.txt", "r") as banned_users_file:
        banned_users = set(line.strip() for line in banned_users_file)

    # Check if the user is already in the set of banned users
    if user in banned_users:
        return False

    # If the user is not banned, add them to the set of banned users and write to banned_users.txt
    banned_users.add(user)
    with open("banned_users.txt", "w") as banned_users_file:
        banned_users_file.write("\n".join(banned_users))

    return True

def write_message(user: str, message: str) -> bool:
    """
    Write a message from a user to the system.

    Parameters:
        - user: The username of the sender.
        - message: The message content.

    Return:
    bool: True if the message is successfully written, False otherwise.
    """
    # Validate the username
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-")
    if not all(char in valid_chars for char in user):
        return False

    # Validate that the user exists and is not banned
    if not is_user_valid(user):
        return False

    # Replace newline characters with "<NEWLINE>"
    message = message.replace('\n', '<NEWLINE>')

    # Create the message format (user|message)
    message_format = f"{user}|{message}"

    # Check if the "messages.txt" file exists, if not, create it
    if not os.path.exists("messages.txt"):
        with open("messages.txt", "w"):
            pass

    # Append the message to "messages.txt"
    with open("messages.txt", "a") as messages_file:
        messages_file.write(message_format + '\n')

    return True

def is_user_valid(user):
    """
    Check if a user is valid (exists and is not banned).

    Parameters:
    user: The username to be checked.

    Return:
    bool: True if the user is valid, False otherwise.
    """
    # Check if the user is in user_data.txt and not in banned_users.txt
    if os.path.exists("user_data.txt") and os.path.exists("banned_users.txt"):
        with open("user_data.txt", "r") as user_data_file:
            users = set(line.strip() for line in user_data_file)

        with open("banned_users.txt", "r") as banned_users_file:
            banned_users = set(line.strip() for line in banned_users_file)

        if user in users and user not in banned_users:
            return True

    return False

def read_messages(user: str):
    """
    Read and print messages for a user.

    Parameters:
    user: The username of the user whose messages to read.
    """

    # Validate the user name
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-")
    if not all(char in valid_chars for char in user):
        print("User not found")
        return

    # Check if the user exists and is not banned
    if not is_user_valid(user):
        if is_user_banned(user):
            print("Sorry, you are banned")
        else:
            print("User not found")
        return

    # Check if the "messages.txt" file exists
    if not os.path.exists("messages.txt"):
        print("Sorry, there are no messages to read.")
        return

    # Read and print messages from "messages.txt"
    with open("messages.txt", "r") as messages_file:
        for line in messages_file:
            parts = line.strip().split("|")
            if len(parts) == 2:
                message_user, message_content = parts
                if message_user == user:
                    print(f"[{message_user}]: {message_content.replace('<NEWLINE>', '\n')}")

def is_user_valid(user):
    # Check if the user is in user_data.txt and not in banned_users.txt
    if os.path.exists("user_data.txt") and os.path.exists("banned_users.txt"):
        with open("user_data.txt", "r") as user_data_file:
            users = set(line.strip() for line in user_data_file)

        with open("banned_users.txt", "r") as banned_users_file:
            banned_users = set(line.strip() for line in banned_users_file)

        if user in users and user not in banned_users:
            return True

    return False

def is_user_banned(user):
    """
    Check if a user is banned.

    Parameters:
    user: The username to be checked.

    Return:
    bool: True if the user is banned, False otherwise.
    """
    # Check if the user is in banned_users.txt
    if os.path.exists("banned_users.txt"):
        with open("banned_users.txt", "r") as banned_users_file:
            banned_users = set(line.strip() for line in banned_users_file)

        if user in banned_users:
            return True

    return False