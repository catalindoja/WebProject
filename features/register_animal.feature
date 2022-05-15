Feature: Register Animal
  In order to keep track of the zoo animals,
  As a veterinary,
  I want to register an animal to a given zoo with its attributes and its associated veterinary and staff.

  Background: There is a zoo, a veterinary and a staff to which the animal will be assigned
    Given I log in as an admin
    Given I register a zoo "Zoo Barcelona"
    Given I register a veterinary "Test_vet" assigned to "Zoo Barcelona"
    Given I register a veterinary "Test_staff" assigned to "Zoo Barcelona"

  Scenario: Register new animal logged in as a veterinary (manually)
    Given I login as user "Test_vet" with password "prova1234@"
    When I create an animal "Test_animal" assigned to the zoo "Zoo Barcelona", the veterinary "Test_vet" and the staff "Test_staff"
    Then I'm viewing the admin page for the animals
    Then There is 1 animal called "Test_animal"

  Scenario: Register new animal logged in as a veterinary (using the api)
    Given I login as user "Test_vet" with password "prova1234@"
    When I create an animal using the api assigned to the zoo "Zoo Barcelona", the veterinary "Test_vet" and the staff "Test_staff"
    Then I'm viewing the admin page for the animals
    Then There is 1 animal
  
  Scenario: Try to register an animal without being logged in as a veterinary
    Given I login as user "Test_staff" with password "prova1234@"
    When I try to access the create animal page
    Then I get redirected to log in as a veterinary

