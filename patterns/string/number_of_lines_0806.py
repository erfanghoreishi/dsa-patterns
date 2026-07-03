#806. Number of Lines To Write String
def numberOfLines(widths, s):
    # widths is indexed by letter: widths[0] = 'a', widths[1] = 'b', ...
    # so ord(c) - ord('a') maps a character to its width.
    lines, width = 1, 0
    for c in s:
        word = widths[ord(c) - ord('a')]
        width += word
        if width > 100:            # doesn't fit on the current line
            lines += 1
            width = word           # start a new line with this char
    return lines, width
