from memory.memory_engine import (
    remember
)

def process_memory(text):

    text = text.lower()

    # Likes

    if "i like" in text:

        item = text.replace(
            "i like",
            ""
        ).strip()

        remember(
            "likes",
            item
        )

        return (
            f"I will remember that "
            f"you like {item}"
        )

    # Name

    if "my name is" in text:

        name = text.replace(
            "my name is",
            ""
        ).strip()

        remember(
            "user_name",
            name
        )

        return (
            f"Nice to meet you "
            f"{name}"
        )

    return None