Feature: Amazon Search tests

  Scenario: User can search for table on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"

  Scenario: User can search for coffee on Amazon
    Given Open amazon main page
    When Search for coffee
    Then Verify search results shown for "coffee"

  Scenario Outline outline: User can search on Amazon
    Given Open amazon main page
    When Search for <search_word>
    Then Verify search results shown for <search_result>
    Examples:
      | search_word | search_result |
      | table       | "table"       |
      | coffe       | "coffee"      |
      | mug         | "mug"         |
      | dress       | "dress"       |


  Scenario: User can search for kindle on Amazon
    Given Open amazon main page
    When Search for kindle
    When Click on kindle item
    When Click add to cart
    When Go to the Cart Page
    Then Verify the cart has the right product

  Scenario: Verify that User can search in a department
    Given Open amazon main page
    When Select department books
    When Search for Faust
    Then Verify correct department shown

