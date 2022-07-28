from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

funny_story = silly_story  # needed to set this to variable so that we can use it
exciting_story = excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# {% set name = {{prompt}} %}
# run flask again when changing files

debug = DebugToolbarExtension(app)

@app.get('/')
def home_page():
    """ create homepage for user to choose story """
    return render_template("home.html")

@app.get('/questions')
def questions_page():
    """ create a form for user inputs needed for story """
    global story
    story = funny_story if request.args.get("story") == "silly" else exciting_story

    return render_template("questions.html", prompts = story.prompts)
    # needed to put in argument for prompts so we have it available
    # putting in the argument here makes it so we don't need to include script in html

@app.get('/results')
def results_page():
    """ displays a page with the story that the user created """
    answers = request.args # request.args is basically a dictionary with query as key, and value as value

    return render_template("results.html", story = story.generate(answers))