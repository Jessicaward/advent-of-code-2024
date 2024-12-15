# Symbols
- `^/>/</V` - guard (with direction)
- `#` - obstructions
- `.` - path

# Guard Rules
- If something is ahead of you, turn right 90 degrees
- Otherwise take a step forward

# Goal
-  The guard will visit a distinct number of positions on the map, how many?

# Thoughts
- Simulate the rules, note down each distinct position
- Go until one of these finishing points is reached
    - The guard leaves the area
    - The guard reaches the starting position