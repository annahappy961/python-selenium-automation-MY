## Created by annag at 2/4/2024
#Feature: Target.com test
#
#
#  Scenario: Appropriate msg is shown for empty cart
#    Given Open Target main page
#    When Click on Cart icon
#    Then Verify 'Your cart is empty' message is shown
#    Then Verify Sing In clickable
#
#  Scenario: Verify logged out user can access Sign In
#    Given Open Target main page
#    When Click Sign In
#    When Click Sign In from right side navigation menu
#    Then Verify 'Sign into your Target account' text seen
#    Then Verify Sing In clickable
#
#    Scenario: Add a product to cart
#      Given Open product page
#      When Add product to cart
#      When Click View cart & check out from side navigation menu
#      Then Verify the total price is seen in cart


#Feature: Test Scenarios for Search functionality
#
#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Car into search field
#    And Click on search icon
#    Then Product results for Car are shown