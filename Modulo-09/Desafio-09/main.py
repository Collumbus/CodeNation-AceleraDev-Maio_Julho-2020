# .travis.yml

config = """

    language: python

    python:

        - '2.7'

        - '2.7.13'

        - '3.7'

        - '3.6.1'

        - 'pypy'

        - 'pypy3'



    # command to install dependencies

    install:

        pip install -r requirements.txt



    # command to run tests

    script: pytest

"""