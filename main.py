

#/usr/bin/env python

# Made by hnldesign <http://www.hnldesign.nl/>
# Translated to Python by Brandon Jackson <http://brackson.com/>

from random import choice

adjectives_1 = ["tossing", "bloody", "shitting", "wanking", "stinky", "raging", "dementing", "dumb", "dipping", "fucking",
                "dipping", "holy", "maiming", "cocking", "ranting", "twunting", "hairy", "spunking", "flipping", "slapping",
                "sodding", "blooming", "frigging", "sponglicking", "guzzling", "glistering", "cock wielding", "failed",
                "artist formally known as", "unborn", "pulsating", "naked", "throbbing", "lonely", "failed", "stale", "spastic",
                "senile", "strangely shaped", "virgin", "bottled", "twin-headed", "fat", "gigantic", "sticky", "prodigal",
                "bald", "bearded", "horse-loving", "spotty", "spitting", "dandy", "fritzl-admiring", "friend of a", 
                "indeterminable", "overrated", "fingerlicking", "diaper-wearing", "leg-humping", "gold-digging", "mong loving",
                "trout-faced", "cunt rotting", "flip-flopping", "rotting", "inbred", "badly drawn", "undead", "annoying",
                "whoring", "leaking", "dripping", "racist", "slutty", "cross-eyed", "irrelevant", "mental", "rotating", "scurvy looking",
                "rambling", "gag sacking", "cunting", "wrinkled old", "dried out", "sodding", "funky", "silly", "unhuman", "bloated",
                "wanktastic", "bum-banging", "cockmunching", "animal-fondling", "stillborn", "scruffy-looking", "hard-rubbing", "rectal",
                "glorious", "eye-less", "constipated", "bastardized", "utter", "hitler's personal", "irredeemable", "complete", "enormous",
                "go suck a", "fuckfaced", "broadfaced", "titless", "son of a", "demonizing", "pigfaced", "treacherous", "retarded"]

nouns_1 = ["cock", "tit", "cunt", "wank", "piss", "crap", "shit", "arse", "sperm", "nipple", "anus",
           "colon", "shaft", "dick", "poop", "semen", "slut", "suck", "earwax", "fart",
           "scrotum", "cock-tip", "tea-bag", "jizz", "cockstorm", "bunghole", "food trough", "bum",
           "butt", "shitface", "ass", "nut", "ginger", "llama", "tramp", "fudge", "vomit", "cum", "lard",
           "puke", "sphincter", "nerf", "turd", "cocksplurt", "cockthistle", "dickwhistle", "gloryhole",
           "gaylord", "spazz", "nutsack", "fuck", "spunk", "shitshark", "shitehawk", "fuckwit",
           "dipstick", "asswad", "chesticle", "clusterfuck", "douchewaffle", "retard"]

nouns_2 = ["force", "bottom", "hole", "goatse", "testicle", "balls", "bucket", "biscuit", "stain", "boy",
           "flaps", "erection", "mange", "twat", "twunt", "mong", "spack", "diarrhea", "sod",
           "excrement", "faggot", "pirate", "asswipe", "sock", "sack", "barrel", "head", "zombie", "alien",
           "minge", "candle", "torch", "pipe", "bint", "jockey", "udder", "pig", "dog", "cockroach",
           "worm", "MILF", "sample", "infidel", "spunk-bubble", "stack", "handle", "badger", "wagon", "bandit",
           "lord", "bogle", "bollock", "tranny", "knob", "nugget", "king", "hole", "kid", "trailer", "lorry", "whale",
           "rag", "foot"]

adjectives_2 = ["licker", "raper", "lover", "shiner", "blender", "fucker", "assjacker", "butler", "packer", "rider",
                "wanker", "sucker", "felcher", "wiper", "experiment", "wiper", "bender", "dictator", "basher", "piper",
                "slapper", "fondler", "plonker", "bastard", "handler", "herder", "fan", "amputee", "extractor", "professor", "graduate",
                "voyeur"]

def generate_insult():
    return choice([choice(adjectives_1) + ' ' + choice(nouns_1) + ' ' + choice(nouns_2),
                   choice(adjectives_1) + ' ' + choice(nouns_1) + ' ' + choice(adjectives_2),
                   choice(nouns_1) + ' ' + choice(nouns_2),
                   choice(nouns_1) + ' ' + choice(adjectives_2)])

if __name__ == '__main__':
        "you're a " + ', a '.join(generate_insult() for w in range(10)) + '.' # example usage

