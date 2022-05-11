Feature: List Veterinary Animals
  In order to see the animals assigned to a given veterinary and their information,
  As a veterinary,
  I want to list my assigned animals.

  Background: There is at least one animal assigned to the same user
    Given Exists a user "user1" with password "password"
    And Exists animal registered by "user1"
      | animal_id  | name                  | zoo_id  | staff_id | veterinary_id | date       |
      | 001        | Mara the Meerkat      | 001     | 001      | 001           | 1998-07-01 |
      | 004        | Donald the Duck       | 001     | 003      | 001           | 1998-07-02 |
      | 015        | Jojo the Jaguar       | 001     | 005      | 001           | 1998-07-03 |
      | 016        | Armando the Armadillo | 001     | 001      | 001           | 1998-07-04 |
      | 017        | Bono the Bonobo       | 001     | 005      | 001           | 1998-07-05 |
      | 052        | All the Alligator     | 001     | 005      | 001           | 1998-07-06 |

  Scenario: List animals assigned to "user1"
    Given Exists animal assigned to "user1"
      | animal_id  | name                  | zoo_id  | staff_id | veterinary_id | date       |
      | 001        | Mara the Meerkat      | 001     | 001      | 001           | 1998-07-01 |
      | 004        | Donald the Duck       | 001     | 003      | 001           | 1998-07-02 |
      | 015        | Jojo the Jaguar       | 001     | 005      | 001           | 1998-07-03 |
      | 016        | Armando the Armadillo | 001     | 001      | 001           | 1998-07-04 |
      | 017        | Bono the Bonobo       | 001     | 005      | 001           | 1998-07-05 |
      | 052        | All the Alligator     | 001     | 005      | 001           | 1998-07-06 |
    When I list animals
    Then I'm viewing a list containing
      | animal_id  | name                  | zoo_id  | staff_id | veterinary_id |
      | 001        | Mara the Meerkat      | 001     | 001      | 001           |
      | 004        | Donald the Duck       | 001     | 003      | 001           |
      | 015        | Jojo the Jaguar       | 001     | 005      | 001           |
      | 016        | Armando the Armadillo | 001     | 001      | 001           |
      | 017        | Bono the Bonobo       | 001     | 005      | 001           |
      | 052        | All the Alligator     | 001     | 005      | 001           |
    And The list contains all animals assigned to "user1"

  Scenario: There are no animals assigned to "user1"
    When I list animals
    Then I'm viewing a list containing
      | animal_id  | name                  | zoo_id  | staff_id | veterinary_id |
      |            |                       |         |          |               |
    And The list contains 0 animals