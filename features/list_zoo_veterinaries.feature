Feature: List Zoo Veterinaries
  In order to know which veterinaries are in a given zoo,
  As an admin,
  I want to list the veterinaries assigned to a zoo.

  Background: There is at least one veterinary assigned to a given zoo
    Given Exists a user "user1" with password "password"
    And Exists zoo with "zoo_id"
    And Exists veterinary with "zoo_id"
      | user   | number_assigned_animals | zoo_id | date       |
      | Joan   | 12                      | 001    | 1998-07-01 |
      | Ricard | 5                       | 003    | 1998-07-02 |
      | Laura  | 42                      | 001    | 1998-07-03 |

  Scenario: List veterinaries in a given zoo
    When I list veterinaries
    Then I'm viewing a list containing
      | user   | number_assigned_animals | zoo_id |
      | Joan   | 12                      | 001    |
      | Ricard | 5                       | 003    |
      | Laura  | 42                      | 001    |
    And The list contains 3 veterinaries

  Scenario: List veterinaries in a given zoo
    Given Exists veterinary registered by "user"
      | user   | number_assigned_animals | zoo_id |
      | Joan   | 12                      | 001    |
      | Ricard | 5                       | 003    |
      | Laura  | 42                      | 001    |
    When I list veterinaries
    Then I'm viewing a list containing
      | user   | number_assigned_animals | zoo_id |
      | Joan   | 12                      | 001    |
      | Ricard | 5                       | 003    |
      | Laura  | 42                      | 001    |
    And The list contains 3 veterinaries

    Scenario: There are no veterinaries in a given zoo
    When I list veterinaries
    Then I'm viewing a list containing
      | user   | number_assigned_animals | zoo_id |
      |        |                         |        |
    And The list contains 0 veterinaries

