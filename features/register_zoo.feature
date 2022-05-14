Feature: Register Zoo
  In order to keep track of the existing zoos,
  As an admin,
  I want to register a zoo with its details.

  Background: There is an admin user
    Given I log in as an admin

  Scenario: Register a zoo
    Given I login as  an admin
    When I register a zoo "Zoo Barcelona"
    Then I'm viewing the admin page
    And There is 1 zoo called "Zoo Barcelona"