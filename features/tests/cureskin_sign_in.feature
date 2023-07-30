# Created by stephenokonkwo at 7/27/23
Feature: cureskin sign in page test cases

  @mobile
  Scenario: User Sign in page is displayed
    Given Open Main page
    When Tap Hamburger BTN
    When Tap on user BTN
    Then Verify User sign in page appears
