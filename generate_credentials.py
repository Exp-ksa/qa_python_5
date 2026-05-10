from faker import Faker
import random

faker = Faker('ru_RU')

def generate_random_credentials():
    # Генерируем имя
    first_name = faker.first_name()

    # Генерируем email
    digits = f"{random.randint(0, 999):03d}"  # Всегда 3 цифры с ведущими нулями
    email = f"sergey_kuznetsov_45_{digits}@yandex.ru"
    
    # Пароль 
    password = faker.password(length=6, special_chars=True, digits=True)
    
    return first_name, email, password