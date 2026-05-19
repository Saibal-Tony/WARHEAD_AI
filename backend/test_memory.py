from memory.memory_engine import (
    remember,
    recall
)

remember(
    "favorite_food",
    "chocolate"
)

food = recall(
    "favorite_food"
)

print(food)