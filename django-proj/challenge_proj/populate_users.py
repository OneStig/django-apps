import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'challenge_proj.settings')

import django
django.setup()

from appTwo.models import User
from faker import Faker

fakegenerator = Faker()

def populate(N=5):
    for e in range(N):
        fake_name = fakegenerator.name().split()
        fake_first_name = fake_name[0]
        fake_user_name = fake_name[0] + fake_name[1]
        fake_last_name = fake_name[1]
        fake_email = fakegenerator.email()

        user = User.objects.get_or_create(first_name=fake_first_name,
                                          user_name=fake_user_name,
                                          last_name=fake_last_name,
                                          email=fake_email)

if __name__ == '__main__':
    print("populating")
    populate(20)
