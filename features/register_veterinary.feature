Feature: Register Veterinary
In order to keep track of the zoo veterinaries,
As a veterinary,
I want to register a veterinary in the corresponding zoo with its personal details.

 Background: There is a registered admin and a zoo
    Given I log in as an admin
    Given I create a zoo "Zoo Barcelona"
    Then Exists a zoo "Zoo Barcelona"

  Scenario: Register just veterinary name
    When I register veterinary assigned to "Zoo Barcelona"
    Then I'm viewing the admin page
    And There is 1 veterinary called "Test_guy"