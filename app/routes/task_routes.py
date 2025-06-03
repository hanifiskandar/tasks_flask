from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Task
from app.forms import TaskForm
from app import db

task_bp = Blueprint('task', __name__, url_prefix="/tasks")

@task_bp.route("/")
def list_tasks():
    tasks = Task.query.all()
    return render_template("tasks/index.html", tasks=tasks)

@task_bp.route("/create", methods=["GET", "POST"])
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("task.list_tasks"))
    return render_template("tasks/create.html", form=form)

@task_bp.route("/tasks/<int:id>")
def show_task(id):
    task = Task.query.get_or_404(id)
    return render_template("tasks/show.html", task=task)


@task_bp.route("/tasks/<int:id>/edit", methods=["GET", "POST"])
def edit_task(id):
    task = Task.query.get_or_404(id)
    form = TaskForm(obj=task)

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("task.list_tasks"))

    return render_template("tasks/edit.html", form=form)

@task_bp.route("/task/<int:id>/delete", methods=["POST"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("task.list_tasks"))
