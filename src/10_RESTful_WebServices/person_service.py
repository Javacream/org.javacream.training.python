from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Any

from flask import Flask, request, jsonify, make_response, url_for

app = Flask(__name__)

# -----------------------------
# Model
# -----------------------------
@dataclass
class Person:
    id: int
    lastname: str
    firstname: str
    height: float
    weight: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

# -----------------------------
# In-memory storage (Demo)
# -----------------------------
_persons: Dict[int, Person] = {}
_next_id: int = 1

def _new_id() -> int:
    global _next_id
    pid = _next_id
    _next_id += 1
    return pid

# -----------------------------
# Validation
# -----------------------------
REQUIRED_FIELDS = {"lastname", "firstname", "height", "weight"}
ALLOWED_FIELDS = set(REQUIRED_FIELDS)

def _as_float(value: Any, field: str) -> float:
    try:
        f = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"Field '{field}' must be a number.")
    return f

def _validate_payload(data: Any, *, partial: bool) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValueError("JSON body must be an object.")

    unknown = set(data.keys()) - ALLOWED_FIELDS
    if unknown:
        raise ValueError(f"Unknown field(s): {sorted(unknown)}")

    if not partial:
        missing = REQUIRED_FIELDS - set(data.keys())
        if missing:
            raise ValueError(f"Missing field(s): {sorted(missing)}")

    out: Dict[str, Any] = {}

    if "lastname" in data:
        if not isinstance(data["lastname"], str) or not data["lastname"].strip():
            raise ValueError("Field 'lastname' must be a non-empty string.")
        out["lastname"] = data["lastname"].strip()

    if "firstname" in data:
        if not isinstance(data["firstname"], str) or not data["firstname"].strip():
            raise ValueError("Field 'firstname' must be a non-empty string.")
        out["firstname"] = data["firstname"].strip()

    if "height" in data:
        h = _as_float(data["height"], "height")
        if h <= 0:
            raise ValueError("Field 'height' must be > 0.")
        out["height"] = h

    if "weight" in data:
        w = _as_float(data["weight"], "weight")
        if w <= 0:
            raise ValueError("Field 'weight' must be > 0.")
        out["weight"] = w

    return out

def _problem(status: int, title: str, detail: str):
    return make_response(jsonify({"status": status, "title": title, "detail": detail}), status)

# -----------------------------
# Routes
# -----------------------------
@app.get("/persons")
def list_persons():
    return jsonify([p.to_dict() for p in _persons.values()]), 200

@app.post("/persons")
def create_person():
    try:
        data = request.get_json(force=True, silent=False)
        cleaned = _validate_payload(data, partial=False)
    except Exception as e:
        return _problem(400, "Bad Request", str(e))

    pid = _new_id()
    person = Person(id=pid, **cleaned)
    _persons[pid] = person

    resp = jsonify(person.to_dict())
    resp.status_code = 201
    resp.headers["Location"] = url_for("get_person", id=pid, _external=True)
    return resp

@app.get("/persons/<int:id>")
def get_person(id: int):
    p = _persons.get(id)
    if not p:
        return _problem(404, "Not Found", f"Person with id={id} not found.")
    return jsonify(p.to_dict()), 200

@app.put("/persons/<int:id>")
def replace_person(id: int):
    if id not in _persons:
        return _problem(404, "Not Found", f"Person with id={id} not found.")
    try:
        data = request.get_json(force=True, silent=False)
        cleaned = _validate_payload(data, partial=False)
    except Exception as e:
        return _problem(400, "Bad Request", str(e))

    _persons[id] = Person(id=id, **cleaned)
    return jsonify(_persons[id].to_dict()), 200

@app.patch("/persons/<int:id>")
def update_person(id: int):
    p = _persons.get(id)
    if not p:
        return _problem(404, "Not Found", f"Person with id={id} not found.")
    try:
        data = request.get_json(force=True, silent=False)
        cleaned = _validate_payload(data, partial=True)
    except Exception as e:
        return _problem(400, "Bad Request", str(e))

    for k, v in cleaned.items():
        setattr(p, k, v)
    return jsonify(p.to_dict()), 200

@app.delete("/persons/<int:id>")
def delete_person(id: int):
    if id not in _persons:
        return _problem(404, "Not Found", f"Person with id={id} not found.")
    del _persons[id]
    return ("", 204)

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
