# Copyright (c) 2025, Marco Noce <nce.marco@gmail.com>
# GNU General Public License v3.0+
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import Flask, jsonify
from bot import start_bot

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "schemaVersion": 1,
        "label": "3A2BOT",
        "message": "alive",
        "color": "green"
    }), 200

if __name__ == "__main__":
    start_bot()
    app.run(host="0.0.0.0", port=10000)
