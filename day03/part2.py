# almost all of this is an exact copy of Part 1, comments here reflect any
# differences from Part 1
import re

class Claim(object):

    def __init__(self, claim_string):
        self.regex_pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
        matches = re.search(self.regex_pattern, claim_string)
        self.id = int(matches.group(1))
        self.start_x = int(matches.group(2))
        self.start_y = int(matches.group(3))
        self.width = int(matches.group(4))
        self.height = int(matches.group(5))
        self.tl = (self.start_x + 1, self.start_y + 1)
        self.br = (self.start_x + self.width, self.start_y + self.height)

    def squares(self):
        sq = set()
        for x in range(0, self.width):
            for y in range(0, self.height):
                sq.add((self.start_x + 1 + x, self.start_y + 1 + y))
        return sq
        
class Fabric(object):

    def __init__(self):
        self.claimed_squares = {}

    def add_claim(self, claim):
        for square in claim.squares():
            if square not in self.claimed_squares:
                self.claimed_squares[square] = []
            self.claimed_squares[square].append(claim.id)

    # for part 2, we need to find the single claim that has no overlaps at
    # all. in order to do this we need to find any claim ID that shares at 
    # least one square with another claim ID.
    def overlapped_claim_ids(self):
        claim_ids = set()
        for address, claims in self.claimed_squares.items():
            if len(claims) > 1:
                claim_ids.update(claims)
        return claim_ids

with open('./inputs/part1-2.txt') as puzzle_input:
    claims = list(map(Claim, puzzle_input.readlines()))

fabric = Fabric()
for claim in claims:
    fabric.add_claim(claim)

# build a list of all claim IDs, then get the list of any claim ID that shares
# at least one other square with another claim.
all_claim_ids = [claim.id for claim in claims]
overlapped_claim_ids = fabric.overlapped_claim_ids()

# compare the full list with the list of shared and find the ID that has no
# shared squares
print([claim_id for claim_id in all_claim_ids if claim_id not in overlapped_claim_ids])