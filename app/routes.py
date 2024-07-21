from flask import Flask, request, redirect, render_template, url_for, Blueprint
from . import db
from .models import URL, IPAddress
import string
import random
from datetime import datetime
import user_agents
import requests
from dotenv import load_dotenv
import os

IPINFO_API_KEY = os.getenv('IPINFO_API_KEY')

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    link = URL.query.filter_by(short_url=short_url).first()
    if link:
        return generate_short_url()
    return short_url

def get_location(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json?token={IPINFO_API_KEY}')
        data = response.json()
        return data.get('country'), data.get('city')
    except Exception as e:
        print(f"Error getting location data: {e}")
        return None, None

def serialize_ip(ip):
    return {
        'ip_address': ip.ip_address,
        'browser': ip.browser,
        'os': ip.os,
        'referrer': ip.referrer,
        'language': ip.language,
        'country': ip.country,
        'city': ip.city,
        'timestamp': ip.timestamp.isoformat()
    }

##app = Flask(__name__)
bp = Blueprint('main', __name__)

def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        campaign = request.form.get('campaign')
        campaign_source = request.form.get('campaign_source')
        short_url = generate_short_url()
        new_url = URL(original_url=original_url, short_url=short_url, campaign=campaign, campaign_source=campaign_source)
        db.session.add(new_url)
        db.session.commit()
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@bp.route('/<short_url>')
def redirect_to_url(short_url):
    link = URL.query.filter_by(short_url=short_url).first_or_404()
    link.clicks += 1
    ip_address = get_client_ip()
    user_agent_str = request.headers.get('User-Agent')
    user_agent = user_agents.parse(user_agent_str)
    browser = user_agent.browser.family
    os = user_agent.os.family
    referrer = request.referrer
    language = request.headers.get('Accept-Language').split(',')[0]
    country, city = get_location(ip_address)
    db.session.add(IPAddress(ip_address=ip_address, browser=browser, os=os, referrer=referrer, language=language, country=country, city=city, url=link))
    db.session.commit()
    return redirect(link.original_url)

@bp.route('/stats/<short_url>')
def stats(short_url):
    link = URL.query.filter_by(short_url=short_url).first_or_404()
    ip_addresses = [serialize_ip(ip) for ip in link.ip_addresses]
    return render_template('stats.html', url=link, ip_addresses=ip_addresses)
