from setuptools import setup, find_packages

setup(
    name="marzban-shortlinks",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
        "pymysql",
    ],
    entry_points={
        "console_scripts": [
            "marzban-shortlinks=cli:main",
        ],
    },
)
