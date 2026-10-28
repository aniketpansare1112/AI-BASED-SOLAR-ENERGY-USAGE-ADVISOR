from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            panel_capacity = float(request.form.get("panel_capacity", 2))
            sunlight_hours = float(request.form.get("sunlight_hours", 5))
            efficiency_percent = float(request.form.get("efficiency", 80))
            daily_use = float(request.form.get("daily_use", 6))
            tariff = float(request.form.get("tariff", 8))

            if panel_capacity <= 0 or sunlight_hours < 0 or not 0 < efficiency_percent <= 100:
                raise ValueError("Please enter positive values and efficiency between 1 and 100.")
            if daily_use < 0 or tariff < 0:
                raise ValueError("Daily usage and tariff cannot be negative.")

            efficiency = efficiency_percent / 100
            solar_daily = panel_capacity * sunlight_hours * efficiency
            solar_monthly = solar_daily * 30
            usage_monthly = daily_use * 30
            surplus = solar_daily - daily_use
            estimated_grid = max(0, usage_monthly - solar_monthly)
            estimated_bill = estimated_grid * tariff

            if surplus >= 1:
                recommendation = "Your estimated solar generation is higher than daily usage. Run high-power appliances during sunny hours when practical."
                status = "surplus"
            elif surplus >= 0:
                recommendation = "Your estimated solar generation is close to your daily usage. Shift suitable appliances to daylight hours to use solar power effectively."
                status = "balanced"
            else:
                recommendation = "Your estimated daily usage is higher than solar generation. Consider reducing avoidable consumption and reviewing system capacity with a qualified installer."
                status = "deficit"

            result = {
                "solar_daily": round(solar_daily, 2),
                "solar_monthly": round(solar_monthly, 2),
                "usage_monthly": round(usage_monthly, 2),
                "surplus": round(surplus, 2),
                "grid": round(estimated_grid, 2),
                "bill": round(estimated_bill, 2),
                "recommendation": recommendation,
                "status": status,
            }
        except (ValueError, TypeError):
            error = "Please enter valid numbers. Efficiency must be between 1 and 100."
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
