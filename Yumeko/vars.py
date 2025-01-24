import random

random_afk_message = (
        "𝖭𝖺𝗋𝗎𝗁𝗈𝖽𝗈! 𝖶𝖺𝗍𝖼𝗁𝗂𝗇𝗀 𝗉𝗈𝗋𝗇 𝖺𝗀𝖺𝗂𝗇?",
        "𝖸𝖾𝖺𝗁 𝗌𝗅𝖾𝖾𝗉 𝖺𝗅𝗋𝖾𝖺𝖽𝗒.",
        "𝖧𝖺𝖺𝗁! 𝖬𝖺𝗒𝖻𝖾 𝖽𝗈𝗂𝗇𝗀 𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝗅𝖾𝗐𝖽 𝖻𝖾𝗁𝗂𝗇𝖽 𝗆𝗒 𝖻𝖺𝖼𝗄.",
        "𝖮𝗄𝖺𝗒, 𝗎𝗉𝖽𝖺𝗍𝗂𝗇𝗀 𝗒𝗈𝗎𝗋 𝖺𝖿𝗄 𝗌𝗍𝖺𝗍𝗎𝗌, 𝖻𝖾 𝗀𝗋𝖺𝗍𝖾𝖿𝗎𝗅 𝗍𝗈 𝗆𝖾.",
        "𝖨 𝗄𝗇𝗈𝗐 𝗒𝗈𝗎 𝖺𝗋𝖾 𝗋𝖾𝖺𝖽𝗂𝗇𝗀..... 𝖬𝖺𝗒 𝖻𝖾 𝖣𝗈𝗎𝗃𝗂𝗇𝗌",
        "𝖲𝗈, 𝗒𝗈𝗎 𝖿𝗂𝗇𝖺𝗅𝗅𝗒 𝖽𝖾𝖼𝗂𝖽𝖾𝖽 𝗍𝗈 𝗅𝖾𝖺𝗏𝖾. 𝖬𝖺𝗒𝖻𝖾 𝗀𝗈𝗂𝗇𝗀 𝗍𝗈 𝗋𝖾𝗅𝗂𝖾𝗏𝖾 𝗒𝗈𝗎𝗋 𝗌𝗍𝗋𝖾𝗌𝗌 𝗂𝗇 𝖿𝗈𝗋𝗆 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖿𝗅𝗎𝗂𝖽𝗌.",
        "𝖨 𝖽𝗈𝗇'𝗍 𝗍𝗁𝗂𝗇𝗄 𝗒𝗈𝗎 𝗀𝗈𝗍 𝖺 𝗀𝗂𝗋𝗅 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝖺𝗋𝖾 𝗂𝗀𝗇𝗈𝗋𝗂𝗇𝗀 𝗍𝗁𝗂𝗌 𝗉𝗋𝖾𝖼𝗂𝗈𝗎𝗌 𝖼𝗁𝖺𝗍, 𝗌𝗈 𝗐𝗁𝖺𝗍 𝖺𝗋𝖾 𝗒𝗈𝗎 𝗎𝗉𝗍𝗈?",
        "𝖶𝖺𝗄𝖺𝗍𝗍𝖺! 𝖲𝖺𝗒𝗈𝗇𝖺𝗋𝖺👋",
        "𝖮𝗄𝖺𝗒! 𝖧𝖺𝗏𝖾 𝗒𝗈𝗎 𝖽𝖾𝖼𝗂𝖽𝖾𝖽 𝗍𝗈 𝖽𝗈 𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝗎𝗌𝖾𝖿𝗎𝗅 𝗈𝗋 𝗌𝗍𝗂𝗅𝗅 𝗃𝖾𝗋𝗄𝗂𝗇𝗀 𝗈𝖿𝖿?",
        "𝖣𝖺𝗆𝗇! 𝖸𝗈𝗎'𝗋𝖾 𝗅𝖾𝖺𝗏𝗂𝗇𝗀, 𝗅𝗂𝗄𝖾 𝖨 𝗐𝗂𝗅𝗅 𝖾𝗏𝖾𝗇 𝗆𝗂𝗌𝗌 𝗒𝗈𝗎.",
        "𝖸𝖾𝖺𝗁 𝗅𝖾𝖺𝗏𝖾! 𝖦𝗋𝗈𝗎𝗉 𝖿𝖾𝖾𝗅𝗌 𝗌𝗈 𝖼𝗅𝖾𝖺𝗇 𝗇𝗈𝗐.",
        "𝖲𝖾𝖾 𝗒𝖺! 𝖭𝗈𝗐 𝖨'𝗅𝗅 𝖾𝗇𝗃𝗈𝗒 𝗆𝗒 𝗈𝖻𝗌𝖾𝗋𝗏𝖺𝗍𝗂𝗈𝗇𝗌 𝗁𝖾𝗋𝖾.",
        "𝖨 𝗐𝖺𝗌 𝖺𝖻𝗈𝗎𝗍 𝗍𝗈 𝖺𝗌𝗄 𝗒𝗈𝗎 𝖿𝗈𝗋 𝖺 𝖼𝗈𝖿𝖿𝖾𝖾, 𝖻𝗎𝗍 𝗒𝗈𝗎 𝖺𝗋𝖾 𝗅𝖾𝖺𝗏𝗂𝗇𝗀 𝖺𝗅𝗋𝖾𝖺𝖽𝗒.",
        "𝖸𝖾𝗌! 𝖦𝗈 𝖺𝗐𝖺𝗒, 𝗒𝗈𝗎 𝖺𝗋𝖾 𝖺 𝗍𝗋𝗈𝗎𝖻𝗅𝖾𝗌𝗈𝗆𝖾.😏",
        "𝖣𝗈𝗇'𝗍 𝗒𝗈𝗎 𝗐𝖺𝗇𝗇𝖺 𝗁𝖾𝖺𝗋 𝗆𝗒 𝗐𝗎𝗏 𝗌𝗍𝗈𝗋𝗒🥰..",
        "𝖧𝗆𝗆𝗉𝗁! 𝖫𝖾𝖺𝗏𝖾 𝖺𝗅𝗋𝖾𝖺𝖽𝗒.\𝗇**𝖺𝗇𝗀𝗋𝗒 𝖼𝗎𝗍𝖾 𝗉𝗈𝗎𝗍𝗌**",
        "𝖶𝗍𝖿, 𝗀𝗈𝗂𝗇𝗀 𝖺𝗅𝗋𝖾𝖺𝖽𝗒? 𝖭𝗈𝗍 𝗅𝗂𝗄𝖾 𝖨 𝖼𝖺𝗋𝖾 𝖺𝖻𝗈𝗎𝗍 𝗂𝗍.",
        "𝖣𝗈 𝗒𝗈𝗎 𝗄𝗇𝗈𝗐 𝗐𝗁𝖺𝗍 𝗂𝗍 𝖿𝖾𝖾𝗅𝗌 𝗅𝗂𝗄𝖾 𝗂𝗇 𝗅𝖺𝗏𝖺? 𝖩𝗎𝗌𝗍 𝗀𝗈 𝖺𝗇𝖽 𝗌𝗂𝗇𝗄 𝗂𝗇 𝗂𝗍 🔥",
        "𝖡𝗒𝖾 𝖻𝗒𝖾!!! 𝖢𝗎𝗆 𝖻𝖺𝖼𝗄 𝗌𝗈𝗈𝗇",
        '𝖡𝖾𝖿𝗈𝗋𝖾 𝗅𝖾𝖺𝗏𝗂𝗇𝗀, 𝖧𝖾 𝗍𝗈𝗅𝖽 𝗆𝖾 "𝖡𝖾 𝗍𝗁𝖾 𝗍𝗌𝗎𝗇 𝗍𝗈 𝗆𝗒 𝖽𝖾𝗋𝖾". 𝖲𝗎𝖼𝗁 𝖺 𝗅𝖾𝗐𝖽 𝖻𝗋𝖺𝗍',
        "𝖤𝗇𝗃𝗈𝗒 𝖿𝖺𝗉𝗉𝗂𝗇𝗀.. 𝖨 𝗆𝖾𝖺𝗇 𝗇𝖺𝗉𝗉𝗂𝗇𝗀*.",
        "𝖲𝗍𝗈𝗉 𝖽𝗋𝖾𝖺𝗆𝗂𝗇𝗀 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎'𝗅𝗅 𝖿𝗂𝗇𝖽 𝖺 𝖽𝖺𝗍𝖾.",
        "𝖠 𝖲𝗇𝗈𝗐𝖻𝖺𝗅𝗅 𝖿𝗂𝗀𝗁𝗍? 𝖭𝗈 𝗍𝗁𝖺𝗇𝗄𝗌! 𝖸𝗈𝗎 𝗆𝗂𝗀𝗁𝗍 𝗁𝗂𝗍 𝗆𝖾 𝗈𝗇 𝗆𝗒 𝖼𝗁𝖾𝗌𝗍.",
        "𝖨 𝗍𝗁𝗂𝗇𝗄 𝗍𝗁𝖾𝗋𝖾 𝗂𝗌 𝗇𝗈 𝖦𝗂𝗋𝗅 𝗂𝗇 𝗍𝗁𝗂𝗌 𝖼𝗁𝖺𝗍, 𝗍𝗁𝖺𝗍'𝗌 𝗐𝗁𝗒 𝗒𝗈𝗎 𝖺𝗋𝖾 𝗀𝗈𝗂𝗇𝗀 𝖺𝗐𝖺𝗒.",
        "**𝖣𝗈𝗇'𝗍 𝗍𝖾𝗅𝗅 𝗆𝗒 𝖬𝖺𝖾𝗌𝗍𝗋𝗈 𝖺𝖻𝗈𝗎𝗍 𝗍𝗁𝗂𝗌**, 𝗂𝖿 𝗒𝗈𝗎'𝗅𝗅 𝗐𝖺𝗂𝗍 𝖨 𝖼𝖺𝗇 𝖿𝗅𝗂𝗋𝗍 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎 𝖺 𝗅𝗂𝗍𝗍𝗅𝖾.",
        "𝖣𝗈 𝗒𝗈𝗎 𝗄𝗇𝗈𝗐 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝖺𝖻𝗈𝗎𝗍 𝖺 𝖳𝗁𝗂𝗀𝗁 𝗆𝖺𝗌𝗌𝖺𝗀𝖾 𝖩𝗈𝖻? 𝖮𝗈𝗉𝗌 𝗆𝗒 𝖻𝖺𝖽, 𝖨 𝗆𝖾𝖺𝗇𝗍 𝖳𝗁𝖺𝗂* 𝖬𝖺𝗌𝗌𝖺𝗀𝖾 𝖩𝗈𝖻𝗌.",
        "𝖬𝗂𝗇𝖽 𝗂𝖿 𝖨 𝖼𝗈𝗆𝖾 𝖺𝗅𝗈𝗇𝗀 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎? 𝖮𝗇𝗅𝗒 𝗂𝖿 𝗒𝗈𝗎 𝖺𝗋𝖾 𝗇𝗈𝗍 𝗍𝗁𝗂𝗇𝗄𝗂𝗇𝗀 𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝗅𝖾𝗐𝖽.",
        "𝖠 𝗌𝗍𝖾𝖺𝗆𝗒 𝖻𝖺𝗍𝗁, 𝖨 𝖺𝗆 𝖻𝖺𝖼𝗄 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝖺 𝖳𝗈𝗐𝖾𝗅. 𝖳𝗁𝖺𝗇𝗄 𝖦𝗈𝖽 𝗒𝗈𝗎 𝖺𝗋𝖾 𝗅𝖾𝖺𝗏𝗂𝗇𝗀, 𝗉𝖾𝗋𝗏.",
        "𝖧𝗆𝗆𝗆𝗆𝗆𝗆𝗆𝗆. 𝖶𝖺𝗇𝗄𝗂𝗇𝗀 𝗈𝖿𝖿?",
        "𝖣𝗂𝖽 𝗒𝗈𝗎 𝗃𝗎𝗌𝗍 𝗌𝗁𝗈𝗍 𝗌𝗈𝗆𝖾 𝗌𝗍𝗂𝖼𝗄𝗒 𝗌𝗍𝗎𝖿𝖿 𝗈𝗇 𝗒𝗈𝗎𝗋 𝗉𝗁𝗈𝗇𝖾 𝖻𝗒 𝗌𝖾𝖾𝗂𝗇𝗀 𝗆𝗒 𝗉𝗂𝖼? 𝖳𝗁𝖺𝗍'𝗌 𝗐𝗁𝗒 𝗀𝗈𝗂𝗇𝗀 𝖺𝗐𝖺𝗒.",
        "𝖥𝗂𝗇𝖾! 𝖨 𝗐𝗈𝗇'𝗍 𝖻𝖾 𝖺 𝖻𝗈𝗍𝗁𝖾𝗋, 𝗅𝗂𝗄𝖾 𝖨 𝖼𝖺𝗋𝖾 𝗂𝖿 𝗒𝗈𝗎 𝖺𝗋𝖾 𝖺𝗐𝖺𝗒. 𝖧𝗆𝗆𝗉𝗁𝗁",
        "𝖸𝗈𝗎 𝗉𝗅𝖺𝗒𝗂𝗇𝗀 𝖢𝖲:𝖦𝖮 𝗇𝗈𝗐? 𝖬𝗒 𝗄𝗂𝗅𝗅 𝗌𝗍𝗋𝖾𝖺𝗄 𝗂𝗌 𝟣𝟥, 𝖻𝗎𝗍 𝖨 𝖽𝗈𝗇'𝗍 𝗉𝗅𝖺𝗒 𝖺𝗇𝗒 𝗀𝖺𝗆𝖾𝗌.🔪🪓🩸",
        "𝖸𝖾𝖺𝗁, 𝖦𝗈 𝖺𝗐𝖺𝗒 𝖧𝗈𝗋𝗇𝗒.",
    )

