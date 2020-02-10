from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.user_id)


class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<City {}>'.format(self.city_id)


class Forecast(db.Model):
    forecast_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    forecast_datetime = db.Column(db.Text, nullable=False)
    forecast = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<Forecast {} at {}>'.format(self.forecast, self.forecast_datetime)
