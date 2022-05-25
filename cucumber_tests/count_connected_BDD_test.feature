
Feature: Count connected parts tests

  Scenario: Graph constits of one component
    Given a one-component connected graph
    When connected parts are counted
    Then the graph is one-component

  Scenario: Graph constits of three component
    Given a three-component connected graph
    When connected parts are counted
    Then the graph is three-component