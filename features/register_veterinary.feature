Feature: Register Veterinary
  In order to keep track of the zoo veterinaries,
  As a admin,
  I want to register a veterinary in the corresponding zoo with its personal details.

 Background: There is a registered admin and a zoo
    Given I log in as an admin
    Given I register a zoo "Zoo Barcelona"

  Scenario: Register a veterinary
    When I register a veterinary "Test_vet" assigned to "Zoo Barcelona"
    Then I'm viewing the admin page for the veterinaries
    And There is 1 veterinary called "Test_vet"