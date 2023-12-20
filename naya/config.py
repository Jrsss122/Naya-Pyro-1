from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "17896688"))
OWNER = int(getenv("OWNER", "1948147616"))
API_HASH = getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://fadhil01:fadhil123@fadhil01.s6lkqsq.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6885113809:AAFv0w3Pn2gl6ICX0eNWXnEwmz1n4zWZEMw")
OPENAI_API = getenv("OPENAI_API", "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")
GIT_TOKEN = getenv("GIT_TOKEN")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "73258cce-3f52-4405-808b-5ca0cb6cb7e6")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/naya1503/Naya-Pyro")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SESSION1 = getenv("SESSION1", "BQFdvl8AM-9Y9GhNzEHrf5XxXO9bT_bNH8llVs_1190GM2FMxlt8N_0Ltl4qKswu79pef75-JNdmvSKV-CxM1g6o3Jt-Mr5cRkDOaYv-SqxQZDHXEjH2MjEIObOD7Qhe9TisN5JXtCvLPinynYmy8YQzp0BhUX4I8Enmtt4NRe6GMuV9eottalx3x5DlrhqHDdVdldovXYZ_ehLIY2lRcRODA6cD0Vwi7omJBykehTVySw4up-rCdHU2mkxrM-MGb-0BG3vrAYtXfEE4gYQ1kAJJFIfnzjoH1rBsoKq7IlMMYSqRD5SRA48I0hoCyG5HMAyjQK1o2EQrVYC5UEufLD5SS0dEkAAAAABEzwJlAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
