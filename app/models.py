from . import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(6), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)
    campaign = db.Column(db.String(200), nullable=True)
    campaign_source = db.Column(db.String(200), nullable=True)
    ip_addresses = db.relationship('IPAddress', backref='url', lazy=True)

class IPAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), nullable=False)
    browser = db.Column(db.String(100))
    os = db.Column(db.String(100))
    referrer = db.Column(db.String(500))
    language = db.Column(db.String(100))
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
