from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from blog.models import Author, Comment, Post

fake = Faker()


class Command(BaseCommand):
    help = "Generate fake data for the blog app"

    def add_arguments(self, parser):
        parser.add_argument(
            "--num_users",
            type=int,
            default=10,
            help="Number of users to generate",
        )

        parser.add_argument(
            "--num_posts",
            type=int,
            default=10,
            help="Number of posts per author to generate",
        )

        parser.add_argument(
            "--num_comments",
            type=int,
            default=10,
            help="Number of comments per post to generate",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        num_users = options["num_users"]
        num_posts = options["num_posts"]
        num_comments = options["num_comments"]

        # Create users and authors
        for _ in range(num_users):
            user_email = fake.email()
            user = get_user_model().objects.create_user(
                email=user_email,
                password=user_email,
                avatar=None,
            )

            author = Author.objects.create(
                user=user,
                bio=fake.sentence(),
            )

            # Create posts for each author
            for _ in range(num_posts):
                post = Post.objects.create(
                    author=author,
                    title=fake.sentence(),
                    content=fake.text(),
                )

                # Create comments for each post
                for _ in range(num_comments):
                    Comment.objects.create(
                        user=get_user_model().objects.order_by("?").first(),
                        post=post,
                        content=fake.text(),
                    )

        self.stdout.write(
            self.style.SUCCESS(
                (
                    f"Successfully created {num_users} users, "
                    f"{num_posts} posts per author, "
                    f"and {num_comments} comments per post."
                ),
            ),
        )
