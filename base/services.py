import re

def slugify(name):
  slug = name.lower().strip()
  slug = re.sub(r'[^\w\s-]', '', slug)
  slug = re.sub(r'[\s_-]+', '-', slug)
  slug = re.sub(r'^-+|-+$', '', slug)
  return slug