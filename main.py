import os
import random
from faker import Faker
import file_operations


RUNES = {
    "а": "а͠ ", "б": "б̋ ", "в": "в͒͠ ",
    "г": "г͒͠ ", "д": "д̋ ", "е": "е͠ ",
    "ё": "ё͒͠ ", "ж": "ж͒ ", "з": "з̋̋͠ ",
    "и": "и ", "й": "й͒͠ ", "к": "к̋̋ ",
    "л": "л̋͠ ", "м": "м͒͠ ", "н": "н͒ ",
    "о": "о̋ ", "п": "п̋͠ ", "р": "р̋͠ ",
    "с": "с͒ ", "т": "т͒ ", "у": "у͒͠ ",
    "ф": "ф̋̋͠ ", "х": "х͒͠ ", "ц": "ц̋ ",
    "ч": "ч̋͠ ", "ш": "ш͒͠ ", "щ": "щ̋ ",
    "ъ": "ъ̋͠ ", "ы": "ы̋͠ ", "ь": "ь̋ ",
    "э": "э͒͠͠ ", "ю": "ю̋͠ ", "я": "я̋ ",
    "А": "А͠ ", "Б": "Б̋ ", "В": "В͒͠ ",
    "Г": "Г͒͠ ", "Д": "Д̋ ", "Е": "Е",
    "Ё": "Ё͒͠ ", "Ж": "Ж͒ ", "З": "З̋̋͠ ",
    "И": "И ", "Й": "Й͒͠ ", "К": "К̋̋ ",
    "Л": "Л̋͠ ", "М": "М͒͠ ", "Н": "Н͒ ",
    "О": "О̋ ", "П": "П̋͠ ", "Р": "Р̋͠ ",
    "С": "С͒ ", "Т": "Т͒ ", "У": "У͒͠ ",
    "Ф": "Ф̋̋͠ ", "Х": "Х͒͠ ", "Ц": "Ц̋ ",
    "Ч": "Ч̋͠ ", "Ш": "Ш͒͠ ", "Щ": "Щ̋ ",
    "Ъ": "Ъ̋͠ ", "Ы": "Ы̋͠ ", "Ь": "Ь̋ ",
    "Э": "Э͒͠͠ ", "Ю": "Ю̋͠ ", "Я": "Я̋ ",
    " ": " "
}


def generate_rune_skills(skills):
    rune_skills = []
    for skill in skills:
        converted = skill
        for char, rune in RUNES.items():
            converted = converted.replace(char, rune)
        rune_skills.append(converted)
    return rune_skills


def generate_character_context(fake_gen, skills):
    context = {
        "first_name": fake_gen.first_name(),
        "last_name": fake_gen.last_name(),
        "job": fake_gen.job(),
        "town": fake_gen.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": skills[0],
        "skill_2": skills[1],
        "skill_3": skills[2],
    }
    return context


def main():
    fake = Faker("ru_RU")
    new_dir = "charsheet"
    os.makedirs(new_dir, exist_ok=True)

    skills = [
        "Стремительный прыжок",
        "Электрический выстрел",
        "Ледяной удар",
        "Стремительный удар",
        "Кислотный взгляд",
        "Тайный побег",
        "Ледяной выстрел",
        "Огненный заряд"
    ]

    rune_skills = generate_rune_skills(skills)

    for number in range(1, 11):
        random_skills = random.sample(rune_skills, k=3)
        context = generate_character_context(fake, random_skills)
        filename = os.path.join(new_dir, f"charsheet_{number}.svg")
        file_operations.render_template("template.svg", filename, context)


if __name__ == "__main__":
    main()
