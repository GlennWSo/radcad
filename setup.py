#!/usr/bin/env python

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="radcad",
    version="0.0.1",
    description="cad stuff written in rust with python bindings",
    author="Glenn",
    author_email="gward@python.net",
    rust_extensions=[
        RustExtension(
            "radcad.hello.rhello",
            binding=Binding.PyO3,
            path="./hello/Cargo.toml",
        ),
        RustExtension(
            "radcad.add_one.radd_one",
            binding=Binding.PyO3,
            path="./add_one/Cargo.toml",
        ),
    ],
    packages=[
        "radcad.hello",
        "radcad.add_one",
        "radcad.adder",
    ],
    # tell setup that the root python source is inside py folder
    package_dir={
        "radcad.hello": "hello/py",
        "radcad.add_one": "add_one",
        "radcad.adder": "adder",
    },
    # entry_points={
    #     "console_scripts": ["greet=hello:greet"],
    # },
    zip_safe=False,
)
