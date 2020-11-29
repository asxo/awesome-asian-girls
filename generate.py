# Fill in the list with sites

import os

template = "template.md"
directory = "websites"
index_md = directory + "/{site}/index.md"
item = "- [{site}](/" + index_md + ")"
output = "README.md"

all_sites = []
original = []
high = []
medium = []
downloading = []


def process_site(site):
    all_sites.append(site)

    with open(index_md.format(site=site), "r") as file:
        for line in file.readlines():
            if line.startswith("- Resolution: **"):
                resolution = line[line.index("**") + 2 :][:-3]
                if resolution.lower() == "original":
                    original.append(site)
                elif resolution.lower() == "high":
                    high.append(site)
                elif resolution.lower() == "medium":
                    medium.append(site)
                else:
                    raise Exception("Undefined resolution: " + resolution)

            elif line.startswith("- Downloading: "):
                if "вњ”пёЏ" in line:  # ✔️
                    downloading.append(site)


def fill_template():
    with open(template, "r") as file:
        content = file.read()

    content = content.format(
        all=generate_items(all_sites),
        original=generate_items(original),
        high=generate_items(high),
        medium=generate_items(medium),
        downloading=generate_items(downloading),
    )

    with open(output, "w") as file:
        file.write(content)


def generate_items(items):
    return "\n".join([item.format(site=i) for i in items])


def main():
    sites = os.listdir(directory)
    sites.remove("_example")
    sites.sort()

    for site in sites:
        process_site(site)

    fill_template()


if __name__ == "__main__":
    main()
