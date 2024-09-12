lyrics = """A full commitment's what I'm thinking of
And if you ask me how I'm feeling
Desert you
Don't tell me you're too blind to see
Gotta make you understand
Hurt you
I just wanna tell you how I'm feeling
Inside, we both know what's been going on
Never gonna give you up
Never gonna give, never gonna give (give you up)
Never gonna let you down
Never gonna make you cry
Never gonna run around and desert you
Never gonna say goodbye
Never gonna tell a lie and hurt you
Ooh (give you up)
Ooh-ooh
Ooh-ooh (give you up)
Ooh-ooh-ooh-ooh
We know the game, and we're gonna play it
We're no strangers to love
We've known each other for so long
You know the rules and so do I
You wouldn't get this from any other guy
Your heart's been aching, but you're too shy to say it""".split("\n")

lyrics = [
    """We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy""",
    """I just wanna tell you how I'm feeling
Gotta make you understand""",
    """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",
    """We've known each other for so long
Your heart's been aching, but you're too shy to say it
Inside, we both know what's been going on
We know the game, and we're gonna play it""",
    """And if you ask me how I'm feeling
Don't tell me you're too blind to see""",
    """Ooh (give you up)
Ooh-ooh (give you up)
Ooh-ooh
Never gonna give, never gonna give (give you up)
Ooh-ooh
Never gonna give, never gonna give (give you up)""",
    """Desert you
Ooh-ooh-ooh-ooh
Hurt you""",
]

lyrics = [
    """We're no strangers to love
You know the rules and so do I (Do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",

    """We've known each other for so long
Your heart's been aching, but you're too shy to say it
Inside, we both know what's been going on
We know the game, and we're gonna play it

And if you ask me how I'm feeling
Don't tell me you're too blind to see

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",

    """Ooh (give you up)
Ooh-ooh (give you up)
Ooh-ooh
Never gonna give, never gonna give (give you up)
Ooh-ooh
Never gonna give, never gonna give (give you up)

We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

I just wanna tell you how I'm feeling
Gotta make you understand""",

    """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",
]

def byte_matches():
    matches = []

    for byte in range(256):
        lyrics_chunk = "\n"
        for i in range(4):
            lyrics_chunk += lyrics[(byte >> (6 - i * 2)) & 0b11] + "\n\n"

        matches += [lyrics_chunk[:-1]]
    
    return matches

def encode(b_data: bytes) -> str:
    matches = byte_matches()

    rickroll = ""

    for b in b_data:
        rickroll += matches[b]
    
    return rickroll

def decode(rickroll_data: str) -> bytes:
    matches = byte_matches()
    b_data = []

    while rickroll_data:
        for i, chunk in enumerate(matches):
            if rickroll_data.startswith(chunk):
                b_data += [i]
                rickroll_data = rickroll_data[len(chunk):]
                break
        else:
            raise RuntimeError("Invalid rickroll 💀")
    
    return bytes(b_data)

file = "hello world.rick"

with open(file, "w") as f:
    f.write(encode("Hello, my name is Kovka 😁".encode()))

with open(file, "r") as f:
    print(decode(f.read()).decode())