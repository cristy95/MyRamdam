from lettuce import step
from nose.tools import *


@step(u'Given that an item has a feeling "([^"]*)"')
def given_that_an_item_has_a_feeling_group1(step, feeling):
    feel = Feel(feeling)
    assert_equal(feel.feeling, feeling)

@step(u'When the user wants to see the rating')
def when_the_user_wants_to_see_the_rating(step):
    feel = Feel(feeling)
    var = feel.feeling is feeling
    assert_equal(var, True)

@step(u'Then the program will view the rating')
def then_the_program_will_view_the_rating(step):
    feel = Feel(feel_rate)
    print 'Feel Rate is', feel.get_feel_rate()

@step(u'Given that an item has no feeling "([^"]*)"')
def given_that_an_item_has_no_feeling_group1(step, group1):
    feel = Feel(feeling)
    assert_equal(len(feel.feelings), 0)

@step(u'Then the program will alert the user that it has no rating yet')
def then_the_program_will_alert_the_user_that_it_has_no_rating_yet(step):
	print 'Data item not yet rated'
