import os
import random
from faker import Faker
import file_operations
from runes_dict import runes


def generate_rune_skills(skills):
    rune_skills = []
    for skill in skills:
        converted = skill
        for char, rune in runes.items():
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
      

if __name__ == '__main__':
    main()