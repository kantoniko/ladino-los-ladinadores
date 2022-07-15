import os
from yaml import safe_load

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(root)
with open(os.path.join(root, 'afishes.yaml')) as fh:
    data = safe_load(fh)
images_dir = os.path.join(root, 'docs', 'afishes')

images = set(os.listdir(images_dir))

images_in_yaml = set()

for entry in data:
    assert 'title' in entry
    assert len(entry['title']) > 10
    assert 'img' in entry
    assert os.path.exists(os.path.join(images_dir, entry['img']))
    images_in_yaml.add(entry['img'])

assert images == images_in_yaml

print("Everything looks fine")
