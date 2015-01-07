from lettuce import step
from nose.tools import *


@step(u'Given that I have put feeling to an item with in a day')
def given_that_i_have_put_feeling_to_an_item_with_in_a_day(step):
    dailyLog = day(1)
    happy = happy(1)
    sad = sad(0)
    angry = angry(0)
    surprised = surprised(0)


@step(u'When I want to see the reports')
def when_i_want_to_see_the_reports(step):
    assert False

@step(u'Then the program will view the past feeling that I have.')
def then_the_program_will_view_the_past_feeling_that_i_have(step):
    dailyLog = day()
    happy = happy(1)
    
   
@step(u'Given that I did not put feeling yesterday')
def given_that_i_did_not_put_feeling_yesterday(step):
    assert False


@step(u'Then the program will say that: You dont put feeling yesterday')
def then_the_program_will_say_that_you_dont_put_feeling_yesterday(step):
    assert False

@step(u'Given that I have put feeling to an a item with in a week')
def given_that_i_have_put_feeling_to_an_a_item_with_in_a_week(step):
    weeklyLog = week(1)

@step(u'Then the program will view the past feeling that I have with in a week')
def then_the_program_will_view_the_past_feeling_that_i_have_with_in_a_week(step):
    assert False

@step(u'Given that I did not put feeling with in a week')
def given_that_i_did_not_put_feeling_with_in_a_week(step):
    assert False

@step(u'Given that I have put feeling to an a item with in a month')
def given_that_i_have_put_feeling_to_an_a_item_with_in_a_month(step):
    assert False

@step(u'Then the program will view the past feeling that I have with in a monthly')
def then_the_program_will_view_the_past_feeling_that_i_have_with_in_a_monthly(step):
    assert False

@step(u'Given that I did not put feeling with in a month')
def given_that_i_did_not_put_feeling_with_in_a_month(step):
    assert False

@step(u'Then the program will say that: You dont put feeling in a week')
def then_the_program_will_say_that_you_dont_put_feeling_in_a_week(step):
    assert True

@step(u'Then the program will say that: You dont put feeling in a month')
def then_the_program_will_say_that_you_don_t_put_feeling_in_a_month(step):
    assert True
