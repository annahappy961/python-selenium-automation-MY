Feature: Tests for Target Help page UI

  Scenario: Verify all elements are shown
    Given Open Target Help page
    Then Verify Target Help text is shown
    And Verify Search Help field is shown
    And Verify Search btn is shown
    And Verify What would you like to do? text is shown
    And Verify Browse all Help pages is shown
    And Verify 'What would you...' 7 elements are shown
    And Verify Contact Us and Product Recalls 2 elements are shown
    And Verify 'Browse all Help pages' 17 elements are shown
