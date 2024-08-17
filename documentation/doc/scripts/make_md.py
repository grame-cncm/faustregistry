import os
import shutil
import subprocess
import sys


registry_path = sys.argv[1]
docs_path = sys.argv[2]
awk_script = sys.argv[3]


def create_new_structure(user, library, version):
    user_path = os.path.join(docs_path, "contributors", user)
    library_path = os.path.join(user_path, library)
    version_path = os.path.join(library_path, version)
    
    os.makedirs(version_path, exist_ok=True)
    return version_path

def write_user_overview(user, libraries):
    user_path = os.path.join(docs_path, "contributors", user)
    os.makedirs(user_path, exist_ok=True)
    user_overview_path = os.path.join(user_path, "overview.md")
    
    with open(user_overview_path, "w") as f:
        f.write(f"# {user} Documentation\n\n")
        f.write(f"Welcome to the documentation page for **{user}**. Below you will find a list of libraries contributed by this user, along with links to their respective documentation.\n\n")
        for library in libraries:
            f.write(f"### [{library}](./{library}/overview.md)\n")
        f.write("\n---\nIf you have any questions or need further assistance, feel free to reach out to us.\n")

def write_library_overview(user, library, versions):
    library_path = os.path.join(docs_path, "contributors", user, library)
    os.makedirs(library_path, exist_ok=True)
    library_overview_path = os.path.join(library_path, "overview.md")
    
    with open(library_overview_path, "w") as f:
        f.write(f"# {library} Documentation\n\n")
        f.write(f"Welcome to the documentation for **{library}**. Below you will find an overview of the different versions of this library, along with links to their respective documentation.\n\n")
        for version in versions:
            f.write(f"### [{version}](./{version}/doc.md)\n")

def process_registry():
    for user in os.listdir(registry_path):
        if(user == ".git" or user == "documentation"):
            continue;
        user_path = os.path.join(registry_path, user)

        if os.path.isdir(user_path):
            libraries = []
            for library in os.listdir(user_path):
                library_path = os.path.join(user_path, library)
                if os.path.isdir(library_path):
                    versions = []
                    for version in os.listdir(library_path):
                        version_path = os.path.join(library_path, version)
                        if os.path.isdir(version_path):
                            versions.append(version)
                            new_version_path = create_new_structure(user, library, version)
                            for library_file in os.listdir(version_path):
                                src_file = os.path.join(version_path, library_file)
                                dest_file = os.path.join(new_version_path, "doc.md")
                                with open(dest_file, "w") as outfile:
                                    subprocess.run(["awk", "-f", awk_script, src_file], stdout=outfile)

                    write_library_overview(user, library, versions)
                    libraries.append(library)
            write_user_overview(user, libraries)


contribs_path = os.path.join(docs_path, "contributors");

if os.path.exists(contribs_path):
    shutil.rmtree(contribs_path)

os.makedirs(contribs_path, exist_ok=True)

process_registry()

print("Documentation structure has been successfully created.")
