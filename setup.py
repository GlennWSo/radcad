#!/usr/bin/env python

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="hello",
    version="0.13.37",
    description="derp",
    author="It me!",
    author_email="gward@python.net",
    rust_extensions=[
        RustExtension(
            "hello.rhello",
            binding=Binding.PyO3,
            path="./hello/Cargo.toml",
        )
    ],
    packages=["hello"],
    # tell setup that the root python source is inside py folder
    package_dir={"hello": "hello/py"},
    # entry_points={
    #     "console_scripts": ["greet=hello:greet"],
    # },
    zip_safe=False,
)
