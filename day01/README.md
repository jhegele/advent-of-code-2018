# Day 1 Solutions Overview

## Part 1

In part one, we have a series of input and just need to aggregate them. My immediate thought here is that we need to get these inputs into a list (list is an array in Python) then just add them up.

```python
with open('./inputs/part1-2.txt') as file_input:
    freq_changes = file_input.readlines()
```

So, here I'm just loading the inputs from the text file into a list (well, technically the `readlines()` method produces an iterable but it behaves like a list so we'll stick with that terminology).

```python
print(sum(map(lambda x: int(x.replace('+', '')), freq_changes)))
```

This is pretty dense and not particularly readable (in other words, it's not particularly _good_ Python). Let's focus on the most relevant piece, though: the `map()` function. If you isolate that portion of the code, this is what you get:

```python
map(lambda x: int(x.replace('+', '')), freq_changes)
```

OK, full disclosure, this is _way_ overkill here. I made a mistake but I'll come back to that in a moment. Here's what's happening in this bit of code:

The `map()` function takes two inputs, a function and an iterable (like a list). So, the full function call looks like this: `map(func, iter)`. It will apply the function to each element of the iterable. In my code, I'm using a `lambda` function which is Python's version of an anonymous function. The easiest way to explain this is to look at a another way of accomplishing this:

```python
def strip_plus_sign(val):
    return int(val.replace('+', ''))

map(strip_plus_sign, freq_changes)
```

The above code does the _exact_ same thing but, instead of using a lambda function, I'm defining a function instead. So, you can think of a lambda as a way to define a function without ever actually giving it an identity. Why would you want to do this? Well, it's handy to be able to do this if your function is fairly simple and serves __exactly__ one purpose. There is plenty of additional literature online about lambda functions if you need/want to explore them a little more. [Here's the W3 Schools tutorial](https://www.w3schools.com/python/python_lambda.asp).

All of this is basically a way to explain that what I wanted to do with that `map()` function is to convert a list of strings that looks like this: `['+1', '-3', '+4', '-2']` to a list of integers that looks like this: `[1, -3, 4, -2]` so that Python can actually add the contents.

Now, remember where I said this was overkill and that I made a mistake? Well, my mistake was assuming that Python's `int()` function would fail to parse something like `'+3'` to `3`. I assumed that the presence of the "+" would cause an error. Turns out, that assumption is incorrect. So, I could have just done this instead of the gnarly "thing" I created:

```python
map(int, freq_changes)
```

In any case, once you have your list of integers, just sum them up and you're done.

## Part 2

This part was slightly more complex than I was expecting for a Day 1 problem. I originally missed that, in order to get the answer, you may need to iterate over the frequency changes more than once. But, once I had that I coded up a solution pretty quickly. Problem is, my original solution is wildly inefficient and takes a whopping 86 seconds to complete on my machine (this is a crazy long time for something so simple, a sure sign that it is **very** poorly optimized).

Opening the file and loading values is the same as above, so I won't go over that here. The relevant piece for Part 2 is this section of code:

```python
while True:
    freq_cumulative += int(freq_changes[freq_change_idx].replace('+', ''))
    if freq_cumulative in freqs_seen:
        print('First reaches {} twice!'.format(freq_cumulative))
        break
    freqs_seen.append(freq_cumulative)
    if freq_change_idx == len(freq_changes) - 1:
        freq_change_idx = 0
    else:
        freq_change_idx += 1
```

Wait, that's an infinite loop! What gives? Yes, it is an infinite loop and that's because I wasn't sure how many times I would actually need to loop through the series of frequencies to get the correct answer. Don't worry, once we find the first repeat, we break the loop so we're in good shape here.

Basically, the flow of this loop is:

1. Update the cumulative frequency
2. Check to see if we have seen this frequency before and, if we have, print it out because we're done
3. If we haven't, append this frequency to our list where we're tracking what we've seen
4. Update our index -- if we're at the end of the list of frequency changes, start over, otherwise move to the next one

Using this logic, it'll continue looping through the list of frequency changes, adding them up, until it finds one we've seen before.

This works but, as mentioned, it is _wildly_ inefficient. I went back and optimzed this (see the `-optimized` version) and the processing time went from 86.6 seconds to 0.10 seconds. The change that drove most of this is that I used a set to track what we had seen before rather than a list. Searching a set is **way** faster than searching a list.