Feature: my.Randam application to be able to add customized feeling

	As a user, I want to customize my own feeling so that I could clearly express what I feel.

	Scenario: Add customized feeling
	Given I add feeling "incomplete"
	And I choose "sad" as the feeling it is leaning towards
	When I click the submit/post button
	Then I could see post "feeling incomplete"

	Scenario: Failed to choose the main feeling
	Given I add feeling "confused"
	And I do not choose a feeling it is leaning towards
	#When I click the submit/post button
	Then the submit/post button is disabled

	Scenario: Session has expired
	Given I add feeling "wehee"
	And I choose "happy" as the feeling it is leaning towards
	And my session has already expired
	#When I click the submit/post button
	Then I could see alert "Your session has already expired"
	And I would have to verify back my identity

	Scenario: Added customized feeling has exceeded 50 characters
	Given I add feeling "ambotnalanganiuihuhuhuhuthereisnousecryingoverspoiledmilk"
	And I choose "sad" as the feeling it is leaning towards
	When I click the submit/post button
	Then I could see alert "Your added feeling is very long"

