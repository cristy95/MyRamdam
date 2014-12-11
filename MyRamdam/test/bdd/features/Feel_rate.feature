Feature: Feel Rate of an item

        As a user, I want to see the rate for an item

        Scenario: Feel rate
        Given that an item has a feeling
        When the user want to see the rating
        Then the program will view the rating

        Scenario: feel rate without added feeling/s
        Given that an item has a no feeling
        When the user want to see the rating
        Then the program will allert the user that it has no rating yet
