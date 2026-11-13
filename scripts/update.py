import sys
import yaml

def update_tag(file_path, new_tag):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    data["image"]["tag"] = new_tag

    with open(file_path, "w") as file:
        yaml.safe_dump(data, file, sort_keys=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python update_tag.py <yaml_file> <new_tag>")
        sys.exit(1)

    update_tag(sys.argv[1], sys.argv[2])
    print(f"Image tag updated to {sys.argv[2]}")