

from flask import Flask

# Requirements :
# - Pandas is your friend
# - Data sanitation is not an illness

# TODO :
#   An investor has an initial wallet value. In performance, you can check performance of the wallet for each date.
# - Compute wallet value over time - Performance data is in %
# - Create a endpoint to access data in JSON of one investor from its ID
# - Scrap the 3 last posts of this Organization on LinkedIN : "https://www.linkedin.com/company/tesla-motors/" and return informations in JSON format through an endpoint "GET /linkedin/tesla_posts"
# - Do what you should for such a software if you'd work with us

# This test should not take you more than 1h, if you do not have enough time, explain what you would have done 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Read the todo into the code ;)'
