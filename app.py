
import numpy as np



import sqlalchemy

from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import Session

from sqlalchemy import create_engine, func



from flask import Flask, jsonify



#################################################

# Database Setup

#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite") 



# reflect an existing database into a new model

Base = automap_base()

# reflect the tables

Base.prepare(engine, reflect=True)



# Save reference to the table

measurement = Base.classes.measurement

station = Base.classes.station



#################################################

# Flask Setup

#################################################

app = Flask(__name__)





#################################################

# Flask Routes



@app.route("/")

def index():

    return (

        f"Home Page<br/>"

        f"Available Routes:<br/>"

        f"/api/v1.0/precipitation<br/>"

        f"/api/v1.0/stations<br/>"

        f"/api/v1.0/tobs<br/>"

        f"/api/v1.0/start(YYYY-MM-DD)/end(YYYY-MM-DD)"

    )

    
if __name__ == "__main__":

    app.run(debug=True)