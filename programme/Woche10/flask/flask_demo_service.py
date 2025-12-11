from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version="1.0", title="Todo API", description="Ein einfacher Todo REST-Service mit Swagger")

ns = api.namespace("todos", description="Todo-Operationen")

todo_model = api.model("Todo", {
    "id": fields.Integer(readonly=True, description="Die ID des Todos"),
    "task": fields.String(required=True, description="Die Aufgabe"),
    "done": fields.Boolean(description="Ob sie erledigt ist")
})

todos = [
    {"id": 1, "task": "Einkaufen", "done": False},
    {"id": 2, "task": "Hausaufgaben", "done": True}
]

@ns.route("/")
class TodoList(Resource):
    @ns.marshal_list_with(todo_model)
    def get(self):
        """Alle Todos abrufen"""
        return todos

    @ns.expect(todo_model)
    @ns.marshal_with(todo_model, code=201)
    def post(self):
        """Neues Todo erstellen"""
        data = api.payload
        new_todo = {
            "id": todos[-1]["id"] + 1 if todos else 1,
            "task": data["task"],
            "done": data.get("done", False)
        }
        todos.append(new_todo)
        return new_todo, 201

@ns.route("/<int:id>")
@ns.response(404, "Todo nicht gefunden")
@ns.param("id", "Die ID des Todos")
class Todo(Resource):
    @ns.marshal_with(todo_model)
    def get(self, id):
        """Ein Todo anzeigen"""
        todo = next((item for item in todos if item["id"] == id), None)
        if todo:
            return todo
        api.abort(404)

    @ns.response(204, "Erfolgreich gelöscht")
    def delete(self, id):
        """Ein Todo löschen"""
        global todos
        todos = [item for item in todos if item["id"] != id]
        return "", 204

    @ns.expect(todo_model)
    @ns.marshal_with(todo_model)
    def put(self, id):
        """Ein Todo aktualisieren"""
        todo = next((item for item in todos if item["id"] == id), None)
        if not todo:
            api.abort(404)
        data = api.payload
        todo.update(data)
        return todo

if __name__ == "__main__":
    app.run(debug=True)
