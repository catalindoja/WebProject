Feature: Delete Animal
  In order to delete an animal from a zoo when it dies or is transfered to another zoo outside our database,
  As a veterinary,
  I want to remove the animal register I created from the database.


  Background: There is a zoo, a veterinary and a staff, assigned to an animal
    Given I log in as an admin
    Given I register a zoo "Zoo Barcelona"
    Given I register a veterinary "Test_vet" assigned to "Zoo Barcelona"
    Given I register a veterinary "Test_staff" assigned to "Zoo Barcelona"
    Given I login as user "Test_vet" with password "prova1234@"
    Given I create an animal "Test_animal" assigned to the zoo "Zoo Barcelona", the veterinary "Test_vet" and the staff "Test_staff"


 Scenario: List animals for the current veterinary
    When I visit the veterinary animal editor page for "Test_vet"
    When I delete the animal "Test_animal"
    When I visit the veterinary animal editor page for "Test_vet"
    Then There's no animal "Test_animal"
 