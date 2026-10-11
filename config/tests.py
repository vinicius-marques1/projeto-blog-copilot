from django.test import SimpleTestCase
from django.urls import reverse


class HomeViewTests(SimpleTestCase):
    def test_home_returns_200(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_uses_expected_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_home_contains_blog_name_and_welcome_text(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Blog Green")
        self.assertContains(
            response,
            "Esse é uma blog para postar coisa legais sobre tecnologia!! "
            "Seja bem vindo(a)!!",
        )

    def test_home_navbar_links_to_posts_and_sobre(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, reverse("posts"))
        self.assertContains(response, reverse("sobre"))


class PostsViewTests(SimpleTestCase):
    def test_posts_returns_200(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)

    def test_posts_uses_expected_template(self):
        response = self.client.get(reverse("posts"))
        self.assertTemplateUsed(response, "posts.html")
        self.assertTemplateUsed(response, "base.html")

    def test_posts_contains_heading(self):
        response = self.client.get(reverse("posts"))
        self.assertContains(response, "Posts")


class SobreViewTests(SimpleTestCase):
    def test_sobre_returns_200(self):
        response = self.client.get(reverse("sobre"))
        self.assertEqual(response.status_code, 200)

    def test_sobre_uses_expected_template(self):
        response = self.client.get(reverse("sobre"))
        self.assertTemplateUsed(response, "sobre.html")
        self.assertTemplateUsed(response, "base.html")

    def test_sobre_contains_heading(self):
        response = self.client.get(reverse("sobre"))
        self.assertContains(response, "Sobre Nós")
