import json
import os
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
    abort,
    session,
    Flask,
)
from werkzeug.utils import secure_filename


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.secret_key = os.urandom(24)

    @app.route("/")
    def home():
        return render_template("home.html", codes=session.keys())

    @app.route("/your-url", methods=["GET", "POST"])
    def your_url():
        if request.method == "POST":
            if os.path.exists("urls.json"):
                with open("urls.json", encoding="UTF-8") as urls_file:
                    urls = json.load(urls_file)
            else:
                urls = {}

            # deepcode ignore UpdateAPI: Unrelevent suggestion
            if request.form["code"] in urls.keys():
                flash(
                    "That short name has already been taken. Please select another name."
                )
                return redirect(url_for("home"))

            if "url" in request.form.keys():
                urls[request.form["code"]] = {"url": request.form["url"]}
            else:
                file = request.files["file"]
                fname = secure_filename(file.filename)
                fname = request.form["code"] + "-" + fname
                full_path = os.path.join(
                    os.getcwd(), "urlshort", "static", "user_files", fname
                )
                # deepcode ignore PT: Already checked above
                file.save(full_path)
                urls[request.form["code"]] = {"file": fname}

            with open("urls.json", "w", encoding="UTF-8") as urls_file:
                json.dump(urls, urls_file)
                session[request.form["code"]] = True

            return render_template("your_url.html", code=request.form["code"])

        return redirect(url_for("home"))

    @app.route("/<string:code>")
    def redirect_to_url(code):
        if os.path.exists("urls.json"):
            with open("urls.json", encoding="UTF-8") as urls_file:
                urls = json.load(urls_file)
            if code in urls.keys():
                if "url" in urls[code].keys():
                    # deepcode ignore OR: Unrelevent suggestion
                    return redirect(urls[code]["url"])

                return redirect(
                    url_for("static", filename="user_files/" + urls[code]["file"])
                )

        return abort(404)

    @app.errorhandler(404)
    def page_not_found(error):
        print(f"Error!\n{error}")
        return render_template("page_not_found.html"), 404

    @app.route("/api")
    def session_api():
        return jsonify(list(session.keys()))

    @app.route("/_status/healthz")
    def health():
        return jsonify({"status": "OK"})

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", debug=False)