random_afk_reply_message = [
                "𝖨𝗌 𝖶𝗂𝗍𝗁 𝖸𝗈𝗎𝗋 𝖦𝖥!",
                "𝖨𝗌 𝖶𝗂𝗍𝗁 𝖸𝗈𝗎𝗋 𝖡𝖥!",
                "𝖨𝗌 𝖬𝖺𝗌𝗍𝗎𝗋𝖻𝖺𝗍𝗂𝗇𝗀! 𝖯𝗅𝖾𝖺𝗌𝖾 𝖣𝗈𝗇'𝗍 𝖣𝗂𝗌𝗍𝗎𝗋𝖻 𝖧𝗂𝗆.",
                "𝖨𝗌 𝖶𝗂𝗍𝗁 𝖸𝗈𝗎𝗋 𝖢𝗋𝗎𝗌𝗁",
                "𝖨𝗌 𝖶𝗂𝗍𝗁 𝖸𝗈𝗎𝗋 𝖲𝗂𝗌",
                "𝖨𝗌 𝖯𝗅𝖺𝗒𝗂𝗇𝗀 𝖲𝗊𝗎𝗂𝖽 𝖦𝖺𝗆𝖾, 𝖧𝖾 𝖶𝗂𝗅𝗅 𝖢𝗈𝗆𝖾 𝖡𝖺𝖼𝗄 𝖠𝖿𝗍𝖾𝗋 𝖶𝗂𝗇𝗇𝗂𝗇𝗀 𝖠 𝖫𝗈𝗍 𝖮𝖿 𝖬𝗈𝗇𝖾𝗒🤑",
            ]

random_back_online_message = (
    "𝖥𝗂𝗇𝗂𝗌𝗁𝖾𝖽 𝖿𝗅𝗂𝗋𝗍𝗂𝗇𝗀 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗋𝗎𝗌𝗁 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗀𝗈𝗍 𝗋𝖾𝗃𝖾𝖼𝗍𝖾𝖽?",
    "𝗈𝗁 𝗅𝗈𝗈𝗄, 𝖶𝖺𝗌 𝗂𝗍 𝗅𝗈𝗏𝖾, 𝗈𝗋 𝗐𝖾𝗋𝖾 𝗒𝗈𝗎 𝗃𝗎𝗌𝗍 𝖻𝖾𝗍𝗋𝖺𝗒𝖾𝖽 𝖺𝗀𝖺𝗂𝗇?",
    "𝖣𝗂𝖽 𝗒𝗈𝗎 𝗋𝗎𝗇 𝗈𝗎𝗍 𝗈𝖿 𝗍𝗂𝗌𝗌𝗎𝖾𝗌, 𝗈𝗋 𝖺𝗋𝖾 𝗒𝗈𝗎 𝗃𝗎𝗌𝗍 𝗁𝖾𝗋𝖾 𝗍𝗈 𝗉𝗋𝖾𝗍𝖾𝗇𝖽 𝗇𝗈𝗍𝗁𝗂𝗇𝗀 𝗁𝖺𝗉𝗉𝖾𝗇𝖾𝖽?",
    "𝖶𝖺𝗌 𝗂𝗍 𝖺 𝗋𝗈𝗆𝖺𝗇𝗍𝗂𝖼 𝖿𝖺𝗂𝗅 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗒𝗈𝗎𝗋 𝗁𝖺𝗇𝖽 𝗄𝖾𝖾𝗉𝗂𝗇𝗀 𝗒𝗈𝗎 𝖻𝗎𝗌𝗒?",
    "𝖫𝖾𝗍 𝗆𝖾 𝗀𝗎𝖾𝗌𝗌—𝗒𝗈𝗎𝗋 𝖼𝗋𝗎𝗌𝗁 𝗅𝖾𝖿𝗍 𝗒𝗈𝗎 𝗈𝗇 𝗋𝖾𝖺𝖽 𝖺𝗀𝖺𝗂𝗇, 𝗋𝗂𝗀𝗁𝗍?",
    "𝗈𝗁, 𝖻𝖺𝖼𝗄 𝗋𝖾𝖺𝗅𝗅𝗒? 𝖣𝗂𝖽 𝗒𝗈𝗎 𝖿𝗂𝗇𝖺𝗅𝗅𝗒 𝗌𝗍𝗈𝗉 𝖼𝗋𝗒𝗂𝗇𝗀 𝗈𝗏𝖾𝗋 𝗒𝗈𝗎𝗋 𝖾𝗑?",
    "𝖫𝗈𝗏𝖾 𝖽𝗂𝖽𝗇’𝗍 𝗐𝗈𝗋𝗄 𝗈𝗎𝗍, 𝗈𝗋 𝖽𝗂𝖽 𝗋𝖾𝖺𝗅𝗂𝗍𝗒 𝗁𝗂𝗍 𝗍𝗈𝗈 𝗁𝖺𝗋𝖽?",
    "𝖣𝗈𝗇𝖾 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 ‘𝖺𝗅𝗈𝗇𝖾 𝗍𝗂𝗆𝖾,’ 𝗈𝗋 𝗂𝗌 𝗂𝗍 𝗃𝗎𝗌𝗍 𝗁𝖺𝗅𝖿𝗍𝗂𝗆𝖾?",
)



