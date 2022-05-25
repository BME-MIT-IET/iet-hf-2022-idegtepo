from behave import *
from algorithms.graph.count_connected_number_of_component import *

graph = {}
test_result = 0

use_step_matcher("re")


@given("a one-component connected graph")
def create_one_component_graph(context):
    global graph
    graph = {1: {2, 3, 4}, 2: {1, 3}, 3: {1, 2}, 4: {1}}

@when("connected parts are counted")
def count_connected_parts(context):
    global graph, test_result
    test_result = count_components(graph, len(graph))


@then("the graph is one-component")
def one_component_graph(context):
    global test_result
    assert (test_result, 1)

@given("a three-component connected graph")
def step_impl(context):
    global graph
    graph = {1: {2}, 2: {1}, 3: {4}, 4: {3}, 5: {6}, 6: {5}}

@then("the graph is three-component")
def step_impl(context):
    global test_result
    assert (test_result, 3)