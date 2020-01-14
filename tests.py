from flask import Blueprint, render_template, jsonify
from .test1 import (
    generate_output as generate_test1_output,
    get_json_data as get_test1_data,
    get_readme as get_test1_readme,
)
from .test2 import (
    generate_output as generate_test2_output,
    get_json_data as get_test2_data,
    get_readme as get_test2_readme,
)
from .test3 import (
    generate_output as generate_test3_output,
    get_json_data as get_test3_data,
    get_readme as get_test3_readme,
)

test = Blueprint("test", __name__)


@test.route("/", methods=["GET"])
def index():
    return render_template(
        "tests.html",
        test1_data=get_test1_data("data.json"),
        test1_output=get_test1_data("output.json"),
        test1_readme=get_test1_readme(),
        test2_data=get_test2_data("data.json"),
        test2_output=get_test2_data("output.json"),
        test2_readme=get_test2_readme(),
        test3_data=get_test3_data("data.json"),
        test3_output=get_test3_data("output.json"),
        test3_readme=get_test3_readme(),
    )


@test.route("/generate_test1", methods=["GET"])
def generate_test1():
    response = {"status": "success"}
    try:
        generate_test1_output()
    except Exception as e:
        return jsonify({"status": str(e)}), 500

    return jsonify(response), 200


@test.route("/generate_test2", methods=["GET"])
def generate_test2():
    response = {"status": "success"}
    try:
        generate_test2_output()
    except Exception as e:
        return jsonify({"status": str(e)}), 500

    return jsonify(response), 200


@test.route("/generate_test3", methods=["GET"])
def generate_test3():
    response = {"status": "success"}
    try:
        generate_test3_output()
    except Exception as e:
        return jsonify({"status": str(e)}), 500

    return jsonify(response), 200
