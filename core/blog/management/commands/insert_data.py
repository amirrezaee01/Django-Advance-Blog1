from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone

from accounts.models import User, Profile
from blog.models import Post, Category


class Command(BaseCommand):
    help = 'Insert fake data into the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Step 1: Create specific categories
        category_names = ['IT', 'DJANGO', 'PYTHON', 'JS', 'HTML', 'CSS']
        categories = []

        for name in category_names:
            category, _ = Category.objects.get_or_create(name=name)
            categories.append(category)

        self.stdout.write(self.style.SUCCESS(
            "✅ Created categories: " + ", ".join(category_names)))

        # Step 2: Create fake users, profiles, and posts
        for _ in range(5):
            user = User.objects.create_user(
                email=fake.email(),
                password='TEST@//123456'
            )

            profile = Profile.objects.get(user=user)
            profile.first_name = fake.first_name()
            profile.last_name = fake.last_name()
            profile.description = fake.text(max_nb_chars=100)
            profile.save()

            self.stdout.write(self.style.SUCCESS(
                f"👤 Created user {user.email}."))

            # Create 1–3 posts per user
            for _ in range(random.randint(1, 3)):
                post = Post.objects.create(
                    author=profile,
                    title=fake.sentence(nb_words=6),
                    content=fake.paragraph(nb_sentences=10),
                    status=random.choice([True, False]),
                    category=random.choice(categories),
                    published_date=timezone.now() - timedelta(days=random.randint(1, 100))
                )

                self.stdout.write(self.style.SUCCESS(
                    f"📝 → Created post: {post.title}"))
