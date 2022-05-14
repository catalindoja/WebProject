Feature: Register Veterinary
In order to keep track of the zoo veterinaries,
As a veterinary,
I want to register a veterinary in the corresponding zoo with its personal details.

 Background: There is a registered user
    Given Exists a user "userProvaAuth" with password "testing4242"
    Given I am on the Django Admin
    Given I create a zoo "Zoo Barcelona"
    Given A zoo "Zoo Barcelona" exists

  Scenario: Register just veterinary name
    Given I login as user "userProvaAuth" with password "testing4242"
    When I register veterinary
    Then I'm viewing the admin page
      | name        |
      | Joan        |
    And There are 1 veterinaries