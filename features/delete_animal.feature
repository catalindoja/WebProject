Feature: Delete Animal
  In order to delete an animal form a zoo when it dies or is transfered to another zoo,
  As a veterinary,
  I want to remove the animal register I created from the database.

  Background: There are registered users and animals assigned to a veterinary
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists animal registered by "user1"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id | date       |
      | 001        | Mara the Meerkat | 001     | 001      | 001           | 1998-07-01 |

  Scenario: Delete deceased animal
    Given I login as user "user1" with password "password
    When  I view the details for animal "Mara the Meerkat"
    And I edit the current animal
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
      |            |                  |         |          |               |
    Then I'm viewing the details page for animal at zoo "001" by "user1"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
      |            |                  |         |          |               |
    And There are 0 animals

  Scenario: Try to delete animal but not logged in
    Given I'm not logged in
    When I view the detail for animal "Mara the Meerkat"
    Then There is no "delete" link avaliable

  Scenario: Try to edit animal but not assigned to you
    Given I login as "user2" with password "password"
    When I view the details for animal "Mara the Meerkat"
    Then There is no "delete" link available