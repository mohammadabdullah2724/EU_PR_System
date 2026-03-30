from flask import Flask, render_template, request, send_file
from database import init_db, get_all_countries
from scraper import scrape_sample_data
from export_excel import export_to_excel

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    countries = get_all_countries()
    return render_template('index.html', countries=countries)

@app.route('/scrape')
def scrape():
    scrape_sample_data()
    return "Scraping completed!"

@app.route('/export')
def export():
    file_path = export_to_excel()
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)