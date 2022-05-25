from behave import *

use_step_matcher("re")


@given("a fully connected graph")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a fully connected graph')


@when("strong connection is tested")
def step_impl(context):
    raise NotImplementedError(u'STEP: When strong connection is tested')


@then("the graph is strongly connected")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the graph is strongly connected')


@then("the graph is not strongly connected")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the graph is not strongly connected')