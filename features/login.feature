Feature: ERS log in
  Scenario: User logg in
    Given Employee is in the log in page
    When  Input correct username
    And correct password
    Then redirect to logged in page