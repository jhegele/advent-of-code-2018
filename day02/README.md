# Day 2 Solutions Overview

## Part 1

One interesting thing about Python is that it treats any string as a list of characters. So, you can do stuff like this:

```python
my_string_var = 'abcde'
my_string_var[0] # would produce 'a'
my_string_var[3] # would produce 'd'
```

So, since we know that Python looks at a string like a list of characters, we can correctly jump to the conclusion that, for Part 1, what we need to do is count the occurrences of elements within a list. Luckily, Python has a built-in helper for just that! We can use `Counter()` from the `collections` library to help us here.

For my Part 1 solution, pretty much all of the logic exists in a single line:

```python
likely_ids = list(map(lambda x: set([v for k, v in Counter(x).items() if v in [2, 3]]), box_ids))
```

Let's break this down from the inside out so that it's easier to see what's going on. The inner-most element here is what is called a [list comprehension](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/) in Python. This particular list comprehension looks a little gnarly because we happen to be building a list out of a dictionary. What I mean there is if we define `x = 'jhegele'`, then `Counter(x)` would return something that looks like this:

```python
{
    'j': 1,
    'h': 1,
    'e': 3,
    'g': 1,
    'l': 1
}
```

This is a dictionary. It is a set of keys (j, h, e, g, and l in this case) and their respective values (here the values are the number of occurrences of the letter). So, what we need to do here is to iterate over the dictionary and build a list of values that are equal to 2 or 3. If you refer back to the list comprehension above, that's exactly what we're doing. We're saying, "give me the value (v) for every key/value pair (k, v) produced when you run `Counter(x)` but **only** if the value (v) is equal to 2 or 3." That reference to `.items()` is telling Python that you want to use the keys _and_ the values. If you left that off, you would iterate over the keys _only_.

The `set()` function is used for convenience here as it will remove any duplicates (per the problem instructions, if the ID has two or more letters that occur twice, you only count one occurrence -- same is true for letters occurring three times). Moving out from there, the `map` and `lambda` combination simply applies our logic to the entire list of box IDs as an anonymous function. Then `list()` converts the output of `map()` to a list.

Whew, OK, now we have a list representing every single box ID. And for each box ID, if it has at least one set of characters repeated twice there will be a 2. If it has at least one set of characters repeated 3 times, there will be a 3. Our list, if we actually printed it out, would look something like this:

```
[set(), {2, 3}, {2}, {3}, {2}, {2}, {3}]
```

We just need to count the number of 2's and the number of 3's and multiply them and we're done.

## Part 2

I initially thought I figured out a "clever" way to approach this problem but, turns out that was _very_ wrong and it failed spectacularly. So, the general approach that I took here was to run through the list of IDs and compare each ID against all other IDs to find the instance where the values were off by one single letter.

Rather than working with nested loops, I built a process that would copmare two strings and return a series of 1's and 0's where 1's indicate that the letters in that position are a match and 0's indicate a mismatch. I can then sum this output and just look for an instance where it equals the length of the string minus one.

Here is where I'm implementing this logic:

```python
def matching_chars(check_id, test_id):
    return sum([1 if val == check_id[idx] else 0 for idx, val in enumerate(test_id)])
```

Again I'm using a list comprehension here. This takes the value of `test_id` and uses the `enumerate()` function to produce an iterable that contains the character and its index. It then uses the `idx` (index) to check that the letter in the same position in the `check_id` string matches. If it does, it assigns a 1, otherwise a 0.

The remainder of the code is simply applying this logic, iteratively, over the list of box IDs to find our result:

```python
box_ids = [v.strip() for v in box_ids]
for idx in range(0, len(box_ids)):
    check_id = box_ids[idx]
    other_ids = [box_id for box_id in box_ids if box_id != check_id]
    other_ids_char_matching = list(map(lambda x: matching_chars(check_id, x), other_ids))
    if len(check_id) - 1 in other_ids_char_matching:
        match_id = other_ids[other_ids_char_matching.index(len(check_id) - 1)]
        break
```

The first thing we do here is clean up the imported data. We don't actually have to do this but it makes it a little easier to print and test while building this.

```python 
box_ids = [v.strip() for v in box_ids]
```

The `.strip()` function will remove any whitespace (spaces or new line chars) from the front/back of a string.

```python
for idx in range(0, len(box_ids)):
```

This is basically Python's version of a traditional `for` loop. It will loop through all the values from 0 to whatever the length of `box_ids` is and, on each iteration, it will assign the new value to `idx`. Note that the loop will end before it actually reaches the final value. So, if you did something like this:

```python
for i in range(0, 5):
    print(i)
```

Your output here would be:

```
0
1
2
3
4
```

Once we're in the loop, we're just isolating the ID to test through this iteration, then generating a list that _excludes_ that ID, then applying our matching function to that list. If we find a string that matches all but one character, we're done.