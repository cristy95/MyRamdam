Feature: Feeling reports for an item

        As a user, I want to see the log af all the feelings that I made

        Scenario: Feeling reports daily
        Given that I have put feeling to an item with in a day
        When I want to see the reports
        Then the program will view the past feeling that I have.

        Scenario: Feeling reports daily with no feeling
        Given that I did not put feeling yesterday
        When I want to see the reports
        Then the program will say that: You dont put feeling yesterday

        Scenario: Feeling reports weekly
        Given that I have put feeling to an a item with in a week
        When I want to see the reports
        Then the program will view the past feeling that I have with in a week

        Scenario: Feeling reports weekly with no feeling
        Given that I did not put feeling with in a week
        When I want to see the reports
        Then the program will say that: You dont put feeling in a week

        Scenario: Feeling reports monthly
        Given that I have put feeling to an a item with in a month
        When I want to see the reports
        Then the program will view the past feeling that I have with in a monthly

        Scenario: Feeling reports monthly with no feeling
        Given that I did not put feeling with in a month
        When I want to see the reports
        Then the program will say that: You dont put feeling in a month