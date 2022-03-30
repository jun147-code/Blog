from django.test import TestCase
from django.contrib.auth.models import User

from post.models import Post

# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create test user
        testUser1 = User.objects.create_user(
            username="12", 
            password="abc123"
        )
        testUser1.save()

        # Create test post
        test_post = Post.objects.create(
            author=testUser1, 
            title='Blog title', 
            body='Body content...'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, '12')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')
    