quotes = [
        ("𝖡𝖾𝗅𝗂𝖾𝗏𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋𝗌𝖾𝗅𝖿. 𝖭𝗈𝗍 𝗂𝗇 𝗍𝗁𝖾 𝗒𝗈𝗎 𝗐𝗁𝗈 𝖻𝖾𝗅𝗂𝖾𝗏𝖾𝗌 𝗂𝗇 𝗆𝖾. 𝖭𝗈𝗍 𝗍𝗁𝖾 𝗆𝖾 𝗐𝗁𝗈 𝖻𝖾𝗅𝗂𝖾𝗏𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎. 𝖡𝖾𝗅𝗂𝖾𝗏𝖾 𝗂𝗇 𝗍𝗁𝖾 𝗒𝗈𝗎 𝗐𝗁𝗈 𝖻𝖾𝗅𝗂𝖾𝗏𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋𝗌𝖾𝗅𝖿.", "𝖪𝖺𝗆𝗂𝗇𝖺", "𝖳𝖾𝗇𝗀𝖾𝗇 𝖳𝗈𝗉𝗉𝖺 𝖦𝗎𝗋𝗋𝖾𝗇 𝖫𝖺𝗀𝖺𝗇𝗇"),
        ("𝖨𝗍'𝗌 𝗇𝗈𝗍 𝗍𝗁𝖾 𝖿𝖺𝖼𝖾 𝗍𝗁𝖺𝗍 𝗆𝖺𝗄𝖾𝗌 𝗌𝗈𝗆𝖾𝗈𝗇𝖾 𝖺 𝗆𝗈𝗇𝗌𝗍𝖾𝗋, 𝗂𝗍'𝗌 𝗍𝗁𝖾 𝖼𝗁𝗈𝗂𝖼𝖾𝗌 𝗍𝗁𝖾𝗒 𝗆𝖺𝗄𝖾 𝗐𝗂𝗍𝗁 𝗍𝗁𝖾𝗂𝗋 𝗅𝗂𝗏𝖾𝗌.", "𝖭𝖺𝗋𝗎𝗍𝗈 𝖴𝗓𝗎𝗆𝖺𝗄𝗂", "𝖭𝖺𝗋𝗎𝗍𝗈"),
        ("𝖳𝗁𝖾 𝗈𝗇𝗅𝗒 𝗍𝗁𝗂𝗇𝗀 𝗍𝗁𝖺𝗍 𝖼𝖺𝗇 𝖽𝖾𝖿𝖾𝖺𝗍 𝗉𝗈𝗐𝖾𝗋 𝗂𝗌 𝗆𝗈𝗋𝖾 𝗉𝗈𝗐𝖾𝗋. 𝖳𝗁𝖺𝗍 𝗂𝗌 𝗍𝗁𝖾 𝗈𝗇𝖾 𝖼𝗈𝗇𝗌𝗍𝖺𝗇𝗍 𝗂𝗇 𝗍𝗁𝗂𝗌 𝗎𝗇𝗂𝗏𝖾𝗋𝗌𝖾. 𝖧𝗈𝗐𝖾𝗏𝖾𝗋, 𝗍𝗁𝖾𝗋𝖾 𝗂𝗌 𝗇𝗈 𝗉𝗈𝗂𝗇𝗍 𝗂𝗇 𝗉𝗈𝗐𝖾𝗋 𝗂𝖿 𝗂𝗍 𝖼𝗈𝗇𝗌𝗎𝗆𝖾𝗌 𝗂𝗍𝗌𝖾𝗅𝖿.", "𝖨𝗍𝖺𝖼𝗁𝗂 𝖴𝖼𝗁𝗂𝗁𝖺", "𝖭𝖺𝗋𝗎𝗍𝗈"),
        ("𝖭𝗈 𝗈𝗇𝖾 𝗄𝗇𝗈𝗐𝗌 𝗐𝗁𝖺𝗍 𝗍𝗁𝖾 𝖿𝗎𝗍𝗎𝗋𝖾 𝗁𝗈𝗅𝖽𝗌. 𝖳𝗁𝖺𝗍'𝗌 𝗐𝗁𝗒 𝗂𝗍𝗌 𝗉𝗈𝗍𝖾𝗇𝗍𝗂𝖺𝗅 𝗂𝗌 𝗂𝗇𝖿𝗂𝗇𝗂𝗍𝖾.", "𝖱𝗂𝗇𝗍𝖺𝗋𝗈𝗎 𝖮𝗄𝖺𝖻𝖾", "𝖲𝗍𝖾𝗂𝗇𝗌;𝖦𝖺𝗍𝖾"),
        ("𝖣𝗈𝗇'𝗍 𝖿𝗈𝗋𝗀𝖾𝗍. 𝖠𝗅𝗐𝖺𝗒𝗌, 𝗌𝗈𝗆𝖾𝗐𝗁𝖾𝗋𝖾, 𝗌𝗈𝗆𝖾𝗈𝗇𝖾 𝗂𝗌 𝖿𝗂𝗀𝗁𝗍𝗂𝗇𝗀 𝖿𝗈𝗋 𝗒𝗈𝗎. 𝖠𝗌 𝗅𝗈𝗇𝗀 𝖺𝗌 𝗒𝗈𝗎 𝗋𝖾𝗆𝖾𝗆𝖻𝖾𝗋 𝗁𝖾𝗋, 𝗒𝗈𝗎 𝖺𝗋𝖾 𝗇𝗈𝗍 𝖺𝗅𝗈𝗇𝖾.", "𝖬𝖺𝖽𝗈𝗄𝖺 𝖪𝖺𝗇𝖺𝗆𝖾", "𝖯𝗎𝖾𝗅𝗅𝖺 𝖬𝖺𝗀𝗂 𝖬𝖺𝖽𝗈𝗄𝖺 𝖬𝖺𝗀𝗂𝖼𝖺"),
        ("𝖳𝗁𝖾 𝗈𝗇𝗅𝗒 𝗍𝗁𝗂𝗇𝗀 𝗐𝖾'𝗋𝖾 𝖺𝗅𝗅𝗈𝗐𝖾𝖽 𝗍𝗈 𝖽𝗈 𝗂𝗌 𝗍𝗈 𝖻𝖾𝗅𝗂𝖾𝗏𝖾 𝗍𝗁𝖺𝗍 𝗐𝖾 𝗐𝗈𝗇'𝗍 𝗋𝖾𝗀𝗋𝖾𝗍 𝗍𝗁𝖾 𝖼𝗁𝗈𝗂𝖼𝖾 𝗐𝖾 𝗆𝖺𝖽𝖾.", "𝖫𝖾𝗏𝗂 𝖠𝖼𝗄𝖾𝗋𝗆𝖺𝗇", "𝖠𝗍𝗍𝖺𝖼𝗄 𝗈𝗇 𝖳𝗂𝗍𝖺𝗇"),
        ("𝖶𝗁𝖺𝗍𝖾𝗏𝖾𝗋 𝗒𝗈𝗎 𝖽𝗈, 𝖾𝗇𝗃𝗈𝗒 𝗂𝗍 𝗍𝗈 𝗍𝗁𝖾 𝖿𝗎𝗅𝗅𝖾𝗌𝗍. 𝖳𝗁𝖺𝗍 𝗂𝗌 𝗍𝗁𝖾 𝗌𝖾𝖼𝗋𝖾𝗍 𝗈𝖿 𝗅𝗂𝖿𝖾.", "𝖱𝗂𝖽𝖾𝗋 (𝖨𝗌𝗄𝖺𝗇𝖽𝖺𝗋)", "𝖥𝖺𝗍𝖾/𝖹𝖾𝗋𝗈"),
        ("𝖨𝖿 𝗒𝗈𝗎 𝖽𝗈𝗇'𝗍 𝗍𝖺𝗄𝖾 𝗋𝗂𝗌𝗄𝗌, 𝗒𝗈𝗎 𝖼𝖺𝗇'𝗍 𝖼𝗋𝖾𝖺𝗍𝖾 𝖺 𝖿𝗎𝗍𝗎𝗋𝖾.", "𝖬𝗈𝗇𝗄𝖾𝗒 𝖣. 𝖫𝗎𝖿𝖿𝗒", "𝖮𝗇𝖾 𝖯𝗂𝖾𝖼𝖾"),
        ("𝖨𝗇 𝗈𝗋𝖽𝖾𝗋 𝗍𝗈 𝗀𝗋𝗈𝗐, 𝗒𝗈𝗎 𝗆𝗎𝗌𝗍 𝖿𝖺𝖼𝖾 𝗍𝗁𝖾 𝗉𝖺𝗂𝗇 𝗈𝖿 𝗍𝗁𝖾 𝗉𝖺𝗌𝗍. 𝖠𝖼𝖼𝖾𝗉𝗍 𝗂𝗍 𝖺𝗇𝖽 𝗆𝗈𝗏𝖾 𝖿𝗈𝗋𝗐𝖺𝗋𝖽.", "𝖤𝗋𝗓𝖺 𝖲𝖼𝖺𝗋𝗅𝖾𝗍", "𝖥𝖺𝗂𝗋𝗒 𝖳𝖺𝗂𝗅"),
        ("𝖲𝗈𝗆𝖾𝗍𝗂𝗆𝖾𝗌 𝗍𝗁𝖾 𝗍𝗁𝗂𝗇𝗀𝗌 𝗍𝗁𝖺𝗍 𝗆𝖺𝗍𝗍𝖾𝗋 𝗍𝗁𝖾 𝗆𝗈𝗌𝗍 𝖺𝗋𝖾 𝗋𝗂𝗀𝗁𝗍 𝗂𝗇 𝖿𝗋𝗈𝗇𝗍 𝗈𝖿 𝗒𝗈𝗎.", "𝖠𝗌𝗎𝗇𝖺 𝖸𝗎𝗎𝗄𝗂", "𝖲𝗐𝗈𝗋𝖽 𝖠𝗋𝗍 𝖮𝗇𝗅𝗂𝗇𝖾"),
        ("𝖳𝗁𝖾 𝗐𝗈𝗋𝗅𝖽’𝗌 𝗇𝗈𝗍 𝗉𝖾𝗋𝖿𝖾𝖼𝗍, 𝖻𝗎𝗍 𝗂𝗍’𝗌 𝗍𝗁𝖾𝗋𝖾 𝖿𝗈𝗋 𝗎𝗌 𝗍𝗋𝗒𝗂𝗇𝗀 𝗍𝗁𝖾 𝖻𝖾𝗌𝗍 𝗂𝗍 𝖼𝖺𝗇. 𝖳𝗁𝖺𝗍’𝗌 𝗐𝗁𝖺𝗍 𝗆𝖺𝗄𝖾𝗌 𝗂𝗍 𝗌𝗈 𝖽𝖺𝗆𝗇 𝖻𝖾𝖺𝗎𝗍𝗂𝖿𝗎𝗅.", "𝖱𝗈𝗒 𝖬𝗎𝗌𝗍𝖺𝗇𝗀", "𝖥𝗎𝗅𝗅𝗆𝖾𝗍𝖺𝗅 𝖠𝗅𝖼𝗁𝖾𝗆𝗂𝗌𝗍: 𝖡𝗋𝗈𝗍𝗁𝖾𝗋𝗁𝗈𝗈𝖽"),
        ("𝖨𝖿 𝗇𝗈𝖻𝗈𝖽𝗒 𝖼𝖺𝗋𝖾𝗌 𝗍𝗈 𝖺𝖼𝖼𝖾𝗉𝗍 𝗒𝗈𝗎 𝖺𝗇𝖽 𝗐𝖺𝗇𝗍𝗌 𝗒𝗈𝗎 𝗂𝗇 𝗍𝗁𝗂𝗌 𝗐𝗈𝗋𝗅𝖽, 𝖺𝖼𝖼𝖾𝗉𝗍 𝗒𝗈𝗎𝗋𝗌𝖾𝗅𝖿 𝖺𝗇𝖽 𝗒𝗈𝗎 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝖽𝗈𝗇’𝗍 𝗇𝖾𝖾𝖽 𝗍𝗁𝖾𝗆 𝖺𝗇𝖽 𝗍𝗁𝖾𝗂𝗋 𝗌𝖾𝗅𝖿𝗂𝗌𝗁 𝗂𝖽𝖾𝖺𝗌.", "𝖦𝗂𝗇𝗍𝗈𝗄𝗂 𝖲𝖺𝗄𝖺𝗍𝖺", "𝖦𝗂𝗇𝗍𝖺𝗆𝖺"),
        ("𝖶𝗁𝖺𝗍𝖾𝗏𝖾𝗋 𝗒𝗈𝗎 𝖽𝗈, 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝖽𝗈 𝗂𝗍 𝗐𝗂𝗍𝗁 𝖺𝗅𝗅 𝗒𝗈𝗎𝗋 𝗁𝖾𝖺𝗋𝗍.", "𝖲𝖺𝖻𝖾𝗋 (𝖠𝗋𝗍𝗈𝗋𝗂𝖺 𝖯𝖾𝗇𝖽𝗋𝖺𝗀𝗈𝗇)", "𝖥𝖺𝗍𝖾/𝗌𝗍𝖺𝗒 𝗇𝗂𝗀𝗁𝗍: 𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖡𝗅𝖺𝖽𝖾 𝖶𝗈𝗋𝗄𝗌"),
        ("𝖤𝗏𝖾𝗇 𝗂𝖿 𝗍𝗁𝗂𝗇𝗀𝗌 𝖺𝗋𝖾 𝗉𝖺𝗂𝗇𝖿𝗎𝗅 𝖺𝗇𝖽 𝗍𝗈𝗎𝗀𝗁, 𝗉𝖾𝗈𝗉𝗅𝖾 𝗌𝗁𝗈𝗎𝗅𝖽 𝖺𝗉𝗉𝗋𝖾𝖼𝗂𝖺𝗍𝖾 𝗐𝗁𝖺𝗍 𝗂𝗍 𝗆𝖾𝖺𝗇𝗌 𝗍𝗈 𝖻𝖾 𝖺𝗅𝗂𝗏𝖾 𝖺𝗍 𝖺𝗅𝗅.", "𝖸𝖺𝗍𝗈", "𝖭𝗈𝗋𝖺𝗀𝖺𝗆𝗂"),
        ("𝖨'𝖽 𝗋𝖺𝗍𝗁𝖾𝗋 𝖽𝗂𝖾 𝗈𝗇 𝗆𝗒 𝖿𝖾𝖾𝗍 𝗍𝗁𝖺𝗇 𝗅𝗂𝗏𝖾 𝗈𝗇 𝗆𝗒 𝗄𝗇𝖾𝖾𝗌.", "𝖤𝗋𝖾𝗇 𝖸𝖾𝖺𝗀𝖾𝗋", "𝖠𝗍𝗍𝖺𝖼𝗄 𝗈𝗇 𝖳𝗂𝗍𝖺𝗇"),
        ("𝖨 𝖽𝗈𝗇'𝗍 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖼𝗈𝗇𝗊𝗎𝖾𝗋 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀. 𝖨 𝗃𝗎𝗌𝗍 𝗍𝗁𝗂𝗇𝗄 𝗍𝗁𝖾 𝗀𝗎𝗒 𝗐𝗂𝗍𝗁 𝗍𝗁𝖾 𝗆𝗈𝗌𝗍 𝖿𝗋𝖾𝖾𝖽𝗈𝗆 𝗂𝗇 𝗍𝗁𝗂𝗌 𝗐𝗁𝗈𝗅𝖾 𝗈𝖼𝖾𝖺𝗇... 𝗂𝗌 𝗍𝗁𝖾 𝖯𝗂𝗋𝖺𝗍𝖾 𝖪𝗂𝗇𝗀!", "𝖬𝗈𝗇𝗄𝖾𝗒 𝖣. 𝖫𝗎𝖿𝖿𝗒", "𝖮𝗇𝖾 𝖯𝗂𝖾𝖼𝖾"),
        ("𝖨𝗍'𝗌 𝗇𝗈𝗍 𝗍𝗁𝖾 𝗌𝗍𝗋𝖾𝗇𝗀𝗍𝗁 𝗈𝖿 𝖺 𝗁𝖾𝗋𝗈 𝗍𝗁𝖺𝗍 𝗆𝖺𝗍𝗍𝖾𝗋𝗌, 𝖻𝗎𝗍 𝗍𝗁𝖾 𝗌𝗍𝗋𝖾𝗇𝗀𝗍𝗁 𝗈𝖿 𝗍𝗁𝖾𝗂𝗋 𝗁𝖾𝖺𝗋𝗍.", "𝖭𝖺𝗍𝗌𝗎 𝖣𝗋𝖺𝗀𝗇𝖾𝖾𝗅", "𝖥𝖺𝗂𝗋𝗒 𝖳𝖺𝗂𝗅"),
        ("𝖳𝗁𝖾 𝗐𝗈𝗋𝗅𝖽 𝗂𝗌 𝗆𝖾𝗋𝖼𝗂𝗅𝖾𝗌𝗌, 𝖺𝗇𝖽 𝗂𝗍'𝗌 𝖺𝗅𝗌𝗈 𝗏𝖾𝗋𝗒 𝖻𝖾𝖺𝗎𝗍𝗂𝖿𝗎𝗅.", "𝖬𝗂𝗄𝖺𝗌𝖺 𝖠𝖼𝗄𝖾𝗋𝗆𝖺𝗇", "𝖠𝗍𝗍𝖺𝖼𝗄 𝗈𝗇 𝖳𝗂𝗍𝖺𝗇"),
        ("𝖭𝗈 𝗈𝗇𝖾 𝗄𝗇𝗈𝗐𝗌 𝗐𝗁𝖺𝗍 𝗍𝗁𝖾 𝖿𝗎𝗍𝗎𝗋𝖾 𝗁𝗈𝗅𝖽𝗌. 𝖳𝗁𝖺𝗍'𝗌 𝗐𝗁𝗒 𝗐𝖾 𝖼𝖺𝗇 𝗇𝖾𝗏𝖾𝗋 𝗌𝖺𝗒 𝗀𝗈𝗈𝖽𝖻𝗒𝖾.", "𝖨𝗌𝖺𝖺𝖼 𝖭𝖾𝗍𝖾𝗋𝗈", "𝖧𝗎𝗇𝗍𝖾𝗋 𝗑 𝖧𝗎𝗇𝗍𝖾𝗋"),
        ("𝖨𝖿 𝗒𝗈𝗎 𝗐𝖺𝗇𝗇𝖺 𝗆𝖺𝗄𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝖽𝗋𝖾𝖺𝗆, 𝗒𝗈𝗎'𝗏𝖾 𝗀𝗈𝗍𝗍𝖺 𝗌𝗍𝖺𝗋𝗍 𝖻𝗒 𝖻𝖾𝗅𝗂𝖾𝗏𝗂𝗇𝗀 𝗂𝗇 𝗍𝗁𝖺𝗍 𝖽𝗋𝖾𝖺𝗆 𝗒𝗈𝗎𝗋𝗌𝖾𝗅𝖿!", "𝖲𝗁𝗈𝗒𝗈 𝖧𝗂𝗇𝖺𝗍𝖺", "𝖧𝖺𝗂𝗄𝗒𝗎𝗎!!"),
        ("𝖡𝖾𝗂𝗇𝗀 𝗐𝖾𝖺𝗄 𝗂𝗌 𝗇𝗈𝗍𝗁𝗂𝗇𝗀 𝗍𝗈 𝖻𝖾 𝖺𝗌𝗁𝖺𝗆𝖾𝖽 𝗈𝖿. 𝖲𝗍𝖺𝗒𝗂𝗇𝗀 𝗐𝖾𝖺𝗄 𝗂𝗌.", "𝖨𝗓𝗎𝗄𝗎 𝖬𝗂𝖽𝗈𝗋𝗂𝗒𝖺", "𝖬𝗒 𝖧𝖾𝗋𝗈 𝖠𝖼𝖺𝖽𝖾𝗆𝗂𝖺"),
        ("𝖤𝗏𝖾𝗇 𝗂𝖿 𝗒𝗈𝗎’𝗋𝖾 𝗐𝖾𝖺𝗄, 𝗍𝗁𝖾𝗋𝖾 𝖺𝗋𝖾 𝗆𝗂𝗋𝖺𝖼𝗅𝖾𝗌 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗌𝖾𝗂𝗓𝖾 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗁𝖺𝗇𝖽𝗌 𝗂𝖿 𝗒𝗈𝗎 𝖿𝗂𝗀𝗁𝗍 𝗈𝗇 𝗍𝗈 𝗍𝗁𝖾 𝗏𝖾𝗋𝗒 𝖾𝗇𝖽.", "𝖦𝗈𝗇 𝖥𝗋𝖾𝖾𝖼𝗌𝗌", "𝖧𝗎𝗇𝗍𝖾𝗋 𝗑 𝖧𝗎𝗇𝗍𝖾𝗋"),
        ("𝖳𝗁𝖾𝗋𝖾 𝖺𝗋𝖾 𝗇𝗈 𝗌𝗁𝗈𝗋𝗍𝖼𝗎𝗍𝗌 𝗂𝗇 𝗅𝗂𝖿𝖾. 𝖳𝗈 𝗐𝗂𝗇, 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝗍𝗈 𝗐𝗈𝗋𝗄 𝗁𝖺𝗋𝖽, 𝖿𝖺𝖼𝖾 𝗒𝗈𝗎𝗋 𝖽𝖾𝗆𝗈𝗇𝗌, 𝖺𝗇𝖽 𝗇𝖾𝗏𝖾𝗋 𝗀𝗂𝗏𝖾 𝗎𝗉.", "𝖸𝖺𝗆𝗂 𝖲𝗎𝗄𝖾𝗁𝗂𝗋𝗈", "𝖡𝗅𝖺𝖼𝗄 𝖢𝗅𝗈𝗏𝖾𝗋"),
        ("𝖳𝗋𝗎𝖾 𝗌𝗍𝗋𝖾𝗇𝗀𝗍𝗁 𝖼𝗈𝗆𝖾𝗌 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗁𝖾𝖺𝗋𝗍, 𝗇𝗈𝗍 𝗃𝗎𝗌𝗍 𝖻𝗋𝗎𝗍𝖾 𝖿𝗈𝗋𝖼𝖾.", "𝖤𝖽𝗐𝖺𝗋𝖽 𝖤𝗅𝗋𝗂𝖼", "𝖥𝗎𝗅𝗅𝗆𝖾𝗍𝖺𝗅 𝖠𝗅𝖼𝗁𝖾𝗆𝗂𝗌𝗍"),
        ("𝖳𝗁𝖾 𝖿𝖾𝖺𝗋 𝗈𝖿 𝖽𝖾𝖺𝗍𝗁 𝖿𝗈𝗅𝗅𝗈𝗐𝗌 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖿𝖾𝖺𝗋 𝗈𝖿 𝗅𝗂𝖿𝖾. 𝖠 𝗆𝖺𝗇 𝗐𝗁𝗈 𝗅𝗂𝗏𝖾𝗌 𝖿𝗎𝗅𝗅𝗒 𝗂𝗌 𝗉𝗋𝖾𝗉𝖺𝗋𝖾𝖽 𝗍𝗈 𝖽𝗂𝖾 𝖺𝗍 𝖺𝗇𝗒 𝗍𝗂𝗆𝖾.", "𝖲𝗁𝗂𝗇𝗈𝖻𝗎 𝖲𝖾𝗇𝗌𝗎𝗂", "𝖸𝗎 𝖸𝗎 𝖧𝖺𝗄𝗎𝗌𝗁𝗈"),
        ("𝖨𝗇 𝗍𝗁𝗂𝗌 𝗐𝗈𝗋𝗅𝖽, 𝗐𝗁𝖾𝗋𝖾𝗏𝖾𝗋 𝗍𝗁𝖾𝗋𝖾 𝗂𝗌 𝗅𝗂𝗀𝗁𝗍 – 𝗍𝗁𝖾𝗋𝖾 𝖺𝗋𝖾 𝖺𝗅𝗌𝗈 𝗌𝗁𝖺𝖽𝗈𝗐𝗌. 𝖠𝗌 𝗅𝗈𝗇𝗀 𝖺𝗌 𝗍𝗁𝖾 𝖼𝗈𝗇𝖼𝖾𝗉𝗍 𝗈𝖿 𝗐𝗂𝗇𝗇𝖾𝗋𝗌 𝖾𝗑𝗂𝗌𝗍𝗌, 𝗍𝗁𝖾𝗋𝖾 𝗆𝗎𝗌𝗍 𝖺𝗅𝗌𝗈 𝖻𝖾 𝗅𝗈𝗌𝖾𝗋𝗌.", "𝖫𝖾𝗅𝗈𝗎𝖼𝗁 𝗏𝗂 𝖡𝗋𝗂𝗍𝖺𝗇𝗇𝗂𝖺", "𝖢𝗈𝖽𝖾 𝖦𝖾𝖺𝗌𝗌"),
        ("𝖨’𝖽 𝗋𝖺𝗍𝗁𝖾𝗋 𝗍𝗋𝗎𝗌𝗍 𝖺𝗇𝖽 𝗋𝖾𝗀𝗋𝖾𝗍 𝗍𝗁𝖺𝗇 𝖽𝗈𝗎𝖻𝗍 𝖺𝗇𝖽 𝗋𝖾𝗀𝗋𝖾𝗍.", "𝖪𝗂𝗋𝗂𝗍𝗌𝗎𝗀𝗎 𝖤𝗆𝗂𝗒𝖺", "𝖥𝖺𝗍𝖾/𝖹𝖾𝗋𝗈"),
        ("𝖸𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗇𝖾𝗏𝖾𝗋 𝗀𝗂𝗏𝖾 𝗎𝗉 𝗈𝗇 𝗅𝗂𝖿𝖾, 𝗇𝗈 𝗆𝖺𝗍𝗍𝖾𝗋 𝗁𝗈𝗐 𝗒𝗈𝗎 𝖿𝖾𝖾𝗅. 𝖭𝗈 𝗆𝖺𝗍𝗍𝖾𝗋 𝗁𝗈𝗐 𝗁𝖺𝗋𝖽 𝗍𝗁𝗂𝗇𝗀𝗌 𝗀𝖾𝗍, 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝗍𝗈 𝗁𝗈𝗅𝖽 𝗈𝗇 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗅𝗂𝖿𝖾, 𝗇𝗈 𝗆𝖺𝗍𝗍𝖾𝗋 𝗐𝗁𝖺𝗍.", "𝖬𝗂𝗌𝖺𝗄𝗂 𝖳𝖺𝗄𝖺𝗁𝖺𝗌𝗁𝗂", "𝖩𝗎𝗇𝗃𝗈𝗎 𝖱𝗈𝗆𝖺𝗇𝗍𝗂𝖼𝖺"),
        ("𝖳𝗁𝖾 𝗍𝗋𝗎𝖾 𝗆𝖾𝖺𝗌𝗎𝗋𝖾 𝗈𝖿 𝖺 𝗌𝗁𝗂𝗇𝗈𝖻𝗂 𝗂𝗌 𝗇𝗈𝗍 𝗁𝗈𝗐 𝗁𝖾 𝗅𝗂𝗏𝖾𝗌 𝖻𝗎𝗍 𝗁𝗈𝗐 𝗁𝖾 𝖽𝗂𝖾𝗌. 𝖨𝗍'𝗌 𝗇𝗈𝗍 𝗐𝗁𝖺𝗍 𝗍𝗁𝖾𝗒 𝖽𝗈 𝗂𝗇 𝗅𝗂𝖿𝖾, 𝖻𝗎𝗍 𝗐𝗁𝖺𝗍 𝗍𝗁𝖾𝗒 𝖽𝗂𝖽 𝖻𝖾𝖿𝗈𝗋𝖾 𝖽𝗒𝗂𝗇𝗀 𝗍𝗁𝖺𝗍 𝗉𝗋𝗈𝗏𝖾𝗌 𝗍𝗁𝖾𝗂𝗋 𝗐𝗈𝗋𝗍𝗁.", "𝖩𝗂𝗋𝖺𝗂𝗒𝖺", "𝖭𝖺𝗋𝗎𝗍𝗈"),
    ]

