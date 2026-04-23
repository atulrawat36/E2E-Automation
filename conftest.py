import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<p><strong>Project:</strong> SauceDemo QA Automation</p>",
        "<p><strong>Tester:</strong> Atul Rawat</p>"
    ])