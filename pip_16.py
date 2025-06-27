import pathlib
import os

print("\n  1. creating path objects")

#current working direcory
print(pathlib.Path)
current_dir = pathlib.Path.cwd()
print(f"current working directory(path object): {current_dir}")


#relative path
relative_file = pathlib.Path("my_document.txt")
print(f"relative file path: {relative_file}")

#absolute path
absolute_path = pathlib.Path("/tmp/test_dir")
print(f"absolute path: {absolute_path}")

#join paths
joined_path = current_dir / 'data' / 'reports' / 'report.csv'
print(f"joned path: {joined_path}")

#accessing path components
print("\n  2. accessing path components")
print(f"full path: {joined_path}")
print(f"file/folder name: {joined_path.name}") #'report.csv'
print(f"parent directory: {joined_path.parent}") #path/to/current/dir/data/........
print(f"file stem(name without suffix): {joined_path.stem}") #report
print(f"file suffix(etension): {joined_path.suffix}") #.csv
print(f"all suffixes: {joined_path.suffixes}") #['.csv']
print(f"anchor(root of the path): {joined_path.anchor}") #................
print(f"path parts: {joined_path.parts}") #................