Feature: Register Visitor
  In order to keep track of the zoo visitors,
  As a visitor,
  I want to register a visitor(myself) in the corresponding zoo with my personal details.

  Background: There is a registered zoo
    Given I log in as an admin
    Given I register a zoo "Zoo Barcelona"

  Scenario: Register a visitor
    When I register a visitor "Test_visitor" assigned to "Zoo Barcelona"
    Then I'm viewing the admin page for the visitors
    And There is 1 visitor called "Test_visitor"