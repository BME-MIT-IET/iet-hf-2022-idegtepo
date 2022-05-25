from behave import *
from algorithms.graph.check_bipartite import *

graph = {}
test_result = False

use_step_matcher("re")

#k3,3
@given("a bipartite graph")
def create_bipartite(context):
    global graph
    graph = {1: {4, 5, 6}, 2: {4, 5, 6}, 3: {4, 5, 6}, 4: {1, 2, 3}, 5: {1, 2, 3}, 6: {1, 2, 3}}



@when("bipartite is tested")
def check_bipartite_test(context):
    global graph, test_result
    result = check_bipartite(graph)


@then("the graph is bipartite")
def result_true(context):
    global test_result
    assert (test_result, True)


@given("a non-bipartite graph")
def create_non_bipartite(context):
    global graph
    graph = {1: {2, 3}, 2: {1, 2}, 3: {1, 2}}



@then("the graph is non-bipartite")
def result_false(context):
    global test_result
    assert (test_result, False)
