AI-BASED SOLAR ENERGY USAGE ADVISOR — RUN GUIDE

Requirements:
- Python 3.10 or newer recommended
- Internet connection for the Chart.js CDN chart (calculations still run locally)

Run on Windows:
1. Extract the ZIP folder.
2. Open a terminal in the extracted project folder.
3. Run: py -m venv .venv
4. Activate: .venv\Scripts\activate
5. Install dependencies: pip install -r requirements.txt
6. Start: python app.py
7. Open: http://127.0.0.1:5000

If `py` does not work, try `python`.

Project notes:
- Python + Flask backend; HTML/CSS/JavaScript frontend.
- Recommendations use predefined IF–THEN rules. This is a rule-based AI prototype, not a trained ML model.
- Results are estimates, not a professional solar assessment or an exact electricity bill.
- Replace the illustrative report screenshots/test outcomes with your own after running the site.
