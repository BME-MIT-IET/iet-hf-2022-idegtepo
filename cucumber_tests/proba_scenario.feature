Feature: Sorting a list using comb sort.

  Scenario: The array is already sorted
    Given A sorted list
    When comb sort is performed
    Then the list is sorted

  Scenario: The array is not sorted
    Given An unsorted list
    When comb sort is performed
    Then the list is sorted

  Scenario: The array is not sorted
    Given An unsorted list
    When comb sort is performed
    Then the list is sorted