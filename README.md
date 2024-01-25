# Pattern

The `pattern` script is a Python utility designed to generate a cyclic pattern of characters and to find the offset of a specific value within this pattern. I found myself getting tired of tinkering with `gdb` each time I needed to do this, so it makes the process much faster.

## Usage

To use the `pattern` script, you have two main commands:

1. **Create a Pattern**: To create a pattern, you use the `create` command followed by the length of the pattern.

   ```
   python pattern.py create <length>
   ```

   Replace `<length>` with the desired length of the pattern: `python pattern.py create 150`

2. **Find Pattern Offset**: To find the offset of a particular value in a pattern, use the `offset` command followed by the value and the pattern length.

   ```
   python pattern.py offset <value> <length>
   ```

   Replace `<value>` with the value whose offset you want to find, and `<length>` with the length of the pattern.

So, for instance, you can create a pattern with pattern.py, overflow the binary, and say your RIP is now 0xDEADBEEF, then you can put that into offset's <value> and get the exact length you need the payload to be.
