import random

def lottery(ball_count=10, max_ball_number=50, min_ball_number=1):
    return sorted(random.sample(range(min_ball_number, max_ball_number), ball_count))
    #test for len
    #change the ball_count to greater or less than 10
    #test for min
    #change the min_ball_number
    #test for max
    #change the max_ball_number
    #return sorted([random.randint(1,50) for x in xrange(ball_count)])
    #test for duplicates
    #return sorted([random.randint(1,50) for x in xrange(ball_count)])

game = lottery()
print game


#unitests
# we should test the list for it's length, should be 10 balls
assert len(game) == 10, "Length of the list should be 10, length is: {}"
# we should test the list for min==1 and max==50
assert min(game) >= 1 , "min of the list should not be less than 1"
assert max(game) <= 50 , "max of the list should not be greater than 50"
# we should test the list for uniqueness
def is_unique(l):
    return len(l) == len(set(l))
assert is_unique(game) is True , "the list should be unique, no duplicates"
