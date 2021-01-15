from flask import Flask, render_template, request
import requests
import multiprocessing
from deliverWine import deliver_wine


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def order():
    global robot_thread
    if request.method == "POST":
        if request.form["status"] == "working":
            try:
                robot_thread = multiprocessing.Process(target=deliver_wine)
                robot_thread.start()
            except:
                # can not start a process twice
                pass
            finally:
                return render_template("order.html")
        else:
            # return type(robot_tread)
            robot_thread.terminate()
            return render_template("index.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)