QUOTES_IMG = (
      "https://i.imgur.com/Iub4RYj.jpg", 
      "https://i.imgur.com/uvNMdIl.jpg", 
      "https://i.imgur.com/YOBOntg.jpg", 
      "https://i.imgur.com/fFpO2ZQ.jpg", 
      "https://i.imgur.com/f0xZceK.jpg", 
      "https://i.imgur.com/RlVcCip.jpg", 
      "https://i.imgur.com/CjpqLRF.jpg", 
      "https://i.imgur.com/8BHZDk6.jpg", 
      "https://i.imgur.com/8bHeMgy.jpg", 
      "https://i.imgur.com/5K3lMvr.jpg", 
      "https://i.imgur.com/NTzw4RN.jpg", 
      "https://i.imgur.com/wJxryAn.jpg", 
      "https://i.imgur.com/9L0DWzC.jpg", 
      "https://i.imgur.com/sBe8TTs.jpg", 
      "https://i.imgur.com/1Au8gdf.jpg", 
      "https://i.imgur.com/28hFQeU.jpg", 
      "https://i.imgur.com/Qvc03JY.jpg", 
      "https://i.imgur.com/gSX6Xlf.jpg", 
      "https://i.imgur.com/iP26Hwa.jpg", 
      "https://i.imgur.com/uSsJoX8.jpg", 
      "https://i.imgur.com/OvX3oHB.jpg", 
      "https://i.imgur.com/JMWuksm.jpg", 
      "https://i.imgur.com/lhM3fib.jpg", 
      "https://i.imgur.com/64IYKkw.jpg", 
      "https://i.imgur.com/nMbyA3J.jpg", 
      "https://i.imgur.com/7KFQhY3.jpg", 
      "https://i.imgur.com/mlKb7zt.jpg", 
      "https://i.imgur.com/JCQGJVw.jpg", 
      "https://i.imgur.com/hSFYDEz.jpg", 
      "https://i.imgur.com/PQRjAgl.jpg", 
      "https://i.imgur.com/ot9624U.jpg", 
      "https://i.imgur.com/iXmqN9y.jpg", 
      "https://i.imgur.com/RhNBeGr.jpg", 
      "https://i.imgur.com/tcMVNa8.jpg", 
      "https://i.imgur.com/LrVg810.jpg", 
      "https://i.imgur.com/TcWfQlz.jpg", 
      "https://i.imgur.com/muAUdvJ.jpg", 
      "https://i.imgur.com/AtC7ZRV.jpg", 
      "https://i.imgur.com/sCObQCQ.jpg", 
      "https://i.imgur.com/AJFDI1r.jpg", 
      "https://i.imgur.com/TCgmRrH.jpg", 
      "https://i.imgur.com/LMdmhJU.jpg", 
      "https://i.imgur.com/eyyax0N.jpg", 
      "https://i.imgur.com/YtYxV66.jpg", 
      "https://i.imgur.com/292w4ye.jpg", 
      "https://i.imgur.com/6Fm1vdw.jpg", 
      "https://i.imgur.com/2vnBOZd.jpg", 
      "https://i.imgur.com/j5hI9Eb.jpg", 
      "https://i.imgur.com/cAv7pJB.jpg", 
      "https://i.imgur.com/jvI7Vil.jpg", 
      "https://i.imgur.com/fANpjsg.jpg", 
      "https://i.imgur.com/5o1SJyo.jpg", 
      "https://i.imgur.com/dSVxmh8.jpg", 
      "https://i.imgur.com/02dXlAD.jpg", 
      "https://i.imgur.com/htvIoGY.jpg", 
      "https://i.imgur.com/hy6BXOj.jpg", 
      "https://i.imgur.com/OuwzNYu.jpg", 
      "https://i.imgur.com/L8vwvc2.jpg", 
      "https://i.imgur.com/3VMVF9y.jpg", 
      "https://i.imgur.com/yzjq2n2.jpg", 
      "https://i.imgur.com/0qK7TAN.jpg", 
      "https://i.imgur.com/zvcxSOX.jpg", 
      "https://i.imgur.com/FO7bApW.jpg", 
      "https://i.imgur.com/KK06gwg.jpg", 
      "https://i.imgur.com/6lG4tsO.jpg"
      
      )



