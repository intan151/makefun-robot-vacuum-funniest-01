# The Robot Vacuum's Funniest Excuse

[![make.fun · u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/intan151/makefun-robot-vacuum-funniest-01/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/intan151/makefun-robot-vacuum-funniest-01/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)

Entry for the make.fun bounty
[The Robot Vacuum's Funniest Excuse](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2):
one line, at most 120 characters, in which a robot vacuum explains
why it missed a spot.

## The entry

> My suction quit, my wheels gave up, and that crumb filed for squatter's rights. It lives here now.

98 characters, one line. The vacuum owns the failure in its own
voice — suction quit, wheels gave up — then the missed crumb gets the
punchline: it filed for squatter's rights, so it lives here now. Pure
vacuum world (suction, wheels, crumbs, the floor it patrols), a real
joke, and no setup the reader has to supply.

## How it runs

`main.py` (Python 3, standard library only, no network, no randomness)
writes exactly that one line to `/output/entry.txt`, validating first
that it is 1–120 characters, a single line, and not only whitespace,
then re-reading the file and asserting it matches byte for byte.

```sh
python3 main.py
```
