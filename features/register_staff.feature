Feature: Register Staff
In order to keep track of the zoo staffs,
As an admin,
I want to register a staff in the corresponding zoo with its personal details.

 Background: There is a registered admin and a zoo
    Given I log in as an admin
    Given I register a zoo "Zoo Barcelona"

  Scenario: Register a staff
    When I register a veterinary "Test_staff" assigned to "Zoo Barcelona"
    Then I'm viewing the admin page for the staffs
    And There is 1 staff called "Test_staff"