KISS_IMAGES = [
    "https://telegra.ph/file/479d9643cdff17a15ec05.jpg",
    "https://telegra.ph/file/0b7ba6fe6d34d896ff03e.jpg",
    "https://telegra.ph/file/1af93fcf1df1f55cd920d.jpg",
    "https://telegra.ph/file/5ae54df45294ef493cfee.jpg",
    "https://telegra.ph/file/b4efc98b62517c522057a.jpg",
    "https://telegra.ph/file/065ef5f65520e10aa7e53.jpg",
    "https://telegra.ph/file/40304f44aa391b6e4ac2f.jpg",
    "https://telegra.ph/file/8a9e88bbc24ed4d5c31cb.jpg",
    "https://telegra.ph/file/754217791a49d70b612a8.jpg",
    "https://telegra.ph/file/af2ea2cfdf50f35ea9c95.jpg"
]




HUG_IMAGES = [
    "https://telegra.ph/file/573ae1b6308ab1e79d111.jpg",
    "https://telegra.ph/file/259e556d9c66b04e47a91.jpg",
    "https://telegra.ph/file/e92f3e4e61805f0eef333.jpg",
    "https://telegra.ph/file/5019c3ed7b5b1836f390c.jpg",
    "https://telegra.ph/file/63f2f028325c21c5c58bd.jpg",
    "https://telegra.ph/file/72b03add03b5cdf36b7a3.jpg",
    "https://telegra.ph/file/5b9375739cb3badc8c603.jpg",
    "https://telegra.ph/file/98ac67d87257fb05db3c0.jpg"
]


KILL_IMAGES = [
    "https://telegra.ph/file/b5b092964071dce42c4ee.jpg",
    "https://telegra.ph/file/c490a4fa660bf027ded48.jpg",
    "https://telegra.ph/file/9d219ac386c790f0fc450.jpg",
    "https://telegra.ph/file/6d663cf17296e4180e9ef.jpg",
    "https://telegra.ph/file/14186accf4f258947a3ca.jpg",
    "https://telegra.ph/file/e1f1047041dcedee375e4.jpg"
]


PAT_IMAGES = [
    "https://telegra.ph/file/c7bdefb24ec556e62313b.jpg",
    "https://telegra.ph/file/115aabb36802273b61452.jpg",
    "https://telegra.ph/file/be5ee39e4293bb43d4b0f.jpg",
    "https://telegra.ph/file/86cf02142fa9d912b1c8d.jpg"
]


SLAP_IMAGES = [
    "https://telegra.ph/file/b36d571ffa6429dbca442.jpg",
    "https://telegra.ph/file/2429404d2fc99bb806916.jpg",
    "https://telegra.ph/file/81a02558b28630fb7af18.jpg",
    "https://telegra.ph/file/c4381aa42b671abe040ec.jpg",
    "https://telegra.ph/file/a72a074316557830bb2b4.jpg",
    "https://telegra.ph/file/f4f2c58c9a81427e39823.jpg",
    "https://telegra.ph/file/d93dbc5c1a54bf10baafd.jpg"
    "https://telegra.ph/file/69ff335b3b56673e854fa.jpg",
    "https://telegra.ph/file/4d7a4ebbcc158609660d1.jpg",
    "https://telegra.ph/file/4a59d2aa067b2fbd111d7.jpg"
]




KICK_IMAGES = [
    "https://telegra.ph/file/84b1a67e223d08af9c9e3.jpg",
    "https://telegra.ph/file/2fe473dca6d5007668c7b.jpg",
    "https://telegra.ph/file/e07d1eb24320ab09eb6e1.jpg",
    "https://telegra.ph/file/ef141e3ccbf28017becaa.jpg",
    "https://telegra.ph/file/0b0a6ffce2e89346662dc.jpg",
    "https://telegra.ph/file/7888cc2f1957713fd0251.jpg",
    "https://telegra.ph/file/7c7211f6ca1223af1b266.jpg"
]


SEX_IMAGES = [
    "https://telegra.ph/file/abf97c9e210194c0e7783.jpg",
    "https://telegra.ph/file/553ad70811376ca0ee4ac.jpg",
    "https://telegra.ph/file/a8f962ca727fcd50506d5.jpg",
    "https://telegra.ph/file/5c5a0c3b493446f0c6053.jpg",
    "https://telegra.ph/file/1a2d756aed07681cb7d2f.jpg",
    "https://telegra.ph/file/77a718f6ddfa22bd32143.jpg",
    "https://telegra.ph/file/7630c06e66b2a275070c9.jpg"
]



# BOT/imgs_config.py

wish_videos = [
    "https://telegra.ph/file/5ca6ddfc49b49fae534da.mp4",
    "https://telegra.ph/file/67e9ed91b66af0dbdbb66.mp4",
    # Add more URLs as needed
]



start_images = [
    "https://telegra.ph/file/332d73be0d9ed89530032.jpg",
    "https://telegra.ph/file/d2ce98708c451b2ab8f4a.jpg",
    "https://telegra.ph/file/88e49e34c67873e694139.jpg",
    "https://telegra.ph/file/562a3c15e21c9c512890c.jpg",
    "https://telegra.ph/file/6eb934b77964cb96f395f.jpg",
    "https://telegra.ph/file/36d7bbab59d2b77c7e922.jpg"
]



def get_random_start_image():
    return random.choice(start_images)

help_command_urls = [
    "https://telegra.ph/file/b63efe1a43972d3db956c.jpg",
    "https://telegra.ph/file/2750d60babc3b2adb7f03.jpg",
    "https://telegra.ph/file/58ccd2638f5c477f2811d.jpg",
    "https://telegra.ph/file/98158d0a330af3e8f5d3c.jpg",
    "https://telegra.ph/file/f3a1f73bf656e30eb9a9e.jpg"
]


COUPLES_PIC = "https://telegra.ph/file/be5cb972c39697f81516f.jpg"


sticker_ids = [
    "CAACAgUAAxkBAAJlFWaRIJsd4mZ0ns4ba7CpeX7ETsjoAALtCQACiUtRVUqlp8SMQZaXNQQ",
    "CAACAgUAAxkBAAJlG2aRIKeC0hGnTIH42l-gkHqw2UHsAAIeDgACzTC4VLzNdy59xsACNQQ",
    "CAACAgUAAxkBAAJlHmaRIKrvH-3RznLIUSNG7_z31RWNAAKMDwACWD2xVO___iq4xCYWNQQ",
    "CAACAgUAAxkBAAJlIWaRIKwnVL92sexLAeLC92EryGWMAAKBDAACSMW4VHbzmvYsOHe1NQQ",
    "CAACAgUAAxkBAAJlJGaRIK4OhdWMlIPxv6sajcVlxQhvAAKSCwACW05QVTxKSZP_WBk4NQQ",
    "CAACAgUAAxkBAAJlJ2aRIK-RAwNazT6EVHhztwKKbqyKAAJtCwACKmpJVSJnkH4nUIrNNQQ"
]

