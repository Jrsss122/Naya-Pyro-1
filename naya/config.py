from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "17896688"))
OWNER = int(getenv("OWNER", "1948147616"))
API_HASH = getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://fadhil01:fadhil123@fadhil01.s6lkqsq.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6484534684:AAFhc381-zhXgXLXG9eNf37ED4DDafZc1yc")
OPENAI_API = getenv("OPENAI_API", "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")
GIT_TOKEN = getenv("GIT_TOKEN")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/naya1503/Naya-Pyro")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SESSION1 = getenv("SESSION1", "BQAP-GEAWKk1o3ejpMQR4vILM57-8FAQvuwwIoCyX4MRoxu98IJApE84qv0vYgM673PiTNPNL9Fqoc1Ce5gMA5IMUaHoGKsnXPRk3rruhJQKxX8uIvydXx0iizZsZ2ZXgRUkgOHpeYGzCtCAExFjv1uOUaMfE5NHd63eh3cYRRbezjQabggPb-5UkXhIhogn3S-0l27FSUbOL140RojfVPIzjkilqhPZbBKE8ntCN_gZNyM1coSAXNoSwhjmcCqUr3UFk4_SiR07_kjHLmMs7m3xvlY46F-5ZybAeJQmCkaPL88ZYL7iQi7VPfdCyPVZTG7nf04zuB_woSC4Ka8iNxUBC1HojAAAAABr5tUGAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
