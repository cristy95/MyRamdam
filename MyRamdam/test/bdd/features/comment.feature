Feature: Application that allows the user to comment to the Professor and Classmate data items

		 As a user, I want to be able to comment to a Professor or a Classmate
		 and choose to be anonymous
		 and edit my comment
		 and delete my comment

Scenario: Add a comment
		  Given the data item exists
		  And I visit the profile of the data item
		  When I enter my comment "Lorem ipsum dolor sit amet"
		  Then the comment and user id is recorded
		  And the comment is shown in the profile of the data item with the identity of the user

Scenario: Add a comment anonymously
		  Given the data item exists
		  And I visit the profile of the data item
		  When I enter my comment "Lorem ipsum dolor sit amet"
		  And I check the option for "Anonymous"
		  Then the comment is recorded
		  But the user id of the comment is not recorded
		  And the comment is shown in the profile of the data item without an identity

Scenario: Edit a comment
		  Given the comment already exists
		  And I visit the comment section in the profile of the data item
		  When I click the button for "Edit"
		  Then an edit comment section field is shown
		  And I edit my comment
		  And I saved it
		  And the edited comment is recorded
		  And the edited comment is shown in the profile of the data item 

Scenario: Delete a comment
		  Given the comment already exists
		  And I visit the comment section in the profile of the data item
		  When I click the button for "Delete"
		  Then an alert for "Confirm" or "Cancel" is shown
		  And I click "Confirm"
		  And the comment is deleted from the record
		  And the comment disappears in the the profile of the data item
