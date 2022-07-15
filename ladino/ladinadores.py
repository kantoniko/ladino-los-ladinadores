import os
from yaml import safe_load

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(root)
with open(os.path.join(root, 'afishes.yaml')) as fh:
    data = safe_load(fh)
for entry in data:
    assert 'title' in entry
    assert len(entry['title']) > 10
    assert 'img' in entry
    assert os.path.exists(os.path.join(root, 'docs', 'afishes', entry['img']))

print("Everything looks fine")
