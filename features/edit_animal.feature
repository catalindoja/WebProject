Feature: Edit Animal
  In order to modify the attributes of an animal registry,
  As a veterinary,
  I want to edit the animal register I created.

  Background: There is a zoo, a veterinary and a staff, assigned to an animal
    Given I log in as an admin
    Given I register a zoo "Zoo Barcelona"
    Given I register a veterinary "Test_vet" assigned to "Zoo Barcelona"
    Given I register a veterinary "Test_staff" assigned to "Zoo Barcelona"
    Given I login as user "Test_vet" with password "prova1234@"
    Given I create an animal "Test_animal" assigned to the zoo "Zoo Barcelona", the veterinary "Test_vet" and the staff "Test_staff"


 Scenario: Edit animal for the current veterinary
    When I edit the animal "Test_animal" to rename it to "Test_edited_animal"
    When I visit the veterinary animal editor page for "Test_vet"
    Then There is 1 animal "Test_edited_animal" 
    And There's no animal "Test_animal"