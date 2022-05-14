Feature: Register Visitor
  In order to keep track of the zoo visitors,
  As a staff,
  I want to register a visitor in the corresponding zoo with its personal details.

  Background: There is a registered staff and a zoo
    Given I log in as an admin
    Given I register a zoo "Zoo Barcelona"
    Then Exists a zoo "Zoo Barcelona"

  Scenario: Register a visitor
    When I register a visitor "Test_guy" assigned to "Zoo Barcelona"
    Then I'm viewing the admin page
    And There is 1 visitor called "Test_guy"