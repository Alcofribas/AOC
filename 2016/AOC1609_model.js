// AOC 2016 Day 9 Model Solution

// https://www.reddit.com/r/adventofcode/comments/5hbygy/2016_day_9_solutions/daz2y09/

// JavaScript (JS, ES2015/ES6)
// both parts in one
// runs in FF/Chrome browser console on the /input page.
// First time on the leaderboard (#87 for part 2), wow.

// (+next): convert next to integer

const unzipLen = (s, rec = false) => {
    let [sum, i] = [0, 0];
    while (i < s.length) {
        if (s[i] !== '(') {
            [sum, i] = [sum + 1, i + 1];
            continue;
        }
				// found bracket
        const [m, next, repeat] = s.slice(i).match(/\((\d+)x(\d+)\)/),
            sectEnd = i + m.length + (+next),
            sectLen = (+repeat) * (rec ? unzipLen(s.slice(i + m.length, sectEnd), rec) : +next);
        [sum, i] = [sum + sectLen, sectEnd];
    }

    return sum;
};

const input = document.body.textContent.trim();
// part1, part2
console.log(unzipLen(input), unzipLen(input, true));
