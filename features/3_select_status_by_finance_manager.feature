Feature: Filter reimbursement by finance manager
  Scenario: Filter reimbursements based on status
    Given Finance Manager has successfully logged in and clicked check reimbursement details
    When select status as pending, approved and denied
    Then Reimbursements should filter as pending, approved and denied