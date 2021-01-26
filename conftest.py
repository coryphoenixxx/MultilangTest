import  pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose correct language")


@pytest.fixture(scope='function')
def browser(request):
    lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    print(f"\nStart browser with {lang} language...")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nQuit browser...")
    browser.quit()
