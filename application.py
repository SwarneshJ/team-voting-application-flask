from flask import Flask, render_template
import requests
import json
from models import TeamMember, EmailList
from models import db

app = application = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)

@app.route('/')
def home():
    # url endpoint to fetch list of all team members
    endpoint_url = "https://coding-assignment.g2crowd.com"

    res = requests.get(endpoint_url)
    response = json.loads(res.text)

    id = 0
    for item in response:
        item["count"] = 0
        item["id"] = id
        teamMember = TeamMember(
            item['name'],
            item['id'],
            item['title'],
            item['count']
        )
        id = id + 1

        # search the table whether this a team member with this name already exists
        existingMember = db.session.query(TeamMember).get(item['name'])

        # If team member already exists then reflect it's current vote count else add a new team member
        if existingMember is not None:
            item["count"] = existingMember.count
        else:
            db.session.add(teamMember)

    db.session.commit()

    # Render index.html webpage and pass earlier fetched data
    return render_template('index.html', payload = response)


@app.route("/initiate_vote/<id>/<email>", methods=["GET"])
def initiate_vote(id, email):
    print("email", email)

    # check whether this email has already been used to vote before
    existingEmail = db.session.query(EmailList).get(email)

    if existingEmail is not None:
        print("You have already voted!")
        return {
            "statusCode": 400,
            "message": "Error"
        }
    else:
        teamMember = TeamMember.query.filter_by(id=id).first()
        print("Voted for " + teamMember.name)
        teamMember.count = teamMember.count + 1

        # Add this email to used email list
        emailList = EmailList(
            email
        )
        db.session.add(emailList)
        db.session.commit()
        voteCount = teamMember.count
        return {
            "statusCode": 200,
            "message": str(voteCount)
        }



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
