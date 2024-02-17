Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify Your cart is empty message seen
    And Verify SignIn btn is clickable on empty cart page
#    And Verify Bullseye empty cart is seen

#  Scenario: Verify product added to cart
#    Given Open target product A-52770446 page
#    When Add product to cart from PP
#    When Click View cart & check out from side navigation
#    Then Verify the Total Price is shown
#
#
#  Scenario: User can add a product to cart
#    Given Open Target main page
#    When Search for candy bags
#    And Click on Add to Cart button
#    And Store product name
#    And Store product price
#    And Confirm Add to Cart button from side navigation
#    And Click View cart & check out from side navigation
#    Then Verify cart has 1 item(s)
#    And Verify cart has correct product name
#    And Verify cart has correct product price
#
#  Scenario: User can add different products to cart
#    Given Open target main page
#    When Search for candy toys
#    And Click on Add to Cart button for product 1
#    And Store product name to a list
#    And Confirm Add to Cart button from side navigation
#    And Close side navigation
#    And Click on Add to Cart button for product 2
#    And Store product name to a list
#    And Confirm Add to Cart button from side navigation
#    And Open cart page
#    Then Verify cart has 2 item(s)
#    And Verify cart has correct multiple products
