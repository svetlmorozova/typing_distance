from setuptools import setup
 

setup(
    name = 'typing_distance',
    version = '0.0.1',
    author = "Svetlana Morozova",
    author_email = "svetl_morozova@mail.ru",
    description = 'Python CLI for string typing distance calculation.',
    packages = ['typing_distance'],
    entry_points = {
        'console_scripts': ['typing_distance = typing_distance.typing_distance:main']
        },
    install_requires=['click']
    )
