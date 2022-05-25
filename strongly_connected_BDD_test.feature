Feature: Strongly connected graph test

  Scenario: Graph is fully connected
    Given a fully connected graph
    When strong connection is tested
    Then the graph is strongly connected

  Scenario: graph is a one way circle
    Given a rarely connected graph
    When strong connection is tested
    Then the graph is not strongly connected