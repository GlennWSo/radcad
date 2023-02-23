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
            "radcad.boolean.rboolean",
            binding=Binding.PyO3,
            path="./boolean/Cargo.toml",
        ),
    ],
    packages=[
        "radcad.hello",
        "radcad.boolean",
    ],
    # tell setup that the root python source is inside py folder
    package_dir={
        "radcad.hello": "hello/py",
        "radcad.boolean": "boolean",
    },
    # entry_points={
    #     "console_scripts": ["greet=hello:greet"],
    # },
    zip_safe=False,
)