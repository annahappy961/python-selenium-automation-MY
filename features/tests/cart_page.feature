Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify Your cart is empty message is shown
    And Verify SignIn btn is clickable on empty cart page
    And Verify Bullseye empty cart is seen

  Scenario: Verify product added to cart
    Given Open Target Product page
    When Add product to cart from PP
    When Click View cart & check out from side navigation menu
    Then Verify the Total Price is shown
