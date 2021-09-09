"""Creates the hashsum of a directory"""

__version__ = "0.0.1"

import argparse
import hashlib
import pathlib


def hash_file(path: pathlib.Path):
    return hashlib.sha1(path.read_bytes()).digest()


def hash_tree(path: pathlib.Path):
    hasher = hashlib.sha1()

    for p in path.rglob("*"):
        if p.is_file():
            hasher.update(hash_file(p))
    return hasher.hexdigest()


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=pathlib.Path, help="Path")
    args = parser.parse_args()
    print(hash_tree(args.path))