# Mapping Telegram commands to API categories
command_to_category = {
    "waifus": "waifu",
    "kickk": "kick",
    # Direct mappings for other categories
    "neko": "neko",
    "shinobu": "shinobu",
    "megumin": "megumin",
    "bully": "bully",
    "cuddle": "cuddle",
    "cry": "cry",
    "hug": "hug",
    "awoo": "awoo",
    "kiss": "kiss",
    "lick": "lick",
    "pat": "pat",
    "smug": "smug",
    "bonk": "bonk",
    "yeet": "yeet",
    "blush": "blush",
    "smile": "smile",
    "wave": "wave",
    "highfive": "highfive",
    "handhold": "handhold",
    "nom": "nom",
    "bite": "bite",
    "glomp": "glomp",
    "slap": "slap",
    "kill": "kill",
    "happy": "happy",
    "wink": "wink",
    "poke": "poke",
    "dance": "dance",
    "cringe": "cringe",
}
LOGO_LINKS = [
    "https://telegra.ph/file/d1838efdafce9fe611d0c.jpg",
    "https://telegra.ph/file/c1ff2d5ec5e1b5bd1b200.jpg",
    "https://telegra.ph/file/08c5fbe14cc4b13d1de05.jpg",
    "https://telegra.ph/file/66614a049d74fe2a220dc.jpg",
    "https://telegra.ph/file/9cc1e4b24bfa13873bd66.jpg",
    "https://telegra.ph/file/792d38bd74b0c3165c11d.jpg",
    "https://telegra.ph/file/e1031e28a4aa4d8bd7c9b.jpg",
    "https://telegra.ph/file/2be9027c55b5ed463fc18.jpg",
    "https://telegra.ph/file/9fd71f8d08158d0cc393c.jpg",
    "https://telegra.ph/file/627105074f0456f42058b.jpg",
    "https://telegra.ph/file/62b712f741382d3c171cd.jpg",
    "https://telegra.ph/file/496651e0d5e4d22b8f72d.jpg",
    "https://telegra.ph/file/6619d0eee2c35e022ee74.jpg",
    "https://telegra.ph/file/f72fcb27c9b1e762d184b.jpg",
    "https://telegra.ph/file/01eac0fe1a722a864d7de.jpg",
    "https://telegra.ph/file/bdcb746fbfdf38f812873.jpg",
    "https://telegra.ph/file/d13e036a129df90651deb.jpg",
    "https://telegra.ph/file/ab6715ce9a63523bd0219.jpg",
    "https://telegra.ph/file/c243f4e80ebf0110f9f00.jpg",
    "https://telegra.ph/file/ff9053f2c7bfb2badc99e.jpg",
    "https://telegra.ph/file/00b9ebbb816285d9a59f9.jpg",
    "https://telegra.ph/file/ad92e1c829d14afa25cf2.jpg",
    "https://telegra.ph/file/58d45cc3374e7b28a1e67.jpg",
    "https://telegra.ph/file/4140a0b3f27c302fd81cb.jpg",
    "https://telegra.ph/file/c4db2b5c84c1d90f5ac8a.jpg",
    "https://telegra.ph/file/c0da5080a3ff7643ddeb4.jpg",
    "https://telegra.ph/file/79fad473ffe888ed771b2.jpg",
    "https://telegra.ph/file/eafd526d9dcc164d7269f.jpg",
    "https://telegra.ph/file/98b50e8424dd2be9fc127.jpg",
    "https://telegra.ph/file/c1ad29c189162a1404749.jpg",
    "https://telegra.ph/file/2d288450ebecc500addbd.jpg",
    "https://telegra.ph/file/9715353976a99becd7632.jpg",
    "https://telegra.ph/file/87670b02a1004bc02bd8d.jpg",
    "https://telegra.ph/file/70789cd69114939a78242.jpg",
    "https://telegra.ph/file/1566bd334f00645cfa993.jpg",
    "https://telegra.ph/file/9727c37bb8c633208b915.jpg",
    "https://telegra.ph/file/27467ef55fab117ccb278.jpg",
    "https://telegra.ph/file/b9c62ff7810d9e84e9e2c.jpg",
    "https://telegra.ph/file/87d22f2c95413059dda4e.jpg",
    "https://telegra.ph/file/e528a731accbcdea140e3.jpg",
    "https://telegra.ph/file/ee3f20c3ce71dc37fecb2.jpg",
    "https://telegra.ph/file/a049f78377a5b8257294d.jpg",
    "https://telegra.ph/file/54d22d39ea89423b7533f.jpg",
    "https://telegra.ph/file/d90baa59b6fe2bc3091d3.jpg",
    "https://telegra.ph/file/b9b3f80dc4635faaeb472.jpg",
    "https://telegra.ph/file/d64be0a98f441a33d2aef.jpg",
    "https://telegra.ph/file/e2c59ac97a900bab5ad7d.jpg",
    "https://telegra.ph/file/41baf461b0a34f1a881a9.jpg",
    "https://telegra.ph/file/8d4082052b4bd0a8cc862.jpg",
    "https://telegra.ph/file/e7d6e0c511137ad67d843.jpg",
    "https://telegra.ph/file/d7b97ea806d4a905b71c4.jpg",
    "https://telegra.ph/file/6bec48ea2c96cf3d668a4.jpg",
    "https://telegra.ph/file/aa64389b70e0de02d18c5.jpg",
    "https://telegra.ph/file/2f75d964a59a3a4ae90e0.jpg",
    "https://telegra.ph/file/f408df72c57cfc05e734f.jpg",
    "https://telegra.ph/file/9d88d9dfb50106bc43c91.jpg",
    "https://telegra.ph/file/a5a6e0f9d172fa386621e.jpg",
    "https://telegra.ph/file/b0fc771c91409ee5cd4dc.jpg",
    "https://telegra.ph/file/b0fc771c91409ee5cd4dc.jpg",
    "https://telegra.ph/file/f75e59ebd4059f394479e.jpg",
    "https://telegra.ph/file/fc0308f59023d0c997166.jpg",
    "https://telegra.ph/file/7e1c04947f6afb6cdf25c.jpg",
    "https://telegra.ph/file/6279bb4be7e48da194353.jpg",
    "https://telegra.ph/file/616784fcd89f13e789685.jpg",
    "https://telegra.ph/file/803e7dd9fafdb086bce4a.jpg",
    "https://telegra.ph/file/d7338861b7f996ec9d40d.jpg",
    "https://telegra.ph/file/828730cd4d73333eaf129.jpg",
    "https://telegra.ph/file/36c9321161d49c4b3d671.jpg",
    "https://telegra.ph/file/ebeae90b99fe482d11784.jpg",
    "https://telegra.ph/file/70f38f92fe8d3060a31e4.jpg",
    "https://telegra.ph/file/db12cf905f557487abc60.jpg",
    "https://telegra.ph/file/0f9be531164c927ded8ec.jpg",
    "https://telegra.ph/file/57fb7a6df3d666878c6f3.jpg",
    "https://telegra.ph/file/242930d9f7aaa0b0729fd.jpg",
    "https://telegra.ph/file/883f255792d2c2ebdd5f5.jpg",
    "https://telegra.ph/file/36a9c0c26967edf90d42d.jpg",
    "https://telegra.ph/file/03bdaf253c43fc97adbbe.jpg",
    "https://telegra.ph/file/5826715ff0895a5321d2d.jpg",
    "https://telegra.ph/file/74807bfbc85057899ea8d.png",
    "https://telegra.ph/file/e390f7531557c12379acb.jpg",
    "https://telegra.ph/file/0b83432e72bb0ce0ed0f1.jpg",
    "https://telegra.ph/file/23276d7f831611e347a7c.jpg",
    "https://telegra.ph/file/109789c7dcc615c6731fa.jpg",
    "https://telegra.ph/file/127ef2c311b42b2dbfb62.jpg",
    "https://telegra.ph/file/bfd7fcd13b2c353030ef0.jpg",
    "https://telegra.ph/file/0f7773c27b1379e2f3bea.jpg",
    "https://telegra.ph/file/4606e5c76a4a6c893a721.png",
    "https://telegra.ph/file/f46c4569d77d9a6be6aed.jpg",
    "https://telegra.ph/file/2b4718637a7396e3b23d9.jpg",
    "https://telegra.ph/file/40bce3c8e8ae3cd0198b9.jpg",
    "https://telegra.ph/file/ac61cfac3290ed635f8cc.jpg",
    "https://telegra.ph/file/55313171c70692e838451.jpg",
    "https://telegra.ph/file/f503ce00794cadbdacdd2.jpg",
    "https://telegra.ph/file/2153d9fad3613041fcd28.jpg",
    "https://telegra.ph/file/6a7a790fe964c8c264b61.jpg",
    "https://telegra.ph/file/103d2f4b7b1088890ae24.jpg",
    "https://telegra.ph/file/63501bb4f1de53a81dba1.jpg",
    "https://telegra.ph/file/00fdb4e3a06a6f6e81c35.jpg",
    "https://telegra.ph/file/e2fbfce637048d2e042da.jpg",
    "https://telegra.ph/file/29d3c7c297c40a17cde4b.jpg",
    "https://telegra.ph/file/97c7aa91c51f72f82c2d9.jpg",
    "https://telegra.ph/file/0096988891ba9b884d2dd.jpg",
    "https://telegra.ph/file/12cb5cb6512b754deb92d.jpg",
    "https://telegra.ph/file/38387c8384879e0ddb803.jpg",
    "https://telegra.ph/file/3353253a27522219cc1ce.jpg",
    "https://telegra.ph/file/daae7def66cb1d1aefa23.jpg",
    "https://telegra.ph/file/e5fe618ad651777061c54.jpg",
    "https://telegra.ph/file/3c56aa160ec242b1670eb.jpg",
    "https://telegra.ph/file/0794ddfefdc770646c478.jpg",
    "https://telegra.ph/file/05bc05a4b878e54ed3b20.jpg",
    "https://telegra.ph/file/ef7ffbd3839645e33a0ec.jpg",
    "https://telegra.ph/file/1daa50b9d3e26a5509cc2.png",
    "https://telegra.ph/file/510600a5b93d83ce048f3.jpg",
    "https://telegra.ph/file/0ede8bd4788327111ecbf.jpg",
    "https://telegra.ph/file/e9f546797e42e821a91e1.jpg",
    "https://telegra.ph/file/fc7fbefe92599bd79d038.jpg",
    "https://telegra.ph/file/b88d6e78e206eb73e2e54.jpg",
    "https://telegra.ph/file/48f8c62829953e82441e8.jpg",
    "https://telegra.ph/file/56f7b34cae98a491e2b35.jpg",
    "https://telegra.ph/file/9c23b4302926d40c46e12.jpg",
    "https://telegra.ph/file/9bf850ea98a2b252ff233.jpg",
    "https://telegra.ph/file/e764f0b3e2ecc56167803.jpg",
    "https://telegra.ph/file/289f9cebe37f31a943f98.jpg",
    "https://telegra.ph/file/0c647be0f5a48d576d692.jpg",
    "https://telegra.ph/file/41c5b44c4f5978828b5b5.jpg",
    "https://telegra.ph/file/9cdce279bdf240a933c14.jpg",
    "https://telegra.ph/file/f20424687f94e9c285133.jpg",
    "https://telegra.ph/file/e7858eb025e1ddb2f6267.jpg",
    "https://telegra.ph/file/3e984aa5ab96df166f2a4.jpg",
    "https://telegra.ph/file/e43e28aa952eaee6a5315.jpg",
    "https://telegra.ph/file/6d222dcaf9ba1072c6062.jpg",
    "https://telegra.ph/file/21e696bbefcfe39c6e74e.jpg",
    "https://telegra.ph/file/64ec61e41da3d4aded33d.jpg",
    "https://telegra.ph/file/5b1d8766504ff75c1bd1f.jpg",
    "https://telegra.ph/file/731879a344b3b49fe51bd.jpg",
    "https://telegra.ph/file/6221afc84b357ed0d1fc5.jpg",
    "https://telegra.ph/file/499bb1117771d8c020038.jpg",
    "https://telegra.ph/file/2690d73bc32cfdb986629.jpg",
    "https://telegra.ph/file/21255de971701b9df0902.jpg",
    "https://telegra.ph/file/434a35e7fe5e2c000c598.jpg",
    "https://telegra.ph/file/22a5d3621aba0b370d0b6.png",
    "https://telegra.ph/file/ae31845d1df2c4a84915b.png",
    "https://telegra.ph/file/ae2b809c8d11e7fa4121d.png",
    "https://telegra.ph/file/ccb7f3113994d5d2b26f6.png",
    "https://telegra.ph/file/5e53f0257ff12a7b0737a.png",
    "https://telegra.ph/file/a613600a9f9f8ee29f0f7.jpg",
    "https://telegra.ph/file/129c14fada1a8c0b151f5.jpg",
    "https://telegra.ph/file/c7552ed4246ccd8efd301.jpg",
    "https://telegra.ph/file/e794f772243d46467bcce.jpg",
    "https://telegra.ph/file/b6c43b9bd63f5f764d60b.jpg",
    "https://telegra.ph/file/11585459a3950de7f307c.png",
    "https://telegra.ph/file/37cde08802c3cea25a03f.jpg",
    "https://telegra.ph/file/d8d2db623223dee65963e.png",
    "https://telegra.ph/file/b7229017ffee2d814c646.jpg",
    "https://telegra.ph/file/65630efca60bfbdf84bc9.jpg",
    "https://telegra.ph/file/b8ce571c2f66a7c7070e5.jpg",
    "https://telegra.ph/file/a39f63f61f143ec00f19f.jpg",
    "https://telegra.ph/file/f7d946d8caaa21bf96dbf.jpg",
    "https://telegra.ph/file/9e4bef8ae0725d6b62108.png",
    "https://telegra.ph/file/3550089b22f3c8f506226.jpg",
    "https://telegra.ph/file/4275a4d4d6d433406b5fa.jpg",
    "https://telegra.ph/file/c476583ff55e1947461ad.jpg",
    "https://telegra.ph/file/87d2e5c0170ead00a2bc2.jpg",
    "https://telegra.ph/file/5027dd7379cc432c06e73.jpg",
    "https://telegra.ph/file/9e447fcaf3c66ddefb603.jpg",
    "https://telegra.ph/file/e5375f8233bea4f74b0f8.jpg",
    "https://telegra.ph/file/a1297510a64733cc5845f.jpg",
    "https://telegra.ph/file/ff04b594b699ce72316d7.jpg",
    "https://telegra.ph/file/093836a52cb166f161819.jpg",
    "https://telegra.ph/file/1e64bae43ca10d628ff6d.jpg",
    "https://telegra.ph/file/678ff9bb3405158a9155e.jpg",
    "https://telegra.ph/file/ab332ced3f63b96c375c5.jpg",
    "https://telegra.ph/file/a736d6cac93294c323303.jpg",
    "https://telegra.ph/file/dce8565bf7742f3d7122b.jpg",
    "https://telegra.ph/file/3f97672eb7b50426d15ff.jpg",
    "https://telegra.ph/file/19c6250369f8588a169c7.jpg",
    "https://telegra.ph/file/13d53b03a48448156564c.jpg",
    "https://telegra.ph/file/d21ff0d35553890e8cf34.jpg",
    "https://telegra.ph/file/a5e4cb43178642ba3709d.jpg",
    "https://telegra.ph/file/ecf108d25a6f5f56f91f4.jpg",
    "https://telegra.ph/file/8bd2b561b4c1f7164f934.png",
    "https://telegra.ph/file/7717658e6930c8196a904.jpg",
    "https://telegra.ph/file/dc85d43c4fc5062de7274.jpg",
    "https://telegra.ph/file/ff05c19f228ab2ed3d39d.jpg",
    "https://telegra.ph/file/ff05c19f228ab2ed3d39d.jpg",
    "https://telegra.ph/file/0d686bfffcb92a2fbdb0f.jpg",
    "https://telegra.ph/file/0d686bfffcb92a2fbdb0f.jpg",
    "https://telegra.ph/file/cdc66f16fbfb75971df2f.jpg",
    "https://telegra.ph/file/5c575892b9f9534fd4f31.jpg",
    "https://telegra.ph/file/78ffc400d4f3236b00e6b.jpg",
    "https://telegra.ph/file/89d32e5bbf084a376c803.jpg",
    "https://telegra.ph/file/b5d7dbcdce241013a061b.jpg",
    "https://telegra.ph/file/c1d228bc1859213d258d7.jpg",
    "https://telegra.ph/file/c6b0720b9f765809ea20a.jpg",
    "https://telegra.ph/file/df7e648f2e68ff8e1a1e6.jpg",
    "https://telegra.ph/file/5148f764cbc4700519909.jpg",
    "https://telegra.ph/file/479e7f51c682dcd1f013f.jpg",
    "https://telegra.ph/file/54a9eb0afe7a0f9c7c2f3.jpg",
    "https://telegra.ph/file/73c52ee54567a61dac47a.jpg",
    "https://telegra.ph/file/1427dbba81bd21b1bfc56.jpg",
    "https://telegra.ph/file/1427dbba81bd21b1bfc56.jpg",
    "https://telegra.ph/file/b0816374b470a5f9c66a6.jpg",
    "https://telegra.ph/file/e10840ec9bea9bbfaff0e.jpg",
    "https://telegra.ph/file/5935275d3ee09bc5a47b8.png",
    "https://telegra.ph/file/c27e64f1e8ece187c8161.jpg",
    "https://telegra.ph/file/055e9af8500ab92755358.jpg",
    "https://telegra.ph/file/f18f71167f9318ea28571.jpg",
    "https://telegra.ph/file/e2e26f252a5e25a1563c5.jpg",
    "https://telegra.ph/file/47ccb13820d6fc54d872b.jpg",
    "https://telegra.ph/file/f2ddccd28ceaeae90b2a3.jpg",
    "https://telegra.ph/file/951c872f7f8d551995652.jpg",
    "https://telegra.ph/file/8e8842f9fe207b8abd951.jpg",
    "https://telegra.ph/file/8a14ecd2347ef88e81201.jpg",
    "https://telegra.ph/file/b3869374ce0af9f26f92a.jpg",
    "https://telegra.ph/file/8e17f8d3633a5696a1ccf.jpg",
    "https://telegra.ph/file/b29d8956ae249773b0ec7.png",
    "https://telegra.ph/file/d0eebe724b67d2ef7647e.jpg",
    "https://telegra.ph/file/5780b3273162d2b9ba9ec.jpg",
    "https://telegra.ph/file/e2d56d5dbb108ba7af20c.jpg",
    "https://telegra.ph/file/1a4f50dd1e4ec9f04bfa1.jpg",
    "https://telegra.ph/file/99b56305fa9c50767f574.jpg",
    "https://telegra.ph/file/0859e0104c671bc9b6b7d.jpg",
    "https://telegra.ph/file/b3af2980caf7040702171.jpg",
    "https://telegra.ph/file/14be160df3b84c59e268e.jpg",
    "https://telegra.ph/file/b958155e1e8e9ab9a0416.jpg",
    "https://telegra.ph/file/24fff051c39b815e5078a.jpg",
    "https://telegra.ph/file/258c02c002e89287d5d9b.jpg",
    "https://telegra.ph/file/d2abc99773a9d4954c2ba.jpg",
    "https://telegra.ph/file/9849b3940f063b065f4e3.jpg",
]

emojis = [
    "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🦁", "🐯", "🐨", "🐼", 
    "🐸", "🐵", "🐔", "🐧", "🦅", "🦆", "🦢", "🦉", "🦇", "🐺", "🐗", 
    "🐴", "🦄", "🐝", "🐞", "🐜", "🦋", "🐌", "🐚", "🦗", "🐙", "🦑", 
    "🐋", "🐬", "🐟", "🦈", "🦓", "🦒", "🐓", "🦃", "🐧", "🐦", "🦩", 
    "🦻", "🦦", "🦥", "🐍", "🦎", "🐢", "🐍", "🦒", "🦘", "🦛", "🐘", 
    "🦣", "🐆", "🦓", "🦡", "🦦", "🐆", "🐅", "🐂", "🐃", "🦄", "🐄"
]


GIF = (
    "https://telegra.ph/file/ef94f2f61aa4d9394ef23.mp4",
    "https://telegra.ph/file/b82442bf9ebc32534f7a2.mp4",
    "https://telegra.ph/file/70d43e136125f9c120d2e.mp4",
    "https://telegra.ph/file/45354d3e42982f8de78f4.mp4",
    "https://telegra.ph/file/a22a0930f069686a0c4ef.mp4",
)

ITEMS = (
    "𝖼𝖺𝗌𝗍 𝗂𝗋𝗈𝗇 𝗌𝗄𝗂𝗅𝗅𝖾𝗍",
    "𝖺𝗇𝗀𝗋𝗒 𝗆𝖾𝗈𝗐",
    "𝖼𝗋𝗂𝖼𝗄𝖾𝗍 𝖻𝖺𝗍",
    "𝗐𝗈𝗈𝖽𝖾𝗇 𝖼𝖺𝗇𝖾",
    "𝗌𝗁𝗈𝗏𝖾𝗅",
    "𝗍𝗈𝖺𝗌𝗍𝖾𝗋",
    "𝖻𝗈𝗈𝗄",
    "𝗅𝖺𝗉𝗍𝗈𝗉",
    "𝗋𝗎𝖻𝖻𝖾𝗋 𝖼𝗁𝗂𝖼𝗄𝖾𝗇",
    "𝗌𝗉𝗂𝗄𝖾𝖽 𝖻𝖺𝗍",
    "𝗁𝖾𝖺𝗏𝗒 𝗋𝗈𝖼𝗄",
    "𝖼𝗁𝗎𝗇𝗄 𝗈𝖿 𝖽𝗂𝗋𝗍",
    "𝗍𝗈𝗇 𝗈𝖿 𝖻𝗋𝗂𝖼𝗄𝗌",
    "𝗋𝖺𝗌𝖾𝗇𝗀𝖺𝗇",
    "𝗌𝗉𝗂𝗋𝗂𝗍 𝖻𝗈𝗆𝖻",
    "𝟣𝟢𝟢-𝖳𝗒𝗉𝖾 𝖦𝗎𝖺𝗇𝗒𝗂𝗇 𝖡𝗈𝖽𝗁𝗂𝗌𝖺𝗍𝗍𝗏𝖺",
    "𝗋𝖺𝗌𝖾𝗇𝗌𝗁𝗎𝗋𝗂𝗄𝖾𝗇",
    "𝖬𝗎𝗋𝖺𝗌𝖺𝗆𝖾",
    "𝖻𝖺𝗇",
    "𝖼𝗁𝗎𝗇𝖼𝗁𝗎𝗇𝗆𝖺𝗋𝗎",
    "𝖪𝗎𝖻𝗂𝗄𝗂𝗋𝗂𝖻ō𝖼𝗁ō",
    "𝗋𝖺𝗌𝖾𝗇𝗀𝖺𝗇",
    "𝗌𝗉𝗁𝖾𝗋𝗂𝖼𝖺𝗅 𝖿𝗅𝗒𝗂𝗇𝗀 𝗄𝖺𝗍",
)

THROW = (
    "𝗍𝗁𝗋𝗈𝗐𝗌",
    "𝖿𝗅𝗂𝗇𝗀𝗌",
    "𝖼𝗁𝗎𝖼𝗄𝗌",
    "𝗁𝗎𝗋𝗅𝗌",
)

HIT = (
    "𝗁𝗂𝗍𝗌",
    "𝗐𝗁𝖺𝖼𝗄𝗌",
    "𝗌𝗅𝖺𝗉𝗌",
    "𝗌𝗆𝖺𝖼𝗄𝗌",
    "𝖻𝖺𝗌𝗁𝖾𝗌",
    "𝗉𝖺𝗍𝗌",
)

EYES = [
    ["⌐■", "■"],
    [" ͠°", " °"],
    ["⇀", "↼"],
    ["´• ", " •`"],
    ["´", "`"],
    ["`", "´"],
    ["ó", "ò"],
    ["ò", "ó"],
    ["⸌", "⸍"],
    [">", "<"],
    ["Ƹ̵̡", "Ʒ"],
    ["ᗒ", "ᗕ"],
    ["⟃", "⟄"],
    ["⪧", "⪦"],
    ["⪦", "⪧"],
    ["⪩", "⪨"],
    ["⪨", "⪩"],
    ["⪰", "⪯"],
    ["⫑", "⫒"],
    ["⨴", "⨵"],
    ["⩿", "⪀"],
    ["⩾", "⩽"],
    ["⩺", "⩹"],
    ["⩹", "⩺"],
    ["◥▶", "◀◤"],
    ["◍", "◎"],
    ["/͠-", "┐͡-\\"],
    ["⌣", "⌣”"],
    [" ͡⎚", " ͡⎚"],
    ["≋"],
    ["૦ઁ"],
    ["  ͯ"],
    ["  ͌"],
    ["ළ"],
    ["◉"],
    ["☉"],
    ["・"],
    ["▰"],
    ["ᵔ"],
    [" ﾟ"],
    ["□"],
    ["☼"],
    ["*"],
    ["`"],
    ["⚆"],
    ["⊜"],
    [">"],
    ["❍"],
    ["￣"],
    ["─"],
    ["✿"],
    ["•"],
    ["T"],
    ["^"],
    ["ⱺ"],
    ["@"],
    ["ȍ"],
    ["  "],
    ["  "],
    ["x"],
    ["-"],
    ["$"],
    ["Ȍ"],
    ["ʘ"],
    ["Ꝋ"],
    [""],
    ["⸟"],
    ["๏"],
    ["ⴲ"],
    ["◕"],
    ["◔"],
    ["✧"],
    ["■"],
    ["♥"],
    [" ͡°"],
    ["¬"],
    [" º "],
    ["⨶"],
    ["⨱"],
    ["⏓"],
    ["⏒"],
    ["⍜"],
    ["⍤"],
    ["ᚖ"],
    ["ᴗ"],
    ["ಠ"],
    ["σ"],
    ["☯"],
]

MOUTHS = [
    ["v"],
    ["ᴥ"],
    ["ᗝ"],
    ["Ѡ"],
    ["ᗜ"],
    ["Ꮂ"],
    ["ᨓ"],
    ["ᨎ"],
    ["ヮ"],
    ["╭͜ʖ╮"],
    [" ͟ل͜"],
    [" ͜ʖ"],
    [" ͟ʖ"],
    [" ʖ̯"],
    ["ω"],
    [" ³"],
    [" ε "],
    ["﹏"],
    ["□"],
    ["ل͜"],
    ["‿"],
    ["╭╮"],
    ["‿‿"],
    ["▾"],
    ["‸"],
    ["Д"],
    ["∀"],
    ["!"],
    ["人"],
    ["."],
    ["ロ"],
    ["_"],
    ["෴"],
    ["ѽ"],
    ["ഌ"],
    ["⏠"],
    ["⏏"],
    ["⍊"],
    ["⍘"],
    ["ツ"],
    ["益"],
    ["╭∩╮"],
    ["Ĺ̯"],
    ["◡"],
    [" ͜つ"],
]

EARS = [
    ["q", "p"],
    ["ʢ", "ʡ"],
    ["⸮", "?"],
    ["ʕ", "ʔ"],
    ["ᖗ", "ᖘ"],
    ["ᕦ", "ᕥ"],
    ["ᕦ(", ")ᕥ"],
    ["ᕙ(", ")ᕗ"],
    ["ᘳ", "ᘰ"],
    ["ᕮ", "ᕭ"],
    ["ᕳ", "ᕲ"],
    ["(", ")"],
    ["[", "]"],
    ["¯\\_", "_/¯"],
    ["୧", "୨"],
    ["୨", "୧"],
    ["⤜(", ")⤏"],
    ["☞", "☞"],
    ["ᑫ", "ᑷ"],
    ["ᑴ", "ᑷ"],
    ["ヽ(", ")ﾉ"],
    ["\\(", ")/"],
    ["乁(", ")ㄏ"],
    ["└[", "]┘"],
    ["(づ", ")づ"],
    ["(ง", ")ง"],
    ["⎝", "⎠"],
    ["ლ(", "ლ)"],
    ["ᕕ(", ")ᕗ"],
    ["(∩", ")⊃━☆ﾟ.*"],
]

TOSS = (
    "𝖧𝖾𝖺𝖽𝗌",
    "𝖳𝖺𝗂𝗅𝗌",
)

DECIDE = ("𝖸𝖾𝗌.", "𝖭𝗈.", "𝖬𝖺𝗒𝖻𝖾.")


