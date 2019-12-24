import pytest
import allure
from allure_commons.types import AttachmentType
import time
from Driver.driver import Driver
from Data.test_data import Config
from utilities.testFrame import InitPages


@pytest.fixture(scope='function')
def get_driver(request):
    driver = Driver(Config.BROWSER).set_browser()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Config.HOME_URL)
    yield driver
    driver.close()
    driver.quit()
    

@pytest.fixture(scope='function')
def app(get_driver):
    page_init = InitPages(get_driver)
    return page_init


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # will execute even before the tryfirst one above!
    # do nothing here intentionally
    outcome = yield
    # will execute after all non-hookwrappers executed
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    # we only look at actual failing test calls, not setup/teardown
    # https://docs.pytest.org/en/latest/example/simple.html#post-process-test-reports-failures


@pytest.fixture()
def screenshot_on_failure(request, get_driver):

    yield

    if request.node.rep_setup.failed: # if rep.when == "call" and rep.failed:
        print("setting up a test failed!", request.node.nodeid)
        allure.attach(get_driver.get_screenshot_as_png(),
                      name=request.function.__name__,
                      # name='Screenshot',
                      attachment_type=AttachmentType.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            print("executing test failed", request.node.nodeid)
            allure.attach(get_driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=AttachmentType.PNG)
