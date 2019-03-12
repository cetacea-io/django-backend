from django.core.management.base import BaseCommand

from users.factories import UserFactory
from courses.factories import CourseFactory
from taxonomies.factories import CategoryFactory, TagFactory

import random

class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users', 
            default=1,
            type=int,
            help='The number of fake users to create.')
    
    def handle(self, *args, **options):
        # for _ in range(options['users']):
        #     print(UserFactory.create())
        populate()


def populate():
    # Create 20 categories
    for _ in range(20):
        CategoryFactory.create()

    from category.models import Category
    categories = list(Category.objects.all()).copy()

    # Create the Admin user
    UserFactory.create(username='admin', is_staff=True, is_superuser=True)

    # Create 10 users
    for _ in range(10):
        UserFactory.create()

    # Create 100 courses
    for _ in range(100):
        random.shuffle(categories)
        n = random.randint(1, 6)
        new_categories = []
        for x in range(n):
            new_categories.append(categories[x])
        CourseFactory.create(categories=tuple(new_categories))