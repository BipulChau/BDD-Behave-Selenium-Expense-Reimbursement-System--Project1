Feature: Action - approve/deny
  Scenario: Check Finance Manager can approve, deny reimbursement
    Given The finance manager is logged in, clicked Check Reimbursement Details and filter status as pending
    When clicks approve
    And clicks deny
    Then  That particular reimbursement should disappear from pending status
