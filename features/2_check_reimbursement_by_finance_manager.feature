Feature: check_reimbursement
  Scenario: check reimbursement of employees by finance manager
    Given Finance Manager is successfully logged-in and is inside the application
    When Clicks Check Reimbursement Details
    Then Should be able to see Reimbursement details of all the employees