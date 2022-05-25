Feature: Bipartite graph test

  Scenario: Graph is bipartite
    Given a bipartite graph
    When bipartite is tested
    Then the graph is bipartite

  Scenario: Graph is not bipartite
    Given a non-bipartite graph
    When bipartite is tested
    Then the graph is non-bipartite