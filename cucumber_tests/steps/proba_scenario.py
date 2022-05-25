from behave import *

use_step_matcher("re")


@given("An unsorted list")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given An unsorted list')


@given("A sorted list")
def fafasf(context):
    raise NotImplementedError(u'STEP: Given A sorted list')


@when("comb sort is performed")
def step_impl(context):
    raise NotImplementedError(u'STEP: When comb sort is performed')


@then("the list is sorted")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the list is sorted')