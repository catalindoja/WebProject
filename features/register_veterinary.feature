Feature: Register Veterinary
In order to keep track of the zoo veterinaries,
As an admin or veterinary?,
I want to register a veterinary in the corresponding zoo with its personal details.

 Background: There is a registered user
    Given Exists a user "admin" with password "admin"

  Scenario: Register just veterinary name
    Given I login as user "admin" with password "admin"
    When I register veterinary
      | name        |
      | Joan        |
    Then I'm viewing the details page for restaurant by "user"
      | name        |
      | Joan        |
    And There are 1 veterinaries