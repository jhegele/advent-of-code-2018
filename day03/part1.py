# import Python's regular expression library
import re

# create a Claim object. this will represent each "claim" from the puzzle
# inputs.
class Claim(object):

    # class constructor -- this gets run before anything else. here we
    # pass the string (i.e. a single line) from the inputs file and
    # parse it out into its components
    def __init__(self, claim_string):
        # this is a regular expression that I'm using to parse out the
        # components of the claim. regex is a complex (but incredibly)
        # useful topic. tons of info on it online if you search.
        self.regex_pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
        matches = re.search(self.regex_pattern, claim_string)
        # here is where I assign each match group to class properties
        self.id = int(matches.group(1))
        self.start_x = int(matches.group(2))
        self.start_y = int(matches.group(3))
        self.width = int(matches.group(4))
        self.height = int(matches.group(5))
        # in order to quickly determine if an overlap exists, we need
        # to know the top-left and bottom-right coordinates of the
        # claim
        self.tl = (self.start_x + 1, self.start_y + 1)
        self.br = (self.start_x + self.width, self.start_y + self.height)

    # this method creates all squares that this claim populates on
    # the fabric. it uses a tuple of the form (x_coord, y_coord) and
    # stores all of these in a set which is then returned.
    def squares(self):
        sq = set()
        # we use nested loops here to build our series of squares. we
        # know that we need width * height total squares.
        for x in range(0, self.width):
            for y in range(0, self.height):
                # our start x and y values represent the number of 
                # EMPTY cells before the claim starts so we need to 
                # add one here to correct for the fact that the 
                # start x and y values aren't where the claim actually
                # starts.
                sq.add((self.start_x + 1 + x, self.start_y + 1 + y))
        return sq
        
# create a Fabric object. this object will represent the current state
# of our fabric. this primarily gives us an easy way to track what
# squares have been claimed.
class Fabric(object):

    def __init__(self):
        self.claimed_squares = {}

    def add_claim(self, claim):
        # we're only worrying about claimed squares here so the first
        # thing we need to do is to check whether this square has
        # already been claimed or not. if not, we need to add it,
        # otherwise we just add the claim ID to the list of IDs that
        # have claimed the square.
        for square in claim.squares():
            if square not in self.claimed_squares:
                self.claimed_squares[square] = []
            self.claimed_squares[square].append(claim.id)

# import puzzle inputs
with open('./inputs/part1-2.txt') as puzzle_input:
    claims = list(map(Claim, puzzle_input.readlines()))

# initialize the fabric object and add our claims
fabric = Fabric()
for claim in claims:
    fabric.add_claim(claim)

# get any square in our fabric object that has more than one claim against
# it, then print the number of squares that meet that criteria.
overlap_squares = [sq for sq, claims in fabric.claimed_squares.items() if len(claims) > 1]
print(len(overlap_squares))