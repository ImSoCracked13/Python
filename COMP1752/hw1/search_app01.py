import os

default_root_path = os.path.expanduser("~" + os.sep + "Documents")
recursive = True
case_sensitive = False
match_phrase = False
extensions = ["py", "txt"]
print_depth = 1
debug = False


def readlines(path):
    """Return contents of text file as a list of lines."""
    with open(path) as file:
        try:
            return file.readlines()
        except UnicodeDecodeError:
            print(f" unicode error in {path}")
            return []


def index_and_search(dirname, root_path_length, search_strings, depth, results, extensions):
    if debug:
        print(dirname)
    try:
        filenames = os.listdir(dirname)
    except PermissionError:
        return
    for filename in filenames:
        path = dirname + os.sep + filename
        if os.path.isdir(path):
            if recursive:
                if depth < print_depth:
                    print(path)
                index_and_search(path, root_path_length, search_strings, depth + 1, results, extensions)
        else:
            if "." not in filename:
                continue
            extension = filename.split(".")[-1]
            if extension not in extensions:
                continue
            lines = readlines(path)
            search_occurrences = 0
            for line in lines:
                if not case_sensitive:
                    line = line.lower()
                for string in search_strings:
                    search_occurrences += line.count(string)
            if search_occurrences > 0:
                search_result = f" {search_occurrences:4} {path[root_path_length:]}"
                results.append(search_result)
                if debug:
                    print(f"{search_occurrences:4} {path[root_path_length:]}")
    if depth == 0:
        results.sort(reverse=True)
        print()
        print("FINAL RESULTS")
        for search_result in results:
            print(search_result)
        print(f" {len(results)} files found")


while True:
    print()
    search_string = input("Search string? ")
    if search_string == "":
        break
    if not case_sensitive:
        search_string = search_string.lower()
    if not match_phrase:
        search_strings = search_string.split()
    else:
        search_strings = [search_string]
    root_path = default_root_path
    print(f"using extensions {extensions}")
    results = []
    if os.path.isdir(root_path):
        index_and_search(root_path, len(root_path) + 1, search_strings, 0, results, extensions)
