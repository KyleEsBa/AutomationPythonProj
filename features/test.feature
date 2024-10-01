Feature: User Login

  Scenario: Successful search on the browser
    Given the user is on the browser page
    When the user search a word
    Then the user is redirected to the results of the search