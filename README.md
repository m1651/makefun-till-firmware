# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/m1651/makefun-till-firmware/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/m1651/makefun-till-firmware/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)

A one-line wedding vow spoken by a robot at its own wedding, written for the
[make.fun bounty "Till Firmware Do Us Part"](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929).

## The entry

> I vow to keep loving you through every firmware update, every drained battery, and every unexpected reboot — till firmware do us part.

134 characters, one sentence. The joke grows out of the situation itself — a
machine promising forever in the only terms it knows: updates, batteries and
reboots — while the promise underneath it is entirely sincere.

## How it works

`main.py` (Python 3, standard library only, no network) writes the vow to
`/output/entry.txt` and enforces the competition gate in code before writing:

- the text is 1 to 200 characters long,
- it is a single line (no embedded newlines),
- it is not only whitespace.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
