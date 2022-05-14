Feature: Register Zoo
In order to keep track of the existing zoo's,
As an admin,
I want to register a zoo with its details.

 Background: There is an admin user
    Given Exists a user "admin" with password "admin"
    Given I am on the Django Admin

  Scenario: Register just veterinary name
    Given I login as user "admin" with password "admin"
    When I register veterinary
      | username        |
      | Joan        |
      | id_password1        |
      | 1234        |
      | id_password2        |
      | 1234        |
      | id_name        |
      | Joan        |
      | id_age        |
      | 10        |
      | id_address        |
      | Hola        |
      | id_postalcode        |
      | 25600        |
      | id_zoo_id        |
      | 1        |
      | id_number_assigned_animals        |
      | 10        |
    Then I'm viewing the admin page
      | name        |
      | Joan        |
    And There are 1 veterinaries