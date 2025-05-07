from ghost_client import GhostClient
import requests
from urllib.parse import urlparse
from markdown2 import markdown  # For Markdown-to-HTML conversion

# Configuration
GHOST_API_URL = "https://broward.ghost.io"
ADMIN_API_KEY = "your-admin-api-key"  # From Ghost admin
POST_URL = "https://broward.ghost.io/gold-token-white-paper/"
GITHUB_FILE_URL = "https://raw.githubusercontent.com/broward/token/main/whitepaper.md"
API_VERSION = "v5.0"

# Initialize Ghost Client
client = GhostClient(host=GHOST_API_URL, api_key=ADMIN_API_KEY, api_version=API_VERSION)

# Extract slug from URL
def get_slug_from_url(post_url):
    return urlparse(post_url).path.strip("/").split("/")[-1]

# Delete post by URL
def delete_post_by_url(post_url):
    try:
        slug = get_slug_from_url(post_url)
        posts = client.posts.list(filter=f"slug:{slug}")
        if not posts:
            print(f"No post found for slug: {slug}. Available slugs:")
            print([p["slug"] for p in client.posts.list()])
            return False
        client.posts.delete(posts[0]["id"])
        print(f"Deleted post: {slug}")
        return True
    except Exception as e:
        print(f"Delete error: {str(e)}")
        return False

# Fetch and convert GitHub content
def fetch_github_content(github_url):
    try:
        response = requests.get(github_url, timeout=10)
        response.raise_for_status()
        content = markdown(response.text)  # Convert Markdown to HTML
        print(f"Fetched GitHub content (first 100 chars): {content[:100]}")
        return content
    except Exception as e:
        print(f"GitHub fetch error: {str(e)}")
        return None

# Create new post
def create_post(slug, content):
    post_data = {
        "title": "Gold Token White Paper",
        "html": content or "<p>Error: No content fetched.</p>",
        "slug": slug,
        "status": "published",
        "tags": ["Gold Token", "White Paper", "Crypto"],
        "authors": ["your-author-email"],  # Update with Ghost user email
        "feature_image": "https://broward.ghost.io/content/images/gold-token-image.jpg"  # Optional
    }
    try:
        new_post = client.posts.create(post_data)
        print(f"Created post at {new_post['url']}")
        return True
    except Exception as e:
        print(f"Create error: {str(e)}")
        return False

# Main
def main():
    slug = get_slug_from_url(POST_URL)
    if not delete_post_by_url(POST_URL):
        print("Aborting: Failed to delete post.")
        return
    content = fetch_github_content(GITHUB_FILE_URL)
    if not content:
        print("Aborting: Failed to fetch content.")
        return
    if create_post(slug, content):
        print("Success! Post updated.")
    else:
        print("Failed to create post.")

if __name__ == "__main__":
    main()
