from pymongo import MongoClient
from bson.objectid import ObjectId

# Параметри підключення
client = MongoClient("mongodb://localhost:27017/")
db = client['cats_db']
collection = db['cats']

# Читання всіх записів
def read_all_cats():
    for cat in collection.find():
        print(cat)

# Знайти кота за ім'ям
def find_cat_by_name(name):
    cat = collection.find_one({"name": name})
    print(cat)

# Оновити вік кота
def update_cat_age(name, new_age):
    collection.update_one({"name": name}, {"$set": {"age": new_age}})

# Додати характеристику
def add_cat_feature(name, feature):
    collection.update_one({"name": name}, {"$addToSet": {"features": feature}})

# Видалити кота
def delete_cat(name):
    collection.delete_one({"name": name})

# Видалити всіх котів
def delete_all_cats():
    collection.delete_many({})

# Приклад використання
if __name__ == "__main__":
    # Додати кота (приклад)
    collection.insert_one({"name": "barsik", "age": 3, "features": ["ходит в капці", "дає себе гладити", "рудий"]})
    
    read_all_cats()
    find_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_cat_feature("barsik", "добрий")
    delete_cat("barsik")
    delete_all_cats()
