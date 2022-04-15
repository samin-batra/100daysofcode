import requests

class Post:
    def __init__(self):
        self.api_url="https://api.npoint.io/e99299dc2a4450416132"
        res = requests.get(self.api_url)
        self.blog_posts = res.json()

    def get_all(self):
        return self.blog_posts

    def get_blog_post(self, index: int):
        if index<=len(self.blog_posts):
            return self.blog_posts[index-1]
        return None

