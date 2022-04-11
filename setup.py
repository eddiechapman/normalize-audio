from setuptools import setup

setup(
    name="normalize-audio",
    version="0.1.0",
    py_modules=["normalize"],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "normalize = normalize:normalize"
        ],
    },
)