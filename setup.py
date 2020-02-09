from setuptools import setup


install_requires = []

setup(
    name='tic-tac-toe',
    packages=['tic_tac_toe'],
    scripts=['bin/ttt'],
    version="0.0.1",
    description="Tic-Tac-Toe Game",
    long_description=open('README.md').read(),
    keywords=['tic-tac-toe', 'game', 'console', 'terminal'],
    author="dslackw",
    author_email="d.zlatanidis@gamil.com",
    url="https://github.com/dslackw/Tic_Tac_Toe",
    package_data={'': ['LICENSE.txt', 'README.md']},
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
        ],
    python_requires='>=3.7'
)
