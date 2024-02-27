Feature: Circle page test
#
#  Scenario: Verify Benefit's you'll love Cards are shown
#    Given Open Target Circle page
#    Then Verify 5 benefit cards are shown
#    And  Verify that clicking through Circle tabs works

  Scenario: User is able to navigate to Google Play Target page
    Given Open Target Circle page
    And Store original window
    When Click Google Play button
    And Switch to new window
    Then Verify Google Play Target page opened
    And Close current page
    And Return to original window
