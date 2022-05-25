from behave import *
from algorithms.graph.check_digraph_strongly_connected import *

graph = Graph
test_result = False

use_step_matcher("re")


# mindket iranyba hozza kell adni
@given("a fully connected graph")
def create_fully_connected_graph(context):
    global graph
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(0, 4)
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 0)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 0)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)


@given("a rarely connected graph")
def create_rarely_connected_graph(context):
    global graph
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    graph.add_edge(4, 3)


@when("strong connection is tested")
def test_strong_connection(context):
    global graph, test_result
    test_result = graph.is_strongly_connected()


@then("the graph is strongly connected")
def check_result_true(context):
    global test_result
    assert (test_result, True)


@then("the graph is not strongly connected")
def check_result_false(context):
    global test_result
    assert (test_result, False)
