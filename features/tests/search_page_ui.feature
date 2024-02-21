Feature: Test for Search page UI

  Scenario: Verify that user can see product title and product image
    Given Open Target main page
    When Search for candy toy
    Then Verify that every product has a title and an image
    