import numpy as np
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    # Basic NumPy calculation: create an array and compute the mean
    data_array = np.array([10, 20, 30, 40, 50])
    array_mean = float(np.mean(data_array))

    return jsonify(
        {
            "message": "Hello, World!",
            "numpy_demo": {
                "array": data_array.tolist(),
                "mean": array_mean,
            },
        }
    )


@app.route("/db-check")
def db_check():
    """Example route demonstrating psycopg2 usage."""
    try:
        # Example connection parameters (update with actual credentials)
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="password",
            host="localhost",
            port="5432",
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()

        return jsonify(
            {"status": "connected", "database_version": db_version[0]}
        )
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
