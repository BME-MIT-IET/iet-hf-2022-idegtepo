from behave import *
from algorithms.graph.check_bipartite import *

graph = {}
test_result = False

use_step_matcher("re")

#k3,3
@given("a bipartite graph")
def create_bipartite(context):
    global graph
    graph = {0: [0, 0, 0, 1, 1, 1], 1: [0, 0, 0, 1, 1, 1], 2: [0, 0, 0, 1, 1, 1], 3: [1, 1, 1, 0, 0, 0], 4: [1, 1, 1, 0, 0, 0], 5: [1, 1, 1, 0, 0, 0]}



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
    graph = {0: [0, 1, 0, 1, 1, 1], 1: [0, 0, 0, 1, 1, 1], 2: [0, 0, 0, 1, 1, 1], 3: [1, 1, 1, 0, 0, 0], 4: [1, 1, 1, 0, 0, 0], 5: [1, 1, 1, 0, 0, 0]}



@then("the graph is non-bipartite")
def result_false(context):
    global test_result
    assert (test_result, False)
