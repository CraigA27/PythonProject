from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    return render_template("/members/show.html", member=member)

@members_blueprint.route("/members/new")
def new_member():
    return render_template("/members/new.html")

@members_blueprint.route("/members", methods=["POST"])
def add_member():
    name = request.form["name"]
    age = request.form["age"]
    membership = request.form["membership"]
    status = request.form["status"]
    new_member = Member(name, age, membership, status)
    member_repository.save(new_member)
    return redirect ("/members")

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)   
    return render_template("/members/edit.html", member=member)

@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    age = request.form["age"]
    membership = request.form["membership"]
    status = request.form["status"]
    member = Member(name, age, membership, status, id)
    member_repository.update(member)
    return redirect("/members")


@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete(id):
    member_repository.delete(id)
    return redirect("/members")


