# -*- coding: utf-8 -*-
import importlib
import json
import jsonpickle
import os.path
import pytest
from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        conf = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(conf) as f:
            target = json.load(f)
    return target



@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_conf = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseurl=web_conf['baseurl'])
    fixture.session.ensure_login(username=web_conf['username'], password=web_conf['password'])
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


@pytest.fixture(scope="session")
def db(request):
    db_conf = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_conf["host"], name=db_conf["name"], user=db_conf["user"], password=db_conf["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.{}".format(module)).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/{}.json".format(file))) as f:
        return jsonpickle.decode(f.read())
