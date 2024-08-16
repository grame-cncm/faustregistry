import os
import yaml
import sys

mkdocs_file = sys.argv[1]
contributors_folder = sys.argv[2]

with open(mkdocs_file, 'r') as file:
    mkdocs_config = yaml.safe_load(file)

contributors_nav = []
for contributor in os.listdir(contributors_folder):
    contributor_path = os.path.join(contributors_folder, contributor)
    if os.path.isdir(contributor_path):
        contributor_entry = {contributor: os.path.join('contributors', contributor, 'overview.md')}
        contributors_nav.append(contributor_entry)

nav = mkdocs_config.get('nav', [])
contributors_section = {'Contributors': contributors_nav}

nav_exists = any('Contributors' in section for section in nav)
if not nav_exists:
    nav.append(contributors_section)
else:
    for section in nav:
        if 'Contributors' in section:
            section['Contributors'] = contributors_nav

with open(mkdocs_file, 'w') as file:
    yaml.dump(mkdocs_config, file, sort_keys=False)

print("Contributors section has been added to mkdocs.yml.")
