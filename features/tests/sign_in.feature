Feature: SignIn Test

#  Scenario: Logged out user can sign in
#    Given Open Target main page
#    When Click Sign In
#    And From side navigation menu, click Sign In
#    Then Verify Sign into your Target account seen
#
#  Scenario: Authorised user can log in
#    Given Open Target main page
#    When Click Sign In
#    And From side navigation menu, click Sign In
#    And Input email and password on SighIn page
#    And Click Sign In on Sign In page
#    Then Verify user is logged in

Scenario: User can open and close Terms and Conditions from sign in page
 Given Open Target main page
 When Click Sign In
 And From side navigation menu, click Sign In
 And Store original windows
 And Click on Target terms and conditions link
 And Switch to the newly opened window
 Then Verify Terms and Conditions page is opened
 And Close Terms and Conditions page page
 And User can switch back to original