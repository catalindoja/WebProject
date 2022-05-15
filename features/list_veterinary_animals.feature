Feature: List Veterinary Animals
  In order to see the animals assigned to a given veterinary and their information,
  As a veterinary,
  I want to list my assigned animals.

  Background: There is a zoo, a veterinary and a staff, assigned to an animal
    Given I log in as an admin
    Given I register a zoo "Zoo Barcelona"
    Given I register a veterinary "Test_vet" assigned to "Zoo Barcelona"
    Given I register a veterinary "Test_staff" assigned to "Zoo Barcelona"
    Given I login as user "Test_vet" with password "prova1234@"
    Given I create an animal "Test_animal" assigned to the zoo "Zoo Barcelona", the veterinary "Test_vet" and the staff "Test_staff"
    Given I create an animal "Test_animal_2" assigned to the zoo "Zoo Barcelona", the veterinary "Test_vet" and the staff "Test_staff"


 Scenario: List animals for the current veterinary
    When I visit the veterinary animal editor page for "Test_vet"
    Then There is a list with the "Test_animal" that the veterinary "Test_vet" created
    And There is a list with the "Test_animal_2" that the veterinary "Test_vet" created
