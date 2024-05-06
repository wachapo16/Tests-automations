@regression_tests

Feature: Validate element created dropdown column

  Scenario: Navigate to the Kayak home page and validate principal elements
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    Then The page "should" contain the next elements
      | name                   | type   |
      | logo                   | input  |
      | title                  | text   |
      | login                  | button |
      | favorite               | button |

  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    Then The url page should be equal to the next "https://www.kayak.com.co/" url

    Scenario Outline: Navigate between countries and validate the URL
      Given I navigate to the kayak main page
      Then I should be in the "home" page
      When I navigate to the "<url>" URL
      Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.br/ |
      | https://www.kayak.com.pr/ |
      

    Scenario Outline: Navigate between menu_option and validate the URL
      Given I navigate to the kayak main page
      Then I should be in the "home" page
      When I click on the "<MenuOption>" "<element_type>"
      Then The URL of the page should match the expected "<URL>"

    Examples:
      | MenuOption     | element_type | URL                                  |
      | Flights        | button       | https://www.kayak.com.co/flights     |
      | Stays          | button       | https://www.kayak.com.co/stays       |
      | Cars           | button       | https://www.kayak.com.co/cars        |
      | Citybreaks     | button       | https://www.kayak.com.co/citybreaks  |  


    
