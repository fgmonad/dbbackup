import pytest

from dbbackup import cli

url = "mysql://user:pass@example.com:3608/dbname"


@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    The parser will exit if it receives a driver without a
    destination.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and
    a destionation.
    """
    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.driver == 'local'
    assert args.destination == '/some/path'


def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the driver name is unknown
    """

    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'digital-ocean', 'destination'])


def test_parser_with_known_drivers(parser):
    """
    The parser will not exit if the driver name is known.
    """

    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])
