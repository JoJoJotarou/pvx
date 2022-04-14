from setuptools import setup, find_packages

setup(
    name="pvx",
    author="JoJoJotarou",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click>=8.1.2",
        "rich>=12.2.0",
        "pexpect>=4.8.0",
    ],
    entry_points="""
        [console_scripts]
        pvx=pvx:pvx
    """,
)
