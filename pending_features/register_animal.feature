Feature: Register Animal
  In order to keep track of the zoo animals,
  As a veterinary,
  I want to register an animal to a given zoo with its attributes and its associated veterinary.

  Background: There is a zoo and a veterinary to which the animal will be assigned
    Given Exists a user "user1" with password "password"
    And Exists zoo registered by "user1"
      | zoo_id | name         | description                           | max_visitors | address     | postal code|
      | 001    | UdL          | Where the fauna studies               | 500          | Lleida      | 25001      |
      | 002    | Cincinnati   | Harambe will forever be in our hearts | 10000        | Cincinnati  | 30002      |
      | 003    | Eigersstor   | Home to animals and fae alike         | 23192        | Sword Coast | 00003      |

  Scenario: Register new animal
    Given I login as user "user1" with password "password"
    When  I register a new animal at the zoo "UdL"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
      | 001        | Mara the Meerkat | 001     | 001      | 001           |
    Then I'm viewing the details page for the animal at zoo "001" by "user1"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
      | 001        | Mara the Meerkat | 001     | 001      | 001           |
    And There is 1 animal

  Scenario: Try to register an animal but not logged in
    Given I'm not logged in
    When I register an animal at the zoo "001"
      | animal_id  | name             | zoo_id  | staff_id | veterinary_id |
      | 001        | Mara the Meerkat | 001     | 001      | 001           |
    Then I'm redirected to the login form
    And There are 0 animals