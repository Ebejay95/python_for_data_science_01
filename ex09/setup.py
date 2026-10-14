from setuptools import setup, find_packages


def main():
    """Build the ft_package distribution."""
    with open("README.md", "r", encoding="utf-8") as readme:
        long_description = readme.read()
    setup(
        name="ft_package",
        version="0.0.1",
        description="A sample test package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/jeberle/ft_package",
        author="jeberle",
        author_email="jeberle@student.42heilbronn.de",
        license="MIT",
        packages=find_packages(),
        python_requires=">=3.10",
    )


if __name__ == "__main__":
    main()