# This feature's credit goes to @ishikki_akabane
FLIRT = (
    "𝖨 𝗁𝗈𝗉𝖾 𝗒𝗈𝗎 𝗄𝗇𝗈𝗐 𝖢𝖯𝖱, 𝖻𝖾𝖼𝖺𝗎𝗌𝖾 𝗒𝗈𝗎 𝗃𝗎𝗌𝗍 𝗍𝗈𝗈𝗄 𝗆𝗒 𝖻𝗋𝖾𝖺𝗍𝗁 𝖺𝗐𝖺𝗒!",
    "𝖲𝗈, 𝖺𝗌𝗂𝖽𝖾 𝖿𝗋𝗈𝗆 𝗍𝖺𝗄𝗂𝗇𝗀 𝗆𝗒 𝖻𝗋𝖾𝖺𝗍𝗁 𝖺𝗐𝖺𝗒, 𝗐𝗁𝖺𝗍 𝖽𝗈 𝗒𝗈𝗎 𝖽𝗈 𝖿𝗈𝗋 𝖺 𝗅𝗂𝗏𝗂𝗇𝗀?",
    "𝖨 𝗈𝗎𝗀𝗁𝗍 𝗍𝗈 𝖼𝗈𝗆𝗉𝗅𝖺𝗂𝗇 𝗍𝗈 𝖲𝗉𝗈𝗍𝗂𝖿𝗒 𝖿𝗈𝗋 𝗒𝗈𝗎 𝗇𝗈𝗍 𝖻𝖾𝗂𝗇𝗀 𝗇𝖺𝗆𝖾𝖽 𝗍𝗁𝗂𝗌 𝗐𝖾𝖾𝗄’𝗌 𝗁𝗈𝗍𝗍𝖾𝗌𝗍 𝗌𝗂𝗇𝗀𝗅𝖾.",
    "𝖸𝗈𝗎𝗋 𝖾𝗒𝖾𝗌 𝖺𝗋𝖾 𝗅𝗂𝗄𝖾 𝗍𝗁𝖾 𝗈𝖼𝖾𝖺𝗇; 𝖨 𝖼𝗈𝗎𝗅𝖽 𝗌𝗐𝗂𝗆 𝗂𝗇 𝗍𝗁𝖾𝗆 𝖺𝗅𝗅 𝖽𝖺𝗒.",
    "𝖶𝗁𝖾𝗇 𝖨 𝗅𝗈𝗈𝗄 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖾𝗒𝖾𝗌, 𝖨 𝗌𝖾𝖾 𝖺 𝗏𝖾𝗋𝗒 𝗄𝗂𝗇𝖽 𝗌𝗈𝗎𝗅.",
    "𝖨𝖿 𝗒𝗈𝗎 𝗐𝖾𝗋𝖾 𝖺 𝗏𝖾𝗀𝖾𝗍𝖺𝖻𝗅𝖾, 𝗒𝗈𝗎’𝖽 𝖻𝖾 𝖺 ‘𝖼𝗎𝗍𝖾-𝖼𝗎𝗆𝖻𝖾𝗋.’",
    "𝖣𝗈 𝗒𝗈𝗎 𝗁𝖺𝗉𝗉𝖾𝗇 𝗍𝗈 𝗁𝖺𝗏𝖾 𝖺 𝖡𝖺𝗇𝖽-𝖠𝗂𝖽? ‘𝖢𝖺𝗎𝗌𝖾 𝖨 𝗌𝖼𝗋𝖺𝗉𝖾𝖽 𝗆𝗒 𝗄𝗇𝖾𝖾𝗌 𝖿𝖺𝗅𝗅𝗂𝗇𝗀 𝖿𝗈𝗋 𝗒𝗈𝗎.",
    "𝖨 𝗇𝖾𝗏𝖾𝗋 𝖻𝖾𝗅𝗂𝖾𝗏𝖾𝖽 𝗂𝗇 𝗅𝗈𝗏𝖾 𝖺𝗍 𝖿𝗂𝗋𝗌𝗍 𝗌𝗂𝗀𝗁𝗍, 𝖻𝗎𝗍 𝗍𝗁𝖺𝗍 𝗐𝖺𝗌 𝖻𝖾𝖿𝗈𝗋𝖾 𝖨 𝗌𝖺𝗐 𝗒𝗈𝗎.",
    "𝖨 𝖽𝗂𝖽𝗇’𝗍 𝗄𝗇𝗈𝗐 𝗐𝗁𝖺𝗍 𝖨 𝗐𝖺𝗇𝗍𝖾𝖽 𝗂𝗇 𝖺 𝗐𝗈𝗆𝖺𝗇 𝗎𝗇𝗍𝗂𝗅 𝖨 𝗌𝖺𝗐 𝗒𝗈𝗎.",
    "𝖸𝗈𝗎’𝗋𝖾 𝗅𝗂𝗄𝖾 𝖺 𝖿𝗂𝗇𝖾 𝗐𝗂𝗇𝖾. 𝖳𝗁𝖾 𝗆𝗈𝗋𝖾 𝗈𝖿 𝗒𝗈𝗎 𝖨 𝖽𝗋𝗂𝗇𝗄 𝗂𝗇, 𝗍𝗁𝖾 𝖻𝖾𝗍𝗍𝖾𝗋 𝖨 𝖿𝖾𝖾𝗅.",
    "𝖸𝗈𝗎’𝗏𝖾 𝗀𝗈𝗍 𝖺 𝗅𝗈𝗍 𝗈𝖿 𝖻𝖾𝖺𝗎𝗍𝗂𝖿𝗎𝗅 𝖼𝗎𝗋𝗏𝖾𝗌, 𝖻𝗎𝗍 𝗒𝗈𝗎𝗋 𝗌𝗆𝗂𝗅𝖾 𝗂𝗌 𝖺𝖻𝗌𝗈𝗅𝗎𝗍𝖾𝗅𝗒 𝗆𝗒 𝖿𝖺𝗏𝗈𝗋𝗂𝗍𝖾.",
    "𝖨𝖿 𝖻𝖾𝗂𝗇𝗀 𝗌𝖾𝗑𝗒 𝗐𝖺𝗌 𝖺 𝖼𝗋𝗂𝗆𝖾, 𝗒𝗈𝗎’𝖽 𝖻𝖾 𝗀𝗎𝗂𝗅𝗍𝗒 𝖺𝗌 𝖼𝗁𝖺𝗋𝗀𝖾𝖽.",
    "𝖨 𝗐𝖺𝗌 𝗐𝗈𝗇𝖽𝖾𝗋𝗂𝗇𝗀 𝗂𝖿 𝗒𝗈𝗎’𝗋𝖾 𝖺𝗇 𝖺𝗋𝗍𝗂𝗌𝗍 𝖻𝖾𝖼𝖺𝗎𝗌𝖾 𝗒𝗈𝗎 𝗐𝖾𝗋𝖾 𝗌𝗈 𝗀𝗈𝗈𝖽 𝖺𝗍 𝖽𝗋𝖺𝗐𝗂𝗇𝗀 𝗆𝖾 𝗂𝗇.",
    "𝖨𝗍 𝗌𝖺𝗒𝗌 𝗂𝗇 𝗍𝗁𝖾 𝖡𝗂𝖻𝗅𝖾 𝗍𝗈 𝗈𝗇𝗅𝗒 𝗍𝗁𝗂𝗇𝗄 𝖺𝖻𝗈𝗎𝗍 𝗐𝗁𝖺𝗍’𝗌 𝗉𝗎𝗋𝖾 𝖺𝗇𝖽 𝗅𝗈𝗏𝖾𝗅𝗒… 𝖲𝗈 𝖨’𝗏𝖾 𝖻𝖾𝖾𝗇 𝗍𝗁𝗂𝗇𝗄𝗂𝗇𝗀 𝖺𝖻𝗈𝗎𝗍 𝗒𝗈𝗎 𝖺𝗅𝗅 𝖽𝖺𝗒 𝗅𝗈𝗇𝗀.",
    "𝖣𝗈 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝖺 𝗆𝖺𝗉? 𝖨 𝗃𝗎𝗌𝗍 𝗀𝗈𝗍 𝗅𝗈𝗌𝗍 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖾𝗒𝖾𝗌.",
    "𝖸𝗈𝗎 𝗄𝗇𝗈𝗐 𝗐𝗁𝖺𝗍 𝗒𝗈𝗎 𝗐𝗈𝗎𝗅𝖽 𝗅𝗈𝗈𝗄 𝗋𝖾𝖺𝗅𝗅𝗒 𝖻𝖾𝖺𝗎𝗍𝗂𝖿𝗎𝗅 𝗂𝗇? 𝖬𝗒 𝖺𝗋𝗆𝗌.",
    "𝖠𝗋𝖾 𝗒𝗈𝗎 𝖺 𝗆𝖺𝗀𝗂𝖼𝗂𝖺𝗇? 𝖨𝗍’𝗌 𝗍𝗁𝖾 𝗌𝗍𝗋𝖺𝗇𝗀𝖾𝗌𝗍 𝗍𝗁𝗂𝗇𝗀, 𝖻𝗎𝗍 𝖾𝗏𝖾𝗋𝗒 𝗍𝗂𝗆𝖾 𝖨 𝗅𝗈𝗈𝗄 𝖺𝗍 𝗒𝗈𝗎, 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝖾𝗅𝗌𝖾 𝖽𝗂𝗌𝖺𝗉𝗉𝖾𝖺𝗋𝗌.",
    "𝖨 𝗐𝗈𝗎𝗅𝖽 𝗇𝖾𝗏𝖾𝗋 𝗉𝗅𝖺𝗒 𝗁𝗂𝖽𝖾 𝖺𝗇𝖽 𝗌𝖾𝖾𝗄 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎 𝖻𝖾𝖼𝖺𝗎𝗌𝖾 𝗌𝗈𝗆𝖾𝗈𝗇𝖾 𝗅𝗂𝗄𝖾 𝗒𝗈𝗎 𝗂𝗌 𝗂𝗆𝗉𝗈𝗌𝗌𝗂𝖻𝗅𝖾 𝗍𝗈 𝖿𝗂𝗇𝖽.",
    "𝖨 𝗍𝗁𝗂𝗇𝗄 𝗍𝗁𝖾𝗋𝖾’𝗌 𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝗐𝗋𝗈𝗇𝗀 𝗐𝗂𝗍𝗁 𝗆𝗒 𝗉𝗁𝗈𝗇𝖾. 𝖢𝗈𝗎𝗅𝖽 𝗒𝗈𝗎 𝗍𝗋𝗒 𝖼𝖺𝗅𝗅𝗂𝗇𝗀 𝗂𝗍 𝗍𝗈 𝗌𝖾𝖾 𝗂𝖿 𝗂𝗍 𝗐𝗈𝗋𝗄𝗌?",
    "𝖠𝗋𝖾 𝗒𝗈𝗎 𝖺𝗇 𝖾𝗅𝖾𝖼𝗍𝗋𝗂𝖼𝗂𝖺𝗇? 𝖡𝖾𝖼𝖺𝗎𝗌𝖾 𝗒𝗈𝗎’𝗋𝖾 𝖽𝖾𝖿𝗂𝗇𝗂𝗍𝖾𝗅𝗒 𝗅𝗂𝗀𝗁𝗍𝗂𝗇𝗀 𝗎𝗉 𝗆𝗒 𝖽𝖺𝗒/𝗇𝗂𝗀𝗁𝗍!",
    "𝖨 𝖺𝗅𝗐𝖺𝗒𝗌 𝗍𝗁𝗈𝗎𝗀𝗁𝗍 𝗁𝖺𝗉𝗉𝗂𝗇𝖾𝗌𝗌 𝗌𝗍𝖺𝗋𝗍𝖾𝖽 𝗐𝗂𝗍𝗁 𝖺𝗇 ‘𝗁,’ 𝖻𝗎𝗍 𝗂𝗍 𝗍𝗎𝗋𝗇𝗌 𝗈𝗎𝗍 𝗆𝗂𝗇𝖾 𝗌𝗍𝖺𝗋𝗍𝗌 𝗐𝗂𝗍𝗁 ‘𝗎.’",
    "𝖨 𝖻𝖾𝗅𝗂𝖾𝗏𝖾 𝗂𝗇 𝖿𝗈𝗅𝗅𝗈𝗐𝗂𝗇𝗀 𝗆𝗒 𝖽𝗋𝖾𝖺𝗆𝗌. 𝖢𝖺𝗇 𝖨 𝗁𝖺𝗏𝖾 𝗒𝗈𝗎𝗋 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆?",
    "𝖨𝖿 𝗒𝗈𝗎 𝗐𝖾𝗋𝖾 𝖺 𝗌𝗈𝗇𝗀, 𝗒𝗈𝗎’𝖽 𝖻𝖾 𝗍𝗁𝖾 𝖻𝖾𝗌𝗍 𝗍𝗋𝖺𝖼𝗄 𝗈𝗇 𝗍𝗁𝖾 𝖺𝗅𝖻𝗎𝗆.",
    "𝖨𝗌 𝗒𝗈𝗎𝗋 𝗇𝖺𝗆𝖾 𝖦𝗈𝗈𝗀𝗅𝖾? 𝖡𝖾𝖼𝖺𝗎𝗌𝖾 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝖾𝗏𝖾𝗋𝗒𝗍𝗁𝗂𝗇𝗀 𝖨’𝗆 𝗌𝖾𝖺𝗋𝖼𝗁𝗂𝗇𝗀 𝖿𝗈𝗋.",
    "𝖣𝗈 𝗒𝗈𝗎 𝖾𝗏𝖾𝗋 𝗀𝖾𝗍 𝗍𝗂𝗋𝖾𝖽 𝖿𝗋𝗈𝗆 𝗋𝗎𝗇𝗇𝗂𝗇𝗀 𝗍𝗁𝗋𝗈𝗎𝗀𝗁 𝗆𝗒 𝗍𝗁𝗈𝗎𝗀𝗁𝗍𝗌 𝖺𝗅𝗅 𝗇𝗂𝗀𝗁𝗍?",
)


normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]