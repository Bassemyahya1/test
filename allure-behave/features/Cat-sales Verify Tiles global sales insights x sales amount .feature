Feature: Validate Categories sales Analysis Dashboard tiles loading
Background:
   Given the user is on the preproduction environment page
    When  he enters the suppliers credentials
    When  he is logged in successfully
    And   he is on the Categories sales Analysis Dashboard
    Then  he verifies that he is on the correct page

  Scenario Outline: As a user  i will verify that Categories Tiles global sales insights x sales amount are well desplayed
    When the user set the filters "<country>" hn "<number>"
    Then Tiles promotion sales insights x sales amount are well displayed
    Examples:
    |country|number|
    |Belgium|2|
    |FRANCE |1|
    |Taiwan|3 |

