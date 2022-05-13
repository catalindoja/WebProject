Feature: Edit Animal
In order to modify the attributes of an animal registry,
As an admin or veterinary,
I want to edit the animal register I created.

  Background: There are registered users and animals assigned to a veterinary
    Given Exists a user "user1" with password "password"
      #User is vet or admin
    And Exists a user "user2" with password "password"
      #User is vet
    And Exists user "user3" with password "password"
      #User is not vet or admin
    And Exists animal registered by "user1"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
      | 001        | Mara the Meerkat | 001     | 001      | 001           |

  Scenario: Transfer animal to another zoo
    Given I login as user "user1" with password "password
    When  I view the details for animal "Mara the Meerkat"
    And I edit the current animal
      | zoo_id | staff_ id | veterinary_id |
      | 002    |           |               |
    Then I'm viewing the details page for animal at zoo "001" by "user1"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
    And There are 0 animals

  Scenario: Change assigned veterinary
    Given I login as user "user1" with password "password
    When  I view the details for animal "Mara the Meerkat"
    And I edit the current animal
      | veterinary_id |
      | 002           |
    Then I'm viewing the details page for animal at zoo "001" by "user1"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
      | 001        | Mara the Meerkat | 001     | 001      | 002           |
    And There is 1 animal

  Scenario: Change assigned staff
    Given I login as user "user1" with password "password
    When  I view the details for animal "Mara the Meerkat"
    And I edit the current animal
      | staff_id |
      | 002      |
    Then I'm viewing the details page for animal at zoo "001" by "user1"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
      | 001        | Mara the Meerkat | 001     | 002      | 001           |
    And There is 1 animal

  Scenario: Try to edit animal but not logged in
    Given I'm not logged in
    When I view the detail for animal "Mara the Meerkat"
    Then There is no "edit" link avaliable

  Scenario: Try to edit animal but not assigned to you or not admin
    Given login as "user3" with password "password"
    When I view the details for animal "Mara the Meerkat"
    Then There is no "edit" link available