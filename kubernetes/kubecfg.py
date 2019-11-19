import argparse
import os
import shutil
from pathlib import Path


def use(args):
    kube = Path.home() / ".kube"
    src = kube / "config.d" / args.name
    dst = kube / "config"
    shutil.copyfile(src, dst)
    print(f"use {src}")


def save(args):
    kube = Path.home() / ".kube"
    src = kube / "config"
    dst = kube / "config.d" / args.name
    os.makedirs(kube / "config.d", exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"save {dst}")


def delete(args):
    kube = Path.home() / ".kube"
    f = kube / "config.d" / args.name
    os.remove(f)
    print(f"delete {f}")


parser = argparse.ArgumentParser()
parser_subparsers = parser.add_subparsers()
subparser_use = parser_subparsers.add_parser('use')
subparser_use.add_argument("name")
subparser_use.set_defaults(func=use)
subparser_save = parser_subparsers.add_parser('save')
subparser_save.add_argument("name")
subparser_save.set_defaults(func=save)
subparser_delete = parser_subparsers.add_parser('delete')
subparser_delete.add_argument("name")
subparser_delete.set_defaults(func=delete)

args = parser.parse_args()
args.func(args)
