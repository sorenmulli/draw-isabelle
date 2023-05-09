from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    required = [
        l.strip()
        for l in f.read().splitlines()
        if l.strip() and not l.strip().startswith("#")
    ]

# pylint: disable=use-dict-literal
setup_args = dict(
    name="draw_isabelle",
    version="0.0.1",
    packages=find_packages(),
    author="Søren Winkel Holm",
    author_email="swholm@protonmail.com",
    url="https://github.com/sorenmulli",
    download_url="https://pypi.org/project/draw_isabelle",
    install_requires=required,
    description="",
    long_description_content_type="text/markdown",
    long_description=readme,
    license="MIT",
    entry_points={
        "console_scripts": [
            "draw-isabelle = draw_isabelle.__main__:run_from_cli",
        ]
    },
)

if __name__ == "__main__":
    setup(**setup_args)
