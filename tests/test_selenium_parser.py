from deeptrace.core.parsers.har_generic import HarParser
from deeptrace.core.parsers.json_generic import JSONGenericParser


def test_selenium_actions() -> None:
    parser = JSONGenericParser()
    result = parser.parse("examples/selenium_actions.json")
    assert len(result) == 2
    assert result[0].name == "Navigate"
    print("selenium_actions.json: OK")


def test_selenium_array() -> None:
    parser = JSONGenericParser()
    result = parser.parse("examples/selenium_array.json")
    assert len(result) == 2
    assert result[0].name == "Click login"
    print("selenium_array.json: OK")


def test_selenium_events() -> None:
    parser = JSONGenericParser()
    result = parser.parse("examples/selenium_events.json")
    assert len(result) == 2
    assert result[0].name == "Open page"
    print("selenium_events.json: OK")


def test_selenium_entries() -> None:
    parser = JSONGenericParser()
    result = parser.parse("examples/selenium_entries.json")
    assert len(result) == 2
    assert result[0].name == "Step 1"
    print("selenium_entries.json: OK")


def test_selenium_har() -> None:
    parser = HarParser()
    result = parser.parse("examples/selenium_har.har")
    assert len(result) == 2
    assert result[0].name == "https://example.com/login"
    print("selenium_har.har: OK")


def test_selenium_broken() -> None:
    parser = JSONGenericParser()
    try:
        parser.parse("examples/broken.json")
        assert False, "Exception expected"
    except ValueError:
        print("broken.json: OK")
