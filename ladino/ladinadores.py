import os
from yaml import safe_load

def load_ladinadores(root):
    with open(os.path.join(root, 'afishes.yaml')) as fh:
        data = safe_load(fh)
    images_dir = os.path.join(root, 'docs', 'afishes')
    yaml_dir = os.path.join(root, 'afishes')
    for filename in os.listdir(yaml_dir):
        print(filename)
        img_filename = filename[0:-4] + 'jpg'
        print(img_filename)
        assert os.path.exists(os.path.join(images_dir, img_filename))
        with open(os.path.join(yaml_dir, filename)) as fh:
            this = safe_load(fh)

    images = set(os.listdir(images_dir))

    images_in_yaml = set()

    for entry in data:
        assert 'titulo' in entry
        assert len(entry['titulo']) > 5
        assert 'img' in entry
        assert os.path.exists(os.path.join(images_dir, entry['img']))
        images_in_yaml.add(entry['img'])

    if images != images_in_yaml:
        print(images-images_in_yaml)
        exit(1)

    return data

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(root)
    data = load_ladinadores(root)
    print("Everything looks fine")
    print(data)

