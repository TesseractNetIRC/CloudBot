
import random

from cloudbot import hook


@hook.command("drug","pill")
def lurve(text, nick, message):
        """Gives a User a drug <user>"""
        target = text.strip()

        # Use {N} to represent the person's nickname who is performing the action
        # Use {T} to represent the person's nickname who is the target of the act$
        drug = [
                "{N} hands {T} a bottle of Vicodin",
                "{N} hands {T} a bag of OxyContin",
                "{N} hands {T} a Morphine drip",
                "{N} hands {T} some Fentanyl",
                "{N} hands {T} a bottle of Codeine",
            ];

        out = "{}".format(random.choice(drug))
        out = out.replace("{N}", nick)
        out = out.replace("{T}", target)

        message(out)
