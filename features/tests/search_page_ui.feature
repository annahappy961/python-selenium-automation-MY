Feature: Test for Search page UI

  Scenario: Verify each product has an image amd a name
    Given Open Target main page
    When Search for candy
    Then Verify 29 images in shown
    And Verify 29 names in